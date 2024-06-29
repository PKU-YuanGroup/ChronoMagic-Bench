# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
current_dir=$(pwd)
# export MODEL_NAME="model_150"
# export VIDEO_FOLDER="${current_dir}/toy_video"
# export TYPE=150   # 150 or 1649
export OUTPUT_DIR="${current_dir}/results/UMTFVD/feature"
# export PRETRAINED="UMT-msrvtt-7k.pth"

cd main
bash get_umt_fvd_feature.sh