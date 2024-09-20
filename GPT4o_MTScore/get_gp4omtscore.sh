openai_api="sk-UybMXXX"
api_base_url="https://XXX"

type="open"  # open or close
model_names=("test_open")  # ("name_1" "name_2")
video_folder="../toy_video"
video_frames_folder="video_frames_folder_temp"
output_dir="results"

python step0-extract_video_frames.py --input_dir $video_folder --output_dir ${output_dir}/GPT4o-MTScores_temp/${video_frames_folder} --model_names "${model_names[@]}" --eval_type $type
python step1-get_temp_results.py --num_workers 8 --openai_api $openai_api --base_url $api_base_url --input_dir ${output_dir}/GPT4o-MTScores_temp/$video_frames_folder --output_dir $output_dir/GPT4o-MTScores_temp/scores_temp --model_names "${model_names[@]}" --eval_type $type
python step2-get_GPT4o-MTScore.py --input_dir ${output_dir}/GPT4o-MTScores_temp/scores_temp --output_dir ${output_dir}/all --model_names "${model_names[@]}" --eval_type $type
python step3-get_merged_GPT4o-MTScore.py --folder_path ${output_dir}/all --output_path $output_dir