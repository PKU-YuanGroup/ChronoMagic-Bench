import copy
import datetime
import logging
import os
import time
from os.path import join

import pandas as pd
import torch
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import wandb

from dataset import MetaLoader
from models.umt import UMT
from tasks.pretrain import setup_testloaders
from tasks.video_feature_extract_utils import evaluation_wrapper
from tasks.shared_utils import setup_model
from utils.basic_utils import MetricLogger, SmoothedValue, setup_seed
from utils.config import Config
from utils.config_utils import setup_main
from utils.distributed import get_rank, is_main_process
from utils.logger import log_dict_to_wandb, setup_wandb


logger = logging.getLogger(__name__)


def main(config):
    if is_main_process() and config.wandb.enable:
        run = setup_wandb(config)

    logger.info(f"config: \n{config}")

    setup_seed(config.seed + get_rank())
    device = torch.device(config.device)
    cudnn.benchmark = True

    test_loader = setup_testloaders(config, mode="ret")
    config.scheduler.num_training_steps = 0
    config.scheduler.num_warmup_steps = 0

    model_cls = eval(config.model.get('model_cls', 'UMT'))
    (
        model,
        model_without_ddp,
        optimizer,
        scheduler,
        scaler,
        tokenizer,
        start_epoch,
        global_step,
    ) = setup_model(
        config,
        model_cls=model_cls,
        has_decoder=False,
        pretrain=False,
        # find_unused_parameters=True,
        find_unused_parameters=False,
    )
    if is_main_process() and config.wandb.enable:
        wandb.watch(model)

    logger.info("Start " + "evaluation" if config.evaluate else "training")
    start_time = time.time()
    with torch.cuda.amp.autocast(enabled=config.fp16):
        video_feats = evaluation_wrapper(
            model_without_ddp, test_loader, tokenizer, device, config
        )

    if is_main_process():
        torch.save(video_feats, join(config.output_dir, f'{os.path.basename(config.output_dir)}.pt'))

    dist.barrier()

    total_time = time.time() - start_time
    total_time_str = str(datetime.timedelta(seconds=int(total_time)))
    logger.info(f"Evaluation time {total_time_str}")
    logger.info(f"Checkpoints and Logs saved at {config.output_dir}")

    if is_main_process() and config.wandb.enable:
        run.finish()


if __name__ == "__main__":
    cfg = setup_main()
    main(cfg)