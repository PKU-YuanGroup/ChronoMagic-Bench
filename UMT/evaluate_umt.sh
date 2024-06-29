current_dir=$(pwd)
export MODEL_NAME="model_1649"
export VIDEO_FOLDER="${current_dir}/toy_video"
export TYPE=1649   # 150 or 1649
export PRETRAINED="UMT-msrvtt-7k.pth"

input_path_step3=results/UMTScore/$TYPE/
output_path_step3=results/UMTScore/$TYPE/
input_path_step4=results/UMTFVD/scores
output_path_step4=results/UMTFVD/temp

bash step0_get_umtfvd_feature.sh
bash step1_get_umtfvd.sh
bash step2_get_umtscope.sh
python step3_get_merge_umt_scores.py --input_path $input_path_step3 --output_path $output_path_step3
python step4_get_merge_umt_fvd.py --input_path $input_path_step4 --output_path $output_path_step4