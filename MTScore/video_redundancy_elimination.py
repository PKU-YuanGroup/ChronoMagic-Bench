import argparse
import numpy as np
import os
import cv2
import json
import torch
from tqdm import tqdm
import shutil
import time
from configs.config import Config, eval_dict_leaf
from configs.utils import retrieve_text, _frame_from_video, setup_internvideo2

def parse_args():
    parser = argparse.ArgumentParser(description="Video Score Calculation")
    parser.add_argument("--seed", type=int, default=1421538, help="Random seed")
    parser.add_argument("--model_name", type=str, default="test", help="Model name")
    parser.add_argument("--input_folder", type=str, default="../toy_video", help="Input folder containing videos")
    parser.add_argument("--output_folder", type=str, default="classify_videos", help="Output folder for saving scores")
    parser.add_argument("--config_path", type=str, default='configs/internvideo2_stage2_config.py', help="Path to config file")
    parser.add_argument("--model_pth", type=str, default='InternVideo2-stage2_1b-224p-f4.pt', help="Path to model checkpoint")
    return parser.parse_args()

def retry_setup(config, max_attempts=3, delay=2):
    attempts = 0
    while attempts < max_attempts:
        try:
            intern_model, tokenizer = setup_internvideo2(config)
            return intern_model, tokenizer
        except Exception as e:
            print(f"Attempt {attempts + 1} failed: {e}")
            attempts += 1
            if attempts == max_attempts:
                raise Exception("All attempts failed.")
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

def calculate_video_score(video_path, text_to_index, text_candidates, intern_model, config):
    video = cv2.VideoCapture(video_path)
    frames = [x for x in _frame_from_video(video)]

    texts, probs = retrieve_text(frames, text_candidates, model=intern_model, topk=5, config=config)

    general_prob = 0.0
    metamorphic_prob = 0.0

    for t, p in zip(texts, probs):
        text_index = text_to_index[t]
        if text_index in [0, 1, 2, 3, 4]:
            general_prob += p
        else:
            metamorphic_prob += p

    return general_prob, metamorphic_prob

def calculate_average_score(scores):
    total_videos = len(scores)
    total_general_score = sum(score[0] for score in scores)
    total_metamorphic_score = sum(score[1] for score in scores)
    average_general_score = total_general_score / total_videos
    average_metamorphic_score = total_metamorphic_score / total_videos
    return average_general_score, average_metamorphic_score

def load_existing_scores(filepath):
    scores = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f:
                scores.append(json.loads(line))
    return scores

def main():
    args = parse_args()

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    config = Config.from_file(args.config_path)
    config = eval_dict_leaf(config)

    config['model']['vision_encoder']['pretrained'] = args.model_pth

    intern_model, tokenizer = retry_setup(config, max_attempts=10, delay=2)

    text_candidates = [
        "A conventional video, not a time-condensed video.",
        "A usual video, not an accelerated video sequence.",
        "A normal video, not a time-lapse video.",
        "A standard video, not a time-lapse.",
        "An ordinary video, different from a fast-motion video.",
        "A time-lapse video, distinct from a regular recording.",
        "A time-lapse footage, not your typical video.",
        "A fast-motion video, unlike a standard video.",
        "A time-condensed video, not a conventional video.",
        "An accelerated video sequence, not a usual video.",
    ]

    text_to_index = {text: index for index, text in enumerate(text_candidates)}
    video_folder = os.path.join(args.input_folder, args.model_name)
    
    folder_a = os.path.join(args.output_folder, "general_videos")
    folder_b = os.path.join(args.output_folder, "metamorphic_videos")
    os.makedirs(folder_a, exist_ok=True)
    os.makedirs(folder_b, exist_ok=True)

    for video_file in tqdm(os.listdir(video_folder), desc="Processing videos"):
        if video_file.endswith('.mp4'):
            video_path = os.path.join(video_folder, video_file)
            general_score, metamorphic_score = calculate_video_score(video_path, text_to_index, text_candidates, intern_model, config)

            if general_score > 0.5:
                destination = os.path.join(folder_a, video_file)
                shutil.copy2(video_path, destination)
                print(f"Copied {video_file} to folder A (general_videos)")
            else:
                destination = os.path.join(folder_b, video_file)
                shutil.copy2(video_path, destination)
                print(f"Copied {video_file} to folder B (metamorphic_videos)")

if __name__ == "__main__":
    main()