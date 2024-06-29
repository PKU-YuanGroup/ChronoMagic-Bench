# <u>Multi-Aspect Data Preprocessing</u> by *ChronoMagic-Pro*
This repo describes how to preprocess [*ChronoMagic-Pro/ProH*](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) datasets on the [ChronoMagic-Bench](https://arxiv.org/abs/2406.18522) paper.

## Adaptive Video Transition Cutting
In stage one: since our training data is sourced from video platforms (e.g., YouTube) where videos are designed to engage the audience, they inherently contain many transitions (significant changes in content during video playback). To address this issue, we follow the method described in [Panda70M](https://github.com/snap-research/Panda-70M) to split the videos into multiple <u>semantically consistent single-scene clips</u>. 

#### Usage

You should first modify the parameters in *<u>'xxx.sh'</u>* as needed to suit the text-to-video (T2V) generation model you want to evaluate (normally, you only need to modify *<u>VIDEO_FOLDER</u>*, *<u>OUTPUT_PATH</u>*), and then run the following commands.

```bash
apt install ffmpeg
cd adaptive_video_transition_cutting
bash run_splitting.sh
```

## Video Redundancy Elimination
In stage two: video publishers often use eye-catching titles, descriptions, or hashtags to attract traffic. As a result, time-lapse videos found through search terms may be general videos. Manually screening large-scale videos is impractical, we construct a zero-shot metamorphic-general classification strategy based on the [Video Retrieval Model](https://github.com/OpenGVLab/InternVideo/tree/main/InternVideo2). After that, we obtain <u>video clips with higher purity and quality</u>.

#### Usage

You should first modify the parameters in *<u>'xxx.sh'</u>* as needed to suit the text-to-video (T2V) generation model you want to evaluate (normally, you only need to modify *<u>input_folder</u>*, *model_pth*), and then run the following commands.

```bash
cd video_redundancy_elimination
bash run_eliminate_video.sh
```
