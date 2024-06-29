# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
input_folder="../../toy_video/test/1"
output_folder="classify_videos"
model_pth='InternVideo2-stage2_1b-224p-f4.pt'

CUDA_VISIBLE_DEVICES=0 python video_redundancy_elimination.py --input_folder $input_folder --output_folder $output_folder --model_pth $model_pth