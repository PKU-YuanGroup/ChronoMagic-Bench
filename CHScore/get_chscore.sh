# If you can't connect to huggingface.co, add this line of code (hf-mirror)
# export HF_ENDPOINT=https://hf-mirror.com
type="open"  # open or close
model_names=("test_open")  # ("name_1" "name_2")
input_folder="../toy_video"
output_folder="results"
model_pth="cotracker2.pth"

python step0-get_CHScore.py --model_names "${model_names[@]}" --input_folder $input_folder --output_folder ${output_folder}/all --model_pth $model_pth --eval_type $type
python step1-get_merged_CHScore.py --folder_path ${output_folder}/all --output_path $output_folder