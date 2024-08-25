import os
import json
import torch
import imageio
import numpy as np
import argparse
from PIL import Image
from tqdm import tqdm

from cotracker.predictor import CoTrackerPredictor

def parse_args():
    parser = argparse.ArgumentParser(description="Process videos and calculate coherence scores.")
    parser.add_argument('--model_pth', type=str, default="cotracker2.pth", help="Path to the model checkpoint.")
    parser.add_argument('--input_folder', type=str, default="../toy_video", help="Folder containing input videos.")
    parser.add_argument('--output_folder', type=str, default="results/all", help="Folder to save output results.")
    parser.add_argument('--model_names', nargs='+', default=["test"], help="Name of the models.")
    parser.add_argument('--grid_size', type=int, default=30, help="Grid size for the model.")
    parser.add_argument('--threshold', type=float, default=0.1, help="Threshold for determining frame cuts.")
    parser.add_argument('--size', type=int, default=None, help="Resize the shortest edge of the frame to this size.")
    parser.add_argument('--eval_type', type=int, choices=[150, 1649], default=150)
    return parser.parse_args()

def read_video_from_path(path, size=None):
    try:
        reader = imageio.get_reader(path)
    except Exception as e:
        print("Error opening video file: ", e)
        return None
    
    frames = []
    for i, im in enumerate(reader):
        image = Image.fromarray(im)
        if size is not None:
            if min(image.size) > size:
                scale = size / min(image.size)
                new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        frames.append(np.array(image))
    return np.stack(frames)

def process_video(video_path, size):
    video_original = read_video_from_path(video_path, size)
    video_tensor = torch.from_numpy(video_original).permute(0, 3, 1, 2)[None].float()
    return video_original, video_tensor

def get_score(model, video, grid_size=30, threshold=0.1):
    _, pred_visibility = model(video, grid_size=grid_size)
    _, frames, point_num = pred_visibility.shape
    
    miss_points = torch.sum(pred_visibility[0, :, :] == 0, dim=1).float() / point_num
    miss_points_ap = miss_points[1:] - miss_points[:-1]
    frames_to_be_cut = (miss_points_ap > threshold).nonzero(as_tuple=True)[0] + 1
    frames_to_be_cut = frames_to_be_cut.cpu().tolist()

    global_stats = {
        "AMPR_score": {"max": 0.9368749856948853, "min": 0.0},
        "MPVR_score": {"max": 0.8997353911399841, "min": 0.0},
        "FCR_score": {"max": 0.625, "min": 0.0},
        "CMPV_score": {"max": 20, "min": 0},
        "MCMPV_score": {"max": 1.0, "min": 0.0},
    }

    weights = {
        "CMPV_score": 0.15,
        "FCR_score": 0.15,
        "AMPR_score": 0.35,
        "MPVR_score": 0.25,
        "MCMPV_score": 0.10,
    }

    # Calculate raw scores
    raw_scores = {
        'AMPR_score': miss_points.mean().item(),
        'MPVR_score': miss_points_ap.std().item(),
        'FCR_score': len(frames_to_be_cut) / frames,
        'CMPV_score': (miss_points_ap > threshold).sum().item(),
        'MCMPV_score': miss_points_ap.max().item(),
    }

    # Normalize scores
    normalized_scores = {}
    for key, value in raw_scores.items():
        min_val = global_stats[key]['min']
        max_val = global_stats[key]['max']
        normalized_scores[key] = (value - min_val) / (max_val - min_val) if max_val != min_val else 0

    # Calculate TSI_sum
    TSI_sum = sum(normalized_scores[key] * weights[key] for key in normalized_scores)

    # Add normalized values to the scores dictionary
    scores = {key: normalized_scores[key] for key in normalized_scores}
    scores['TSI_sum'] = TSI_sum

    # Calculate TSI_score
    scores['TSI_score'] = 1 / TSI_sum if TSI_sum != 0 else 0

    return scores

def main(args):
    model = CoTrackerPredictor(checkpoint=os.path.join(args.model_pth))

    if torch.cuda.is_available():
        model = model.cuda()

    for model_name in tqdm(args.model_names, desc="Processing models"):
        if args.eval_type == 1649:
            for part in tqdm(["1", "2", "3"], desc="Processing parts", leave=False):
                input_dir = os.path.join(args.input_folder, model_name, part)
                output_file_path = os.path.join(args.output_folder, f"{model_name}_{part}_CHScore.json")

                if not os.path.exists(args.output_folder):
                    os.makedirs(args.output_folder)
                
                if os.path.exists(output_file_path):
                    with open(output_file_path, 'r') as existing_file:
                        all_scores_data = json.load(existing_file).get("all_scores", [])
                else:
                    all_scores_data = []
                
                processed_video_names = {list(video_scores.keys())[0] for video_scores in all_scores_data}

                for video_file in tqdm(os.listdir(input_dir), unit='video', leave=False):
                    if video_file.endswith('.mp4'):
                        video_path = os.path.join(input_dir, video_file)
                        video_name = video_file.split('.mp4')[0]

                        if video_name in processed_video_names:
                            print(f"Skipping {video_name} as it already exists.")
                            continue

                        _, video = process_video(video_path, args.size)

                        if torch.cuda.is_available():
                            video = video.cuda()

                        scores = get_score(model, video, args.grid_size, args.threshold)
                        all_scores_data.append({video_name: scores})

                total_average_score = sum([list(video_scores.values())[0]['TSI_score'] for video_scores in all_scores_data]) / len(all_scores_data) if all_scores_data else 0

                merged_data = {
                    "total_average_score": total_average_score,
                    "all_scores": all_scores_data
                }

                with open(output_file_path, 'w') as merged_file:
                    json.dump(merged_data, merged_file, indent=4)

                print(f"CHScore has been saved to {output_file_path}")
        elif args.eval_type == 150:
            input_dir = os.path.join(args.input_folder, model_name)
            output_file_path = os.path.join(args.output_folder, f"{model_name}_CHScore.json")

            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)
                
            if os.path.exists(output_file_path):
                with open(output_file_path, 'r') as existing_file:
                    all_scores_data = json.load(existing_file).get("all_scores", [])
            else:
                all_scores_data = []
                
            processed_video_names = {list(video_scores.keys())[0] for video_scores in all_scores_data}

            for video_file in tqdm(os.listdir(input_dir), unit='video', leave=False):
                if video_file.endswith('.mp4'):
                    video_path = os.path.join(input_dir, video_file)
                    video_name = video_file.split('.mp4')[0]

                    if video_name in processed_video_names:
                        print(f"Skipping {video_name} as it already exists.")
                        continue

                    _, video = process_video(video_path, args.size)

                    if torch.cuda.is_available():
                        video = video.cuda()

                    scores = get_score(model, video, args.grid_size, args.threshold)
                    all_scores_data.append({video_name: scores})

            total_average_score = sum([list(video_scores.values())[0]['TSI_score'] for video_scores in all_scores_data]) / len(all_scores_data) if all_scores_data else 0

            merged_data = {
                "total_average_score": total_average_score,
                "all_scores": all_scores_data
            }

            with open(output_file_path, 'w') as merged_file:
                json.dump(merged_data, merged_file, indent=4)

if __name__ == "__main__":
    args = parse_args()
    main(args)