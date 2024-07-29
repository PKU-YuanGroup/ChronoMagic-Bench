import argparse
import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed with error: {result.stderr}")
    else:
        print(result.stdout)

def main():
    parser = argparse.ArgumentParser(description="Run video processing pipeline.")
    parser.add_argument('--model_names', nargs='+', default=["test"], help="Name of the models.")
    parser.add_argument('--input_folder', type=str, default="toy_video", help='Path to the input folder containing videos')
    parser.add_argument('--output_folder', type=str, default="results", help='Path to the output folder')
    parser.add_argument('--video_frames_folder', type=str, default="video_frames_folder_temp", help='Path to the temporary folder for video frames')
    parser.add_argument('--model_pth_CHScore', type=str, default='cotracker2.pth', help='Path to the model checkpoint')
    parser.add_argument('--model_pth_MTScore', type=str, default='InternVideo2-stage2_1b-224p-f4.pt', help='Path to the new model checkpoint')
    parser.add_argument('--num_workers', type=int, default=8, help='Number of workers to use')
    parser.add_argument('--hf_endpoint', type=str, default='https://hf-mirror.com', help='HF Endpoint')
    parser.add_argument('--openai_api', type=str, default="sk-UybXXX", help='OpenAI API key')
    parser.add_argument('--api_base_url', type=str, default=None, help='API base URL')  # "https://XXX"

    args = parser.parse_args()

    # If you can't connect to huggingface.co, add this line of code (hf-mirror)
    # os.environ['HF_ENDPOINT'] = args.hf_endpoint

    os.environ['openai_api'] = args.openai_api
    os.environ['api_base_url'] = args.api_base_url

    current_path = os.getcwd()
    args.input_folder = os.path.join(current_path, args.input_folder)
    args.output_folder = os.path.join(current_path, args.output_folder)

    # Calculate CHScore
    run_command(f"python CHScore/step0-get_CHScore.py --model_names {' '.join(args.model_names)} --input_folder {args.input_folder} --output_folder {args.output_folder}/all --model_pth {args.model_pth_CHScore}")

    # Calculate GPT4o-MTScore
    os.chdir('MTScore')
    run_command(f"python GPT4o_MTScore/step0-extract_video_frames.py --input_dir {args.input_folder} --output_dir {args.output_folder}/GPT4o-MTScores_temp/{args.video_frames_folder} --model_names {' '.join(args.model_names)}")
    run_command(f"python GPT4o_MTScore/step1-get_temp_results.py --num_workers {args.num_workers} --openai_api {args.openai_api} --base_url {args.api_base_url} --input_dir {args.output_folder}/GPT4o-MTScores_temp/{args.video_frames_folder} --output_dir {args.output_folder}/GPT4o-MTScores_temp/scores_temp --model_names {' '.join(args.model_names)}")
    run_command(f"python GPT4o_MTScore/step2-get_GPT4o-MTScore.py --input_dir {args.output_folder}/GPT4o-MTScores_temp/scores_temp --output_dir {args.output_folder}/all --model_names {' '.join(args.model_names)}")
    os.chdir(current_path)
    
    # Calculate MTScore
    run_command(f"python MTScore/step0-get_MTScore.py --model_names {' '.join(args.model_names)} --input_folder {args.input_folder} --output_folder {args.output_folder}/all --model_pth {args.model_pth_MTScore}")

    # # get uploaded json
    run_command(f"python get_uploaded_json.py --input_path {args.output_folder}/all --output_path {args.output_folder}")

if __name__ == "__main__":
    main()
