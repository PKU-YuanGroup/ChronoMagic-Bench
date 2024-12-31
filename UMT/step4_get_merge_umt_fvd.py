import os
import json
import argparse
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate and save average FVD values for models.")
    parser.add_argument("--input_path", type=str, default="results/UMTFVD/scores", help="The root directory containing model results.")
    parser.add_argument("--output_path", type=str, default="results/UMTFVD/temp", help="The directory to save the output JSON files.")
    parser.add_argument("--metrics", nargs='+', default=[
        'fvd32_16f', 'fvd64_16f', 'fvd128_16f', 'fvd256_16f', 'fvd300_16f', 'fvd512_16f', 'fvd1024_16f'
    ], help="List of metrics to process (default: all metrics).")
    return parser.parse_args()

def get_fvd_values_from_jsonl(jsonl_path, metric):
    fvd_values = []
    with open(jsonl_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            if metric in data['results']:
                fvd_values.append(data['results'][metric])
    return fvd_values

def get_model_fvd_values(root_dir, metric):
    model_fvd_values = defaultdict(list)
    for model_dir in os.listdir(root_dir):
        model_prefix = model_dir.split('-t2v')[0]
        model_path = os.path.join(root_dir, model_dir)
        if os.path.isdir(model_path):
            for subdir in os.listdir(model_path):
                subdir_path = os.path.join(model_path, subdir)
                if os.path.isdir(subdir_path):
                    jsonl_file = os.path.join(subdir_path, f'metric-{metric}.jsonl')
                    if os.path.isfile(jsonl_file):
                        model_fvd_values[model_prefix].extend(get_fvd_values_from_jsonl(jsonl_file, metric))
    return model_fvd_values

def calculate_average_fvd_for_models(root_dir, metric):
    model_fvd_values = get_model_fvd_values(root_dir, metric)
    model_average_fvd = {}
    for model, values in model_fvd_values.items():
        if values:
            average_fvd = sum(values) / len(values)
            model_average_fvd[model] = average_fvd
        else:
            model_average_fvd[model] = None
    return model_average_fvd

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    args = parse_args()

    for eval_type in ["close", "open"]:
        new_input_path = os.path.join(args.input_path, eval_type)
        if not os.path.exists(new_input_path):
            continue
        new_output_path = os.path.join(args.output_path, eval_type)
        os.makedirs(new_output_path, exist_ok=True)

        all_averages = {}
        
        for metric in args.metrics:
            output_file = os.path.join(new_output_path, f'umt_{metric}.json')
            average_fvd_per_model = calculate_average_fvd_for_models(new_input_path, metric)
            save_results_to_json(average_fvd_per_model, output_file)
            print(f'Results saved to {output_file}')
            for model, avg_fvd in average_fvd_per_model.items():
                if model not in all_averages:
                    all_averages[model] = []
                if avg_fvd is not None:
                    all_averages[model].append(avg_fvd)

        merged_averages = {model: sum(values) / len(values) for model, values in all_averages.items() if values}
        
        if eval_type == "open":
            prefix_scores = {}
            for key, value in merged_averages.items(): 
                prefix = "_".join(key.split("_")[:-1])
                if prefix not in prefix_scores:
                    prefix_scores[prefix] = []
                prefix_scores[prefix].append(value)
            all_averages = prefix_scores
            merged_averages = {model: sum(values) / len(values) for model, values in all_averages.items() if values}

        merge_output_file = os.path.join(args.input_path, f'merge_umtfvd_{eval_type}.json')
        save_results_to_json(merged_averages, merge_output_file)
        print(f'Merged results saved to {merge_output_file}')

if __name__ == "__main__":
    main()