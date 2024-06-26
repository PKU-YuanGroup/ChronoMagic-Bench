<h2 align="center"> <a href="https://arxiv.org/abs/2404.05014">ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of 

<a href="https://arxiv.org/abs/2404.05014"> Text-to-Time-lapse Video Generation </a></h2>

<h5 align="center"> If you like our project, please give us a star ⭐ on GitHub for the latest update.  </h2>


<h5 align="center">



[![hf_space](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench)
[![arXiv](https://img.shields.io/badge/Arxiv-2404.05014-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2404.05014) 
[![Home Page](https://img.shields.io/badge/Project-<Website>-blue.svg)](https://pku-yuangroup.github.io/ChronoMagic-Bench/) 
[![Dataset](https://img.shields.io/badge/Dataset-<HuggingFace>-green)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro)
[![Dataset](https://img.shields.io/badge/Dataset-<HuggingFace>-green)](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LICENSE) 
![GitHub Repo stars](https://img.shields.io/github/stars/PKU-YuanGroup/ChronoMagic-Bench)

</h5>

<div align="center">
This repository is the official implementation of ChronoMagic-Bench, a benchmark for metamorphic evaluation of text-to-time-lapse video generation. The key insight is to evaluate the capabilities of Text-to-Video Generation Models in physics, biology, and chemistry by enabling the generation of time-lapse videos, which are characterized by rich physics priors, through a free-form text prompt.
</div>




<br>

<details open><summary>💡 We also have other video generation project that may interest you ✨. </summary><p>
<!--  may -->



> [**Open-Sora-Plan**](https://github.com/PKU-YuanGroup/Open-Sora-Plan) <br>
> PKU-Yuan Lab and Tuzhan AI etc. <br>
> [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)  [![github](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan.svg?style=social)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)  <br>
>
> [**MagicTime**](https://github.com/PKU-YuanGroup/MagicTime) <br>
> Shenghai Yuan, Jinfa Huang and Yujun Shi etc. <br>
> [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/PKU-YuanGroup/MagicTime)  [![github](https://img.shields.io/github/stars/PKU-YuanGroup/MagicTime.svg?style=social)](https://github.com/PKU-YuanGroup/MagicTime)  <br>
> </p></details>


## 📣 News

* ⏳⏳⏳ Evaluate more Text-to-Video Generation Models via *ChronoMagic-Bench*.
* ⏳⏳⏳ Release the code of the "Multi-Aspect Data Preprocessing", which is used to process the dataset. The code is being organized. 
* ⏳⏳⏳ Support evaluating customized videos. The code and instructions are being organized. 
* `[2024.06.28]`  🔥 We released the **ChronoMagic-Pro** and  **ChronoMagic-ProH** datasets. The datasets include **460K** and **150K** time-lapse video-text pairs respectively and can be downloaded at  [HF-Dataset-Pro](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) and [HF-Dataset-ProH](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH).
* `[2024.06.27]`  🔥 We release the **arXiv paper** and **Leaderboard** for *ChronoMagic-Bench*, and you can click [here](https://arxiv.org/abs/2404.05014) to read the paper and [here](https://huggingface.co/spaces/BestWishYsh/ChronoMagic-Bench) to see the leaderboard.
* `[2024.06.26]`  🔥 We release the **testing prompts**, **reference videos** and **generated results** by different models in *ChronoMagic-Bench*, and you can click [here](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Bench) to see more details.
* `[2024.06.25]`  🔥 **All codes & datasets** are coming soon! Stay tuned 👀!

## 😮 Highlights

*ChronoMagic-Bench* can reflect the **physical prior capacity** of Text-to-Video Generation Model.

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

## ⚙️ Requirements and Installation

We recommend the requirements as follows.

### Environment

```bash
git clone https://github.com/PKU-YuanGroup/ChronoMagic-Bench.git
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

## 👍 Acknowledgement

* This project wouldn't be possible without the following open-sourced repositories:
  [CoTracker](https://github.com/facebookresearch/co-tracker), [InternVideo2](https://github.com/OpenGVLab/InternVideo/tree/main/InternVideo2), [UMT](https://github.com/OpenGVLab/unmasked_teacher), [FETV](https://github.com/llyx97/FETV-EVAL), [VBench](https://github.com/Vchitect/VBench), [ShareGPT4Video](https://sharegpt4video.github.io/) and [LAION Aesthetic Predictor](https://github.com/LAION-AI/aesthetic-predictor).


## 🔒 License

* The majority of this project is released under the Apache 2.0 license as found in the [LICENSE](https://github.com/PKU-YuanGroup/ChronoMagic-Bench/blob/main/LICENSE) file.
* The service is a research preview. Please contact us if you find any potential violations.

## ✏️ Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil:.

```BibTeX
@article{yuan2024magictime,
  title={MagicTime: Time-lapse Video Generation Models as Metamorphic Simulators},
  author={Yuan, Shenghai and Huang, Jinfa and Shi, Yujun and Xu, Yongqi and Zhu, Ruijie and Lin, Bin and Cheng, Xinhua and Yuan, Li and Luo, Jiebo},
  journal={arXiv preprint arXiv:2404.05014},
  year={2024}
}
```

## 🤝 Contributors

<a href="https://github.com/PKU-YuanGroup/ChronoMagic-Bench/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PKU-YuanGroup/ChronoMagic-Bench&anon=true" />

</a>

