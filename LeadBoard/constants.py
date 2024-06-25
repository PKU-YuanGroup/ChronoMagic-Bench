MODEL_INFO = ["Model", "Backbone"]

ALL_RESULTS = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "CHScore↑", "GPT4o-MTScore↑"]

SELECTED_RESULTS = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "CHScore↑", "GPT4o-MTScore↑"]
SELECTED_RESULTS_150 = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "GPT4o-MTScore↑"]

DATA_TITILE_TYPE = ["markdown", 'markdown', "number", "number", "number", "number", "number"]

CSV_DIR_CHRONOMAGIC_BENCH = "./file/results_ChronoMagic-Bench.csv"
CSV_DIR_CHRONOMAGIC_BENCH_150 = "./file/results_ChronoMagic-Bench-150.csv"

COLUMN_NAMES = MODEL_INFO + ALL_RESULTS

LEADERBORAD_INTRODUCTION = """# ChronoMagic-Bench Leaderboard
    
    Welcome to the leaderboard of the ChronoMagic-Bench! 
     
    🏆ChronoMagic-Bench represents the inaugural benchmark dedicated to assessing T2V models' capabilities in generating time-lapse videos that demonstrate significant metamorphic amplitude and temporal coherence. The benchmark probes T2V models for their physics, biology, and chemistry capabilities, in a free-form text control.
    
    If you like our project, please give us a star ⭐ on GitHub for the latest update.

    [GitHub](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [arXiv](https://arxiv.org/abs/2404.05014) | [Home Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) | [ChronoMagic-Pro](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) | [ChronoMagic-ProH](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH)
"""

SUBMIT_INTRODUCTION = """# Submit Introduction
    Obtain `ChronoMagic-Bench-Input.json` from our [github repository](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) after evaluation.


    ## Submit Example
    For example, if you want to upload Video-ChatGPT's result in the leaderboard, you need to:
    1. Fill in 'MagicTime' in 'Model Name' if it is your first time to submit your result (You can leave 'Revision Model Name' blank).
    2. Fill in 'MagicTime' in 'Revision Model Name' if you want to update your result (You can leave 'Model Name' blank).
    3. Select ‘Backbone Type’ (DiT or U-Net).
    4. Fill in 'https://github.com/x/x' in 'Model Link'.
    5. Upload `ChronoMagic-Bench-Input.json`.
    6. Click the 'Submit Eval' button.
    7. Click 'Refresh' to obtain the uploaded leaderboard.
"""

TABLE_INTRODUCTION = """In the table below, we summarize each task performance of all the models.
        We use UMT-FVD, UMTScore, MTScore, CHScore, GPT4o-MTScore as the primary evaluation metric for each tasks.
    """

CITATION_BUTTON_LABEL = "Copy the following snippet to cite these results"
CITATION_BUTTON_TEXT = r"""@article{yuan2024magictime,
  title={MagicTime: Time-lapse Video Generation Models as Metamorphic Simulators},
  author={Yuan, Shenghai and Huang, Jinfa and Shi, Yujun and Xu, Yongqi and Zhu, Ruijie and Lin, Bin and Cheng, Xinhua and Yuan, Li and Luo, Jiebo},
  journal={arXiv preprint arXiv:2404.05014},
  year={2024}
}"""
