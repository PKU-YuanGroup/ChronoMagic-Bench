import datetime
import logging
import time

import numpy as np
import torch
import torch.distributed as dist
import torch.nn.functional as F
from einops import rearrange

from models.criterions import get_sim
from utils.basic_utils import MetricLogger
from utils.distributed import get_rank, get_world_size

logger = logging.getLogger(__name__)


def extract_text_feats(texts, max_txt_l, tokenizer, model, device):
    num_text = len(texts)
    text_bs = 256
    text_feats = []
    text_atts = []

    for i in range(0, num_text, text_bs):
        text = texts[i : min(num_text, i + text_bs)]
        text_input = tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=max_txt_l,
            return_tensors="pt",
        ).to(device)

        text_feat = model.encode_text(text_input)[0]
        text_feats.append(text_feat)
        text_atts.append(text_input.attention_mask)

    text_feats = torch.cat(text_feats, dim=0)
    text_atts = torch.cat(text_atts, dim=0)
    return text_feats, text_atts


def extract_vision_feats(data_loader, model, device, config):
    image_feats_all = []
    pooled_image_feats_all = []
    metric_logger = MetricLogger(delimiter="  ")
    header = "extracting image feats"
    iterator = metric_logger.log_every(data_loader, 100, header)
    for image, img_id in iterator:
        image = image.to(device, non_blocking=True)
        image_feat, pooled_image_feat = model.encode_vision(image, test=True)
        if config.evaluation.eval_frame_ensemble == "concat":  # default
            if len(image_feat.shape) == 4:
                image_feat = rearrange(image_feat, "b t l c -> b (t l) c").contiguous()
            image_feat = image_feat.unsqueeze(1)  # (bsz, 1, #frm*L, d)
        else:
            assert config.video_input.num_frames == 1, "only support single-frame"
            assert config.evaluation.eval_frame_ensemble in ["mean", "max", "lse"]
        if config.evaluation.eval_offload:
            image_feats_all.append(image_feat.cpu())
            pooled_image_feats_all.append(pooled_image_feat.cpu())
        else:
            image_feats_all.append(image_feat)
            pooled_image_feats_all.append(pooled_image_feat)

    image_feats_all = torch.cat(image_feats_all, dim=0)

    pooled_image_feats_all = torch.cat(pooled_image_feats_all, dim=0)
    return image_feats_all, pooled_image_feats_all


@torch.no_grad()
def evaluation_wrapper(model, data_loader, tokenizer, device, config, prefix=""):
    with torch.cuda.amp.autocast(enabled=config.fp16):
        # it2_emd is based on the similarity between text and vision output embeddings, i2t_x computes the it matching score using another fusion module
        video_feats = evaluation(
            model, data_loader, tokenizer, device, config
        )
    return video_feats


@torch.no_grad()
def evaluation(model, data_loader, tokenizer, device, config):
    model.eval()

    metric_logger = MetricLogger(delimiter="  ")
    header = "Evaluation:"
    dtype = torch.half if config.fp16 else torch.float
    media_type = data_loader.dataset.media_type
    logger.info(f"Start evaluation for media_type={media_type}")

    logger.info("Computing dual encoder features...")
    start_time = time.time()

    # this computes all features in each GPU
    # texts = data_loader.dataset.text
    # max_txt_l = config.inputs.max_txt_l
    # if not isinstance(max_txt_l, int):
    #     max_txt_l = max_txt_l[media_type]
    # text_feats, text_atts = extract_text_feats(
    #     texts, max_txt_l, tokenizer, model, device
    # )  # (bsz, Lt, d), (bsz, Lt)

    image_feats, pooled_image_feats = extract_vision_feats(
        data_loader, model, device, config
    )  # (bsz, 1, #frm*Li, d) or (bsz, #frm, Li, d), (bsz, #frm, d)
    logger.info("Finished feature extraction")
    _pooled_image_feats = (
        pooled_image_feats.to(device, non_blocking=True)
        if config.evaluation.eval_offload
        else pooled_image_feats
    )

    total_time = time.time() - start_time
    total_time_str = str(datetime.timedelta(seconds=int(total_time)))
    logger.info(f"Evaluation time {total_time_str}")
    return model.vision_proj(_pooled_image_feats).mean(1).cpu()


@torch.no_grad()
def itm_eval(scores_i2t, scores_t2i, txt2img, img2txt):
    # Images->Text
    ranks = np.zeros(scores_i2t.shape[0])
    for index, score in enumerate(scores_i2t):
        inds = np.argsort(score)[::-1]
        # Score
        gt_txt_ids = img2txt[index]
        if isinstance(gt_txt_ids, int):
            ranks[index] = np.where(inds == gt_txt_ids)[0][0]
        else:
            rank = 1e20
            for i in gt_txt_ids:
                tmp = np.where(inds == i)[0][0]
                if tmp < rank:
                    rank = tmp
            ranks[index] = rank

    # Compute metrics
    tr1 = 100.0 * len(np.where(ranks < 1)[0]) / len(ranks)
    tr5 = 100.0 * len(np.where(ranks < 5)[0]) / len(ranks)
    tr10 = 100.0 * len(np.where(ranks < 10)[0]) / len(ranks)

    # Text->Images
    ranks = np.zeros(scores_t2i.shape[0])

    for index, score in enumerate(scores_t2i):
        inds = np.argsort(score)[::-1]
        gt_img_ids = txt2img[index]
        if isinstance(gt_img_ids, int):
            ranks[index] = np.where(inds == gt_img_ids)[0][0]
        else:  # list, used in the case each caption has multiple GT images
            # Score
            rank = 1e20
            for i in gt_img_ids:
                tmp = np.where(inds == i)[0][0]
                if tmp < rank:
                    rank = tmp
            ranks[index] = rank

    # Compute metrics
    ir1 = 100.0 * len(np.where(ranks < 1)[0]) / len(ranks)
    ir5 = 100.0 * len(np.where(ranks < 5)[0]) / len(ranks)
    ir10 = 100.0 * len(np.where(ranks < 10)[0]) / len(ranks)

    tr_mean = (tr1 + tr5 + tr10) / 3
    ir_mean = (ir1 + ir5 + ir10) / 3
    r_mean = (tr_mean + ir_mean) / 2

    eval_result = {
        "txt_r1": tr1,
        "txt_r5": tr5,
        "txt_r10": tr10,
        "txt_r_mean": tr_mean,
        "img_r1": ir1,
        "img_r5": ir5,
        "img_r10": ir10,
        "img_r_mean": ir_mean,
        "r_mean": r_mean,
    }
    eval_result = {k: round(v, 2) for k, v in eval_result.items()}
    return eval_result
