import os
import argparse

def save_file_paths(directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp4"):
                    path = os.path.abspath(os.path.join(root, file))
                    f.write("%s\n" % path)

def main():
    parser = argparse.ArgumentParser(description="Save file paths of .mp4 files in a directory to an output file.")
    parser.add_argument('--input_path', type=str, help="The directory to search for .mp4 files.")
    parser.add_argument('--output_file', type=str, help="The file to save the list of .mp4 file paths.")
    
    args = parser.parse_args()
    
    output_dir = os.path.dirname(args.output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    save_file_paths(args.input_path, args.output_file)

if __name__ == '__main__':
    main()
