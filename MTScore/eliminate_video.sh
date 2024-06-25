# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
model_name="test"
input_folder="../toy_video"
output_folder="classify_videos"
model_pth='InternVideo2-stage2_1b-224p-f4.pt'

python video_redundancy_elimination.py --model_name $model_name --input_folder $input_folder --output_folder $output_folder --model_pth $model_pth