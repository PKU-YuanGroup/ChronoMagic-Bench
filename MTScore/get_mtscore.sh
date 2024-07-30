# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
type=150  # 150 or 1649
model_names=("test_150")  #("test_1649" "test_1649")
input_folder="../toy_video"
output_folder="results"
model_pth='InternVideo2-stage2_1b-224p-f4.pt'

python step0-get_MTScore.py --model_name "${model_names[@]}" --input_folder $input_folder --output_folder ${output_folder}/all --model_pth $model_pth --eval_type $type
python step1-get_merged_MTScore.py --folder_path ${output_folder}/all --output_path $output_folder