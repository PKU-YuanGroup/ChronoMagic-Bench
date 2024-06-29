# UMTScore and FVD-UMT
This repo describes how to evaluate a text-to-video (T2V) generation model on the [ChronoMagic-Bench](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) benchmark using [UMTScore](https://github.com/llyx97/FETV-EVAL) and [UMT-FVD](https://github.com/llyx97/FETV-EVAL).

## Prepare Videos for Evaluation
The generated videos should be named corresponding to the prompt ID in ChronoMagic-Bench and placed in the evaluation folder, which is structured as follows. We also provide input examples in the ['UMT/toy_video'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/UMT/toy_video) .

```bash
# for ChronoMagic-Bench
`-- input_video_folder
    `-- model_name_a
        |-- 1
        |   |-- 3d_printing_08.mp4
        |   `-- ...
        |-- 2
        |   |-- 3d_printing_08.mp4
        |   `-- ...
        `-- 3
            |-- 3d_printing_08.mp4
            `-- ...
    `-- model_name_b
        |-- 1
        |   |-- 3d_printing_08.mp4
        |   `-- ...
        |-- 2
        |   |-- 3d_printing_08.mp4
        |   `-- ...
        `-- 3
            |-- 3d_printing_08.mp4
            `-- ...
            
# for ChronoMagic-Bench-150
-- input_video_folder
    |-- model_name_a
    |   |-- 3d_printing_08.mp4
    |   `-- animal_04.mp4
    |   `-- ...
    |-- model_name_b
    |   |-- 3d_printing_08.mp4
    |   `-- ...
    `-- ...
```

The filenames of all videos to be evaluated should be "<u>videoid</u>.mp4". For example, if the <u>videoid</u> is 3d_printing_08, the video filename should be "3d_printing_08.mp4". If this naming convention is not followed, the text relevance cannot be evaluated.

## Usage
We provide output examples in the ['UMT/results'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/UMT/results). You can run the following commands for testing, then modify the parameters in *<u>'xxx.sh'</u>* as needed to suit the text-to-video (T2V) generation model you want to evaluate (normally, you only need to modify *<u>MODEL_NAME</u>*, <u>*VIDEO_FOLDER*</u>, *<u>TYPE</u>* and *<u>PRETRAINED</u>*).

```bash
bash evaluate_umt.sh
```

If you only want to evaluate any one of the metrics instead of calculating all of them, you can follow the step below.

```bash
current_dir=$(pwd)
export MODEL_NAME="model_1649"
export VIDEO_FOLDER="${current_dir}/toy_video"
export TYPE=1649   # 150 or 1649
export PRETRAINED="UMT-msrvtt-7k.pth"
input_path_step3=results/UMTScore/$TYPE/
output_path_step3=results/UMTScore/$TYPE/
input_path_step4=results/UMTFVD/scores
output_path_step4=results/UMTFVD/temp

# for UMT-FVD
bash step0_get_umtfvd_feature.sh
bash step1_get_umtfvd.sh
python step4_get_merge_umt_fvd.py --input_path $input_path_step4 --output_path $output_path_step4

# for UMTScore
bash step2_get_umtscope.sh
python step3_get_merge_umt_scores.py --input_path $input_path_step3 --output_path $output_path_step3
```

and then you will get the results —— [*merge_umtfvd_150.json*](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/UMT/results/UMTFVD/scores/merge_umtfvd_150.json), [*merge_umtfvd_1649.json*](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/UMT/results/UMTFVD/scores/merge_umtfvd_1649.json) and [*merge_umtscore_150.json*](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/UMT/results/UMTScore/150/merge_umtscore_150.json)
