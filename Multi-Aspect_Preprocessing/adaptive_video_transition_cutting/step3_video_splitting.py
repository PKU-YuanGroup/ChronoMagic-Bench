import os
import json
import argparse
from datetime import datetime
import subprocess
from tqdm import tqdm
from threading import Lock

file_lock = Lock()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Event Stitching")
    parser.add_argument("--video-list", type=str, required=True)
    parser.add_argument("--event-timecode", type=str, required=True)
    parser.add_argument("--output-folder", type=str, default="outputs")
    args = parser.parse_args()

    f = open(args.video_list, "r")
    video_paths = f.read().splitlines()
    f.close()

    f = open(args.event_timecode, "r")
    video_timecodes = json.load(f)
    f.close()

    os.makedirs(args.output_folder, exist_ok=True)

    miss_path = "miss_splitting.txt"
    if not os.path.exists(miss_path):
        with open(miss_path, 'w') as f:
            f.write('')

    for video_path in tqdm(video_paths):
        video_name = video_path.split("/")[-1].split('.')[0]
        if video_path.split("/")[-1] in video_timecodes:
            timecodes = video_timecodes[video_path.split("/")[-1]]
            for i, timecode in enumerate(timecodes): 
                output_file = os.path.join(args.output_folder, f"{video_name}.{i}.mp4")
                if os.path.exists(output_file):
                    print(f"{output_file} has been processed, skipping.")
                    continue

                with file_lock:
                    print(f"FMissing to video_splitting: {video_path}")
                    with open(miss_path, 'a') as f:
                        f.write(f"{video_path}\n")
        else:
            with file_lock:
                print(f"Missing timecodes for video: {video_path}")
                with open(miss_path, 'a') as f:
                    f.write(f"{video_path}\n")
