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

    input_dir = os.path.dirname(args.video_list)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        
    f = open(args.video_list, "r")
    video_paths = f.read().splitlines()
    f.close()

    f = open(args.event_timecode, "r")
    video_timecodes = json.load(f)
    f.close()

    os.makedirs(args.output_folder, exist_ok=True)

    fail_path = "temp/failed_splitting.txt"
    fail_dir = os.path.dirname(fail_path)
    if not os.path.exists(fail_dir):
        os.makedirs(fail_dir)
    if not os.path.exists(fail_path):
        with open(fail_path, 'w') as f:
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
                start_time = datetime.strptime(timecode[0], '%H:%M:%S.%f')
                end_time = datetime.strptime(timecode[1], '%H:%M:%S.%f')
                video_duration = (end_time - start_time).total_seconds()
                os.system("ffmpeg -hide_banner -loglevel panic -ss %s -t %.3f -i %s %s"%(timecode[0], video_duration, video_path, os.path.join(args.output_folder, video_name+".%i.mp4"%i)))
        else:
            with file_lock:
                print(f"Failed to detect cutscenes in video: {video_path}, Error: {e}")
                with open(fail_path, 'a') as f:
                    f.write(f"{video_path}\n")
