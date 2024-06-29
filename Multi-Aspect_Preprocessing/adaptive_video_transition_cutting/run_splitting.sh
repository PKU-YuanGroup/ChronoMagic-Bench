# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
DEVICE_ID=1
VIDEO_FOLDER="../../toy_video/test/1"
VIDEO_LIST="temp/step0_video_list.txt"
JSON_FILE="temp/step1_cutscene_frameidx.json"
JSON_FILE_2="temp/step2_event_timecode.json"
OUTPUT_PATH="step3_output_video_folder"

CUDA_VISIBLE_DEVICES=$DEVICE_ID python step0_get_file_list.py --input_path $VIDEO_FOLDER --output_file $VIDEO_LIST
CUDA_VISIBLE_DEVICES=$DEVICE_ID python step1_cutscene_detect.py --video-list $VIDEO_LIST --output-json-file $JSON_FILE
CUDA_VISIBLE_DEVICES=$DEVICE_ID python step2_event_stitching.py --video-list $VIDEO_LIST --cutscene-frameidx $JSON_FILE --output-json-file $JSON_FILE_2
CUDA_VISIBLE_DEVICES=$DEVICE_ID python step3_video_splitting.py --video-list $VIDEO_LIST --event-timecode $JSON_FILE_2 --output-folder $OUTPUT_PATH