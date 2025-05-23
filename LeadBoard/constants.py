MODEL_INFO = ["Model", "Backbone"]

ALL_RESULTS = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "CHScore↑", "GPT4o-MTScore↑"]

SELECTED_RESULTS = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "CHScore↑", "GPT4o-MTScore↑"]
SELECTED_RESULTS_150 = ["UMT-FVD↓", "UMTScore↑", "MTScore↑", "CHScore↑", "GPT4o-MTScore↑"]

DATA_TITILE_TYPE = ["markdown", 'markdown', "number", "number", "number", "number", "number"]

CSV_DIR_CHRONOMAGIC_BENCH = "./file/results_ChronoMagic-Bench.csv"
CSV_DIR_CHRONOMAGIC_BENCH_150 = "./file/results_ChronoMagic-Bench-150.csv"

COLUMN_NAMES = MODEL_INFO + ALL_RESULTS

LEADERBORAD_INTRODUCTION = """
    <div style='display: flex; align-items: center; justify-content: center; text-align: center;'>
        <img src='https://www.pnglog.com/MqiNJ0.jpg' style='width: 600px; height: auto; margin-right: 10px;' />
    </div>

    # ChronoMagic-Bench Leaderboard
    
    Welcome to the leaderboard of the ChronoMagic-Bench! (**NeurIPS 2024 D&B Spotlight**)
     
    🏆ChronoMagic-Bench represents the inaugural benchmark dedicated to assessing T2V models' capabilities in generating time-lapse videos that demonstrate significant metamorphic amplitude and temporal coherence. The benchmark probes T2V models for their physics, biology, and chemistry capabilities, in a free-form text control.
    
    If you like our project, please give us a star ⭐ on GitHub for the latest update.

    [GitHub](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [arXiv](https://arxiv.org/abs/2406.18522) | [Home Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) | [ChronoMagic-Pro](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-Pro) | [ChronoMagic-ProH](https://huggingface.co/datasets/BestWishYsh/ChronoMagic-ProH)
"""

SUBMIT_INTRODUCTION = """# Submission Guidelines
    1. Fill in *'Model Name'* if it is your first time to submit your result **or** Fill in *'Revision Model Name'* if you want to update your result.
    2. Select *‘Backbone Type’* (DiT or U-Net).
    3. Fill in your home page to *'Model Link'*.
    4. After evaluation, follow the guidance in the [github repository](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) to obtain `ChronoMagic-Bench-Input.json` and upload it here.
    5. Click the 'Submit Eval' button.
    6. Click 'Refresh' to obtain the uploaded leaderboard.
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
