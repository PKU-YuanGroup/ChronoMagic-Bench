# UMTScore and FVD-UMT
This repo describes how to evaluate a text-to-video (T2V) generation model on the [ChronoMagic-Bench](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) benchmark using [UMTScore](https://github.com/llyx97/FETV-EVAL) and [UMT-FVD](https://github.com/llyx97/FETV-EVAL).

## Prepare Videos for Evaluation
The generated videos should be named corresponding to the prompt ID in ChronoMagic-Bench and placed in the evaluation folder, which is structured as follows. We also provide input examples in the ['toy_video'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/toy_video) . ()

```
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
We provide output examples in the ['results'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/results). You can run the following commands for testing, then modify the parameters in *<u>'xxx.sh'</u>* as needed to suit the text-to-video (T2V) generation model you want to evaluate.

```

```
