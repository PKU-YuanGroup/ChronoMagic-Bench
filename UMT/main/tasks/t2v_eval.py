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
import json
import argparse

from dataset import MetaLoader
from models.umt import UMT
from tasks.pretrain import setup_testloaders
from tasks.t2v_eval_utils import evaluation_wrapper
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
        sim_scores, avg_sim_scores = evaluation_wrapper(
            model_without_ddp, test_loader, tokenizer, device, config
        )
        # id mapping, skipping unusual prompts (531-608) that do not contain real videos
        if 'fetv_anno_real.json' in config.test_file.test[0]:
            for key in sim_scores:
                for id in range(531, 541):
                    sim_scores[key].update({str(id+78): sim_scores[key][str(id)]})
                    sim_scores[key].pop(str(id))

    if is_main_process():
        if config.evaluate:
            save_file = "UMTScore.json"
            with open(join(config.output_dir, save_file), 'w') as f:
                json.dump(sim_scores["UMTScore"], f)
                
        sim_scores = pd.DataFrame(sim_scores)
        print(sim_scores)
        print(f"Avg UMTScores: {avg_sim_scores}")
        with open(join(config.output_dir, 'scores.txt'), 'w') as file:
            file.write(f"Avg UMTScores: {avg_sim_scores}\n")

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