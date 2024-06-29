import os
import re
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate and save average UMT scores.")
    parser.add_argument("--input_path", type=str, default="results/UMTScore", help="The base path to the UMTScore directories.")
    parser.add_argument("--output_path", type=str, default="results/UMTScore", help="The output JSON file path.")
    return parser.parse_args()

def extract_score(score_str):
    match = re.search(r"UMTScore': (-?\d+\.\d+)", score_str)
    if match:
        return float(match.group(1))
    return None

def calculate_average_scores(input_path):
    model_data = {}
    
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file == 'scores.txt':
                full_path = os.path.join(root, file)
                with open(full_path, 'r') as f:
                    content = f.read()
                    score = extract_score(content)
                    if score is not None:
                        parts = root.split(os.sep)
                        model_name = parts[-2]
                        version = parts[-1]
                        
                        if model_name not in model_data:
                            model_data[model_name] = {}
                        
                        if version not in model_data[model_name]:
                            model_data[model_name][version] = {'total': 0, 'count': 0}
                        
                        model_data[model_name][version]['total'] += score
                        model_data[model_name][version]['count'] += 1
    
    averages = {model: {} for model in model_data}
    for model, versions in model_data.items():
        for version, data in versions.items():
            if data['count'] > 0:
                average_score = data['total'] / data['count']
                averages[model][version] = average_score
    
    return averages

def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main(input_path, output_path):
    average_scores = calculate_average_scores(input_path)

    for key, value in average_scores.items():
        prefix_scores = {}
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if sub_key.split("_")[0] == sub_key:
                    prefix = sub_key
                else:
                    prefix = "_".join(sub_key.split("_")[:-1])
                if prefix not in prefix_scores:
                    prefix_scores[prefix] = []
                prefix_scores[prefix].append(sub_value)

                average_scores = {prefix: sum(scores) / len(scores) for prefix, scores in prefix_scores.items()}

                output = {
                    "UMTScore": average_scores
                }
                
            output_cur = os.path.join(output_path, f"merge_umtscore_{key}.json")
            print(json.dumps(output, indent=4))
            save_to_json(output, output_cur)

if __name__ == "__main__":
    args = parse_args()
    main(args.input_path, args.output_path)