<div align=center>
<img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/images/logo_bench.jpg?raw=true" width="450px">
</div>
<h2 align="center"> <a href="https://arxiv.org/abs/2406.18522">[NeurIPS D&B 2024 Spotlight] ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation </a></h2>

<h5 align="center"> If you like our project, please give us a star ⭐ on GitHub for the latest update.  </h2>


<h5 align="center">


[![hf_space](https://img.shields.io/badge/🤗-LeaderBoard-blue.svg)](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench)
[![hf_space](https://img.shields.io/badge/🤗-Paper%20In%20HF-red.svg)](https://huggingface.co/papers/2406.18522)
[![arXiv](https://img.shields.io/badge/Arxiv-2406.18522-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2406.18522) 
[![Home Page](https://img.shields.io/badge/Project-<Website>-blue.svg)](https://pku-yuangroup.github.io/ChronoMagic-Bench/) 
[![Dataset](https://img.shields.io/badge/Dataset-ChronoMagicPro-green)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro)
[![Dataset](https://img.shields.io/badge/Dataset-ChronoMagicProH-green)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH)
[![Dataset Download](https://img.shields.io/badge/Download-Sampled_Videos-red)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main/Results)
[![zhihu](https://img.shields.io/badge/-Twitter@Adina%20Yakup%20-black?logo=twitter&logoColor=1D9BF0)](https://twitter.com/AdeenaY8/status/1806409038743171191)
[![zhihu](https://img.shields.io/badge/-Twitter@Jinfa%20Huang%20-black?logo=twitter&logoColor=1D9BF0)](https://twitter.com/vhjf36495872/status/1806151450441159024?s=61&t=lLg2j2-sZ9igea_Cj3ToLw)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LICENSE) 
![GitHub Repo stars](https://img.shields.io/github/stars/PKU-YuanGroup/ChronoMagic-Bench)

</h5>

<div align="center">
This repository is the official implementation of ChronoMagic-Bench, a benchmark for metamorphic evaluation of text-to-time-lapse video generation. The key insight is to evaluate the capabilities of Text-to-Video Generation Models in physics, biology, and chemistry by enabling the generation of time-lapse videos, which are characterized by rich physics priors, through a free-form text prompt.
</div>




<br>

<details open><summary>💡 We also have other video generation projects that may interest you ✨. </summary><p>
<!--  may -->



> [**Open-Sora-Plan**](https://github.com/PKU-YuanGroup/Open-Sora-Plan) <br>
> PKU-Yuan Lab and Tuzhan AI etc. <br>
> [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)  [![github](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan.svg?style=social)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)  <br>
>
> [**MagicTime**](https://arxiv.org/abs/2404.05014) <br>
> Shenghai Yuan, Jinfa Huang and Yujun Shi etc. <br>
> [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/PKU-YuanGroup/MagicTime)  [![github](https://img.shields.io/github/stars/PKU-YuanGroup/MagicTime.svg?style=social)](https://github.com/PKU-YuanGroup/MagicTime)  <br>
>
> [**ConsisID**](https://arxiv.org/abs/2411.17440) <br>
> Shenghai Yuan, Jinfa Huang and Xianyi He etc. <br>
> [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/PKU-YuanGroup/ConsisID/)  [![github](https://img.shields.io/github/stars/PKU-YuanGroup/ConsisID.svg?style=social)](https://github.com/PKU-YuanGroup/ConsisID/)  <br>
> </p></details>


## 📣 News

* ⏳⏳⏳ Evaluate more Text-to-Video Generation Models via *ChronoMagic-Bench*.
* `[2024.09.30]`  🔥 We have updated the calculation of the CHScore, making it more robust to temporally coherent disappearance of points. You can click [here](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/CHScore) for detailed implementation.
* `[2024.09.26]`  ✨ Our paper is accepted by **NeurIPS 2024 D&B track** as a **spotlight** present.
* `[2024.08.13]`  🔥 We further evaluate [EasyAnimate-V3](https://github.com/aigc-apps/EasyAnimate) and [CogVideoX-2B](https://github.com/THUDM/CogVideo). The results are available [here](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench).
* `[2024.06.30]`  🔥 We release the code of the **"Multi-Aspect Data Preprocessing"**, which is used to process the *ChronoMagic-Pro* dataset. Please click [here](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/Multi-Aspect_Preprocessing) and [here](https://huggingface.co/papers/2406.18522) to see more details. 
* `[2024.06.29]`  🔥 Support evaluating customized Text-to-Video models. The code and instructions are available in this repo.
* `[2024.06.28]`  🔥 We release the **ChronoMagic-Pro** and  **ChronoMagic-ProH** datasets. The datasets include **460K** and **150K** time-lapse video-text pairs respectively and can be downloaded at  [HF-Dataset-Pro](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) and [HF-Dataset-ProH](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH).
* `[2024.06.27]`  🔥 We release the **arXiv paper** and **Leaderboard** for *ChronoMagic-Bench*, and you can click [here](https://arxiv.org/abs/2406.18522) to read the paper and [here](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench) to see the leaderboard.
* `[2024.06.26]`  🔥 We release the **testing prompts**, **reference videos** and **generated results** by different models in *ChronoMagic-Bench*, and you can click [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench) to see more details.
* `[2024.06.25]`  🔥 **All codes & datasets** are coming soon! Stay tuned 👀!

## 😮 Highlights

*ChronoMagic-Bench* can reflect the **physical prior capacity** of Text-to-Video Generation Model.

#### Resources
* [ChronoMagic-Bench](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main): including 1649 time-lapse video-text pairs. (captioned by GPT-4o)
* [ChronoMagic-Bench-150](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main): including 150 time-lapse video-text pairs. (captioned by GPT-4o)
* [ChronoMagic](https://huggingface.co/datasets/BestWishYsh/ChronoMagic): including 2265 time-lapse video-text pairs. (captioned by GPT-4V)
* [ChronoMagic-Pro](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro): including 460K time-lapse video-text pairs. (captioned by ShareGPT4Video)
* [ChronoMagic-ProH](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH): including 150K time-lapse video-text pairs. (captioned by ShareGPT4Video)

### :mega: Overview

In contrast to existing benchmarks, **ChronoMagic-Bench** emphasizes generating videos with high persistence and strong variation, i.e., metamorphic time-lapse videos with high physical prior content.

<table style="margin-bottom:auto; border: 1px solid #ddd; margin-left: auto; margin-right: auto; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 14px;">
        <thead style="background-color: #f2f2f2;">
            <tr style="border-bottom: 1px solid #ddd;">
                <th style="text-align: center;">Backbone</th>
                <th style="text-align: center;">Type</th>
                <th style="text-align: center;">Visual Quality</th>
                <th style="text-align: center;">Text Relevance</th>
                <th style="text-align: center;">Metamorphic Amplitude</th>
                <th style="text-align: center;">Temporal Coherence</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="text-align: center;"><strong>UCF-101</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">❌</td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="text-align: center;"><strong>Make-a-Video-Eval</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">❌</td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="text-align: center;"><strong>MSR-VTT</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">❌</td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="text-align: center;"><strong>FETV</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">✔️</td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="text-align: center;"><strong>VBench</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">✔️</td>
            </tr>
            <tr style="border-bottom: 2px solid #ddd;">
                <td style="text-align: center;"><strong>T2VScore</strong></td>
                <td style="text-align: center;">General</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">❌</td>
                <td style="text-align: center;">❌</td>
            </tr>
            <tr>
                <td style="text-align: center;"><strong>ChronoMagic-Bench</strong></td>
                <td style="text-align: center;">Time-lapse</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
                <td style="text-align: center;">✔️</td>
            </tr>
        </tbody>
</table>


We specifically design **four major categories** for time-lapse videos *(as shown below)*, including *biological*, *human-created*, *meteorological*, and *physical* videos, and extend these to **75 subcategories**. Based on this, we construct **ChronoMagic-Bench**, comprising 1,649 prompts and their corresponding reference time-lapse videos. 

<table style="width: 100%; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 14px; text-align: center;">
        <thead style="background-color: #f2f2f2; border-bottom: 2px solid #ddd;">
            <tr>
                <th style="padding: 10px;">Biological</th>
                <th style="padding: 10px;">Human Created</th>
                <th style="padding: 10px;">Meteorological</th>
                <th style="padding: 10px;">Physical</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_0_0.gif?raw=true" alt="Biological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_1_0.gif?raw=true" alt="Human Created" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_2_0.gif?raw=true" alt="Meteorological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_3_0.gif?raw=true" alt="Physical" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="padding: 2px 10px;">"Time-lapse of microgreens germinating and growing ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a modern house being constructed in ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a beach sunset capturing the sun's ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of an ice cube melting on a solid ..."</td>
            </tr>
            <tr>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_0_1.gif?raw=true" alt="Biological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_1_1.gif?raw=true" alt="Human Created" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_2_1.gif?raw=true" alt="Meteorological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_3_1.gif?raw=true" alt="Physical" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
            </tr>
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="padding: 2px 10px;">"Time-lapse of microgreens germinating and growing ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a 3D printing process: starting with ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a solar eclipse showing the moon's ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a cake baking in an oven, depicting ..."</td>
            </tr>
            <tr>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_0_2.gif?raw=true" alt="Biological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_1_2.gif?raw=true" alt="Human Created" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_2_2.gif?raw=true" alt="Meteorological" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
                <td><img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/videos/A_3_2.gif?raw=true" alt="Physical" style="width: 235px; height: 235px; padding: 5px 10px;"></td>
            </tr>
            <tr>
                <td style="padding: 2px 10px;">"Time-lapse of a butterfly metamorphosis from ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a busy nighttime city intersection ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a landscape transitioning from a ..."</td>
                <td style="padding: 2px 10px;">"Time-lapse of a strawberry rotting: starting with ..."</td>
            </tr>
        </tbody>
</table>    


### :mortar_board: Evaluation Results

<p align="center">
  <img src="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/ProjectPage/static/images/results_open+close.jpg?raw=true"/>
</p>


We visualize the evaluation results of various <b>open-source</b> and <b>closed-source</b> T2V generation models across ChronoMagic-Bench.

#### :trophy: Leaderboard

See numeric values at our [Leaderboard](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench) :1st_place_medal::2nd_place_medal::3rd_place_medal:

or you can run it locally:

```bash
cd LeadBoard
python app.py
```

## ⚙️ Requirements and Installation

We recommend the requirements as follows.

### Environment

```bash
git clone --depth=1 https://github.com/PKU-YuanGroup/ChronoMagic-Bench.git
cd ChronoMagic-Bench
conda create -n chronomagic python=3.10
conda activate chronomagic

# install base packages
pip install -r requirements.txt

# install flash-attn
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention/csrc/layer_norm && pip install .
cd ../../../
rm -r flash-attention
```

### Download Checkpoints

```bash
huggingface-cli download --repo-type model \
BestWishYsh/ChronoMagic-Bench \
--local-dir BestWishYsh/ChronoMagic-Bench
```

##  :bookmark_tabs: Benchmark Prompts 

We provide *evaluation prompt lists* of *ChronoMagic-Bench* [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main/Captions) or [here](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/prompts). You can use this to sample videos for evaluation of your model. We also provide the *reference videos* for the corresponding evaluation prompts [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main).

## :hammer: Usage

Use *ChronoMagic-Bench* to evaluate videos, and video generative models.

### Prepare Videos for Evaluation

The generated videos should be named corresponding to the prompt ID in ChronoMagic-Bench and placed in the evaluation folder, which is structured as follows. We also provide input examples in the ['toy_video'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/toy_video) . 

```
# for open-source models
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
            
# for close-source models
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

### Get MTScore, CHScore and GPT4o-MTScore

We provide output examples in the ['results'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/results). You can run the following commands for testing, then modify the relevant parameters (such as *<u>model_names</u>*, <u>*input_folder*</u>, <u>*model_pth*</u> and *<u>openai_api</u>*) to suit the text-to-video (T2V) generation model you want to evaluate.

```bash
python evaluate.py \
  --eval_type "open" \
  --model_names test \
  # or more than one model
  # --model_names name1 name2  \
  --input_folder toy_video \
  --output_folder results \
  --video_frames_folder video_frames_folder_temp \
  --model_pth_CHScore cotracker2.pth \
  --model_pth_MTScore InternVideo2-stage2_1b-224p-f4.pt \
  --num_workers 8 \
  --openai_api "sk-UybXXX" \
```

If you only want to evaluate any one of the metrics instead of calculating all of them, you can follow the step below. Before running, please modify the parameters in *<u>'xxx.sh'</u>* as needed. (If you want to obtain the [JSON](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LeadBoard/file/ChronoMagic-Bench-Input.json) to submit to the [leaderboard](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench), you can organize the output files in *MTScore / CHScore / GPT4o-MTScore* according to ['results'](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/results) and then proceed with the following steps.)

```bash
# for MTScore
cd MTScore
bash get_chscore.sh

# for CHScore
cd CHScore
bash get_mtscore.sh

# for GPT4o-MTScore
cd GPT4o_MTScore
bash get_gp4omtscore.sh
```

### Get UMT-FVD and UMTScore

Please refer to the folder [UMT](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/UMT) for how to compute the UMTScore.

### Get File and Submit to Leaderboard

```bash
python get_uploaded_json.py \
  --input_path results/all \
  --output_path results
```

After completing the above steps, you will obtain [ChronoMagic-Bench-Input.json](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LeadBoard/file/ChronoMagic-Bench-Input.json), and then you need to manually fill the [JSON](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LeadBoard/file/ChronoMagic-Bench-Input.json) with UMT-FVD and UMTScore (as we calculate them separately). Finally, you can submit the [JSON](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LeadBoard/file/ChronoMagic-Bench-Input.json) to [HuggingFace](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench).

## :surfer: Sampled Videos

[![Dataset Download](https://img.shields.io/badge/Download-Sampled_Videos-red)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main/Results)

To facilitate future research and to ensure full transparency, we release all the videos we sampled and used for *ChronoMagic-Bench* evaluation. You can download them on [Hugging Face](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench/tree/main/Results). We also provide detailed explanations of the sampled videos and detailed setting for the models under evaluation [here](https://arxiv.org/abs/2406.18522).

## 🐳 ChronoMagicPro Dataset
*ChronoMagic-Pro* with **460K** time-lapse videos, each accompanied by a detailed caption. We also released the **150K** subset (*ChronoMagic-ProH*), which is a higher quality subset. All the dataset can be downloaded at [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) and  [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH), or you can download it with the following command. Some samples can be found on our [Project Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/).

```bash
huggingface-cli download --repo-type dataset \
--resume-download BestWishYsh/ChronoMagic-Pro \  # or BestWishYsh/ChronoMagic-ProH
--local-dir BestWishYsh/ChronoMagic-Pro \  # or BestWishYsh/ChronoMagic-ProH
--local-dir-use-symlinks False
```

Please refer to the folder [Multi-Aspect_Preprocessing](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/tree/main/Multi-Aspect_Preprocessing) for how *ChronoMagic-Pro* to process this data.

## 👍 Acknowledgement

* This project wouldn't be possible without the following open-sourced repositories:
  [CoTracker](https://github.com/facebookresearch/co-tracker), [InternVideo2](https://github.com/OpenGVLab/InternVideo/tree/main/InternVideo2), [UMT](https://github.com/OpenGVLab/unmasked_teacher), [FETV](https://github.com/llyx97/FETV-EVAL), [VBench](https://github.com/Vchitect/VBench), [Panda-70M](https://github.com/snap-research/Panda-70M), [ShareGPT4Video](https://sharegpt4video.github.io/) and [LAION Aesthetic Predictor](https://github.com/LAION-AI/aesthetic-predictor).


## 🔒 License

* The majority of this project is released under the Apache 2.0 license as found in the [LICENSE](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LICENSE) file.
* The service is a research preview. Please contact us if you find any potential violations. (shyuan-cs@hotmail.com)

## ✏️ Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil:.

```BibTeX
@article{yuan2024chronomagic,
  title={ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation},
  author={Yuan, Shenghai and Huang, Jinfa and Xu, Yongqi and Liu, Yaoyang and Zhang, Shaofeng and Shi, Yujun and Zhu, Ruijie and Cheng, Xinhua and Luo, Jiebo and Yuan, Li},
  journal={arXiv preprint arXiv:2406.18522},
  year={2024}
}
```

## 🤝 Contributors

<a href="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PKU-YuanGroup/ChronoMagic-Bench&anon=true" />

</a>

