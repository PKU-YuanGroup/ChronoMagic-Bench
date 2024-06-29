from scenedetect import detect, ContentDetector
from tqdm import tqdm
import cv2
import os, re, json, argparse
from tqdm import tqdm

from threading import Lock

file_lock = Lock()

def cutscene_detection(video_path, cutscene_threshold=27, max_cutscene_len=10):
    scene_list = detect(video_path, ContentDetector(threshold=cutscene_threshold, min_scene_len=15), start_in_scene=True)
    end_frame_idx = [0]

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    for scene in scene_list:
        new_end_frame_idx = scene[1].get_frames()
        while (new_end_frame_idx-end_frame_idx[-1]) > (max_cutscene_len+2)*fps: # if no cutscene at min_scene_len+2, then cut at min_scene_len
            end_frame_idx.append(end_frame_idx[-1] + int(max_cutscene_len*fps))
        end_frame_idx.append(new_end_frame_idx)
    
    cutscenes =[]
    for i in range(len(end_frame_idx)-1):
        cutscenes.append([end_frame_idx[i], end_frame_idx[i+1]])

    return cutscenes


def write_json_file(data, output_file):
    data = json.dumps(data, indent = 4)
    def repl_func(match: re.Match):
        return " ".join(match.group().split())
    data = re.sub(r"(?<=\[)[^\[\]]+(?=])", repl_func, data)
    data = re.sub(r'\[\s+', '[', data)
    data = re.sub(r'],\s+\[', '], [', data)
    data = re.sub(r'\s+\]', ']', data)
    with open(output_file, "w") as f:
        f.write(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cutscene Detection")
    parser.add_argument("--video-list", type=str, required=True)
    parser.add_argument("--output-json-file", type=str, default="cutscene_frame_idx.json")
    args = parser.parse_args()

    input_dir = os.path.dirname(args.video_list)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    f = open(args.video_list, "r")
    video_paths = f.read().splitlines()
    
    video_cutscenes = {}
    if os.path.exists(args.output_json_file):
        with open(args.output_json_file, "r") as f:
            video_cutscenes = json.load(f)
            
    fail_path = "temp/failed_cutscene.txt"
    fail_dir = os.path.dirname(fail_path)
    if not os.path.exists(fail_dir):
        os.makedirs(fail_dir)
    if not os.path.exists(fail_path):
        with open(fail_path, 'w') as f:
            f.write('')

    for video_path in tqdm(video_paths):
        video_name = video_path.split("/")[-1]
        if video_name in video_cutscenes:
            print(f"Skipping already processed video: {video_name}")
            continue

        try:
            cutscenes_raw = cutscene_detection(video_path, cutscene_threshold=25, max_cutscene_len=5)
            video_cutscenes[video_path.split("/")[-1]] = cutscenes_raw
            write_json_file(video_cutscenes, args.output_json_file)
        except Exception as e:
            print(f"Failed to detect cutscenes in video: {video_path}, Error: {e}")
            with file_lock:
                with open(fail_path, 'a') as f:
                    f.write(f"{video_path}\n")