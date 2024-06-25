__all__ = ['block', 'make_clickable_model', 'make_clickable_user', 'get_submissions']

import gradio as gr
import pandas as pd
import json
import io

from constants import *

global data_component, data_component_150, filter_component

def upload_file(files):
    file_paths = [file.name for file in files]
    return file_paths

def compute_scores(input_data):
    return [None, [
        input_data["Average_MTScore"],
        input_data["Average_CHScore"],
        input_data["Average_GPT4o-MTScore"],
        input_data["Average_UMT-FVD"],
        input_data["Average_UMTScore"]
    ]]

def add_new_eval(
    input_file,
    model_name_textbox: str,
    revision_name_textbox: str,
    backbone_type_dropdown: str,
    model_link: str,
):
    if input_file is None:
        return "Error! Empty file!"
    else:
        input_json = json.load(io.BytesIO(input_file))
        
        if model_name_textbox not in input_json:
            return f"Error! Model '{model_name_textbox}' not found in input file!"
        
        selected_model_data = input_json[model_name_textbox]

        scores = compute_scores(selected_model_data)
        input_data = scores[1]
        input_data = [float(i) for i in input_data]

        csv_data = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH)

        if revision_name_textbox == '':
            col = csv_data.shape[0]
            model_name = model_name_textbox
            name_list = [name.split(']')[0][1:] if name.endswith(')') else name for name in csv_data['Model']]
            assert model_name not in name_list
        else:
            model_name = revision_name_textbox
            model_name_list = csv_data['Model']
            name_list = [name.split(']')[0][1:] if name.endswith(')') else name for name in model_name_list]
            if revision_name_textbox not in name_list:
                col = csv_data.shape[0]
            else:
                col = name_list.index(revision_name_textbox)

        if model_link == '':
            model_name = model_name  # no url
        else:
            model_name = '[' + model_name + '](' + model_link + ')'

        backbone = backbone_type_dropdown

        new_data = [
            model_name,
            backbone,
            input_data[3],
            input_data[4],
            input_data[0],
            input_data[1],
            input_data[2],
        ]
        csv_data.loc[col] = new_data 
        csv_data.to_csv(CSV_DIR_CHRONOMAGIC_BENCH, index=False)
    return "Evaluation successfully submitted!"

def add_new_eval_150(
    input_file,
    model_name_textbox: str,
    revision_name_textbox: str,
    backbone_type_dropdown: str,
    model_link: str,
):
    if input_file is None:
        return "Error! Empty file!"
    else:
        input_json = json.load(io.BytesIO(input_file))
        
        if model_name_textbox not in input_json:
            return f"Error! Model '{model_name_textbox}' not found in input file!"
        
        selected_model_data = input_json[model_name_textbox]

        scores = compute_scores(selected_model_data)
        input_data = scores[1]
        input_data = [float(i) for i in input_data]

        csv_data = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH_150)

        if revision_name_textbox == '':
            col = csv_data.shape[0]
            model_name = model_name_textbox
            name_list = [name.split(']')[0][1:] if name.endswith(')') else name for name in csv_data['Model']]
            assert model_name not in name_list
        else:
            model_name = revision_name_textbox
            model_name_list = csv_data['Model']
            name_list = [name.split(']')[0][1:] if name.endswith(')') else name for name in model_name_list]
            if revision_name_textbox not in name_list:
                col = csv_data.shape[0]
            else:
                col = name_list.index(revision_name_textbox)

        if model_link == '':
            model_name = model_name  # no url
        else:
            model_name = '[' + model_name + '](' + model_link + ')'

        backbone = backbone_type_dropdown

        new_data = [
            model_name,
            backbone,
            input_data[3],
            input_data[4],
            input_data[0],
            input_data[1],
            input_data[2],
        ]
        csv_data.loc[col] = new_data 
        csv_data.to_csv(CSV_DIR_CHRONOMAGIC_BENCH_150, index=False)
    return "Evaluation (150) successfully submitted!"

def get_baseline_df():
    df = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH)
    df = df.sort_values(by="MTScore↑", ascending=False)
    present_columns = MODEL_INFO + checkbox_group.value
    df = df[present_columns]
    return df

def get_baseline_df_150():
    df = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH_150)
    df = df.sort_values(by="MTScore↑", ascending=False)
    present_columns = MODEL_INFO + checkbox_group_150.value
    df = df[present_columns]
    return df

def get_all_df():
    df = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH)
    df = df.sort_values(by="MTScore↑", ascending=False)
    return df

def get_all_df_150():
    df = pd.read_csv(CSV_DIR_CHRONOMAGIC_BENCH_150)
    df = df.sort_values(by="MTScore↑", ascending=False)
    return df

block = gr.Blocks()


with block:
    gr.Markdown(
        LEADERBORAD_INTRODUCTION
    )
    with gr.Tabs(elem_classes="tab-buttons") as tabs:
        # table 1
        with gr.TabItem("🏅 ChronoMagic-Bench", elem_id="ChronoMagic-Bench-tab-table", id=0):
            with gr.Row():
                with gr.Accordion("Citation", open=False):
                    citation_button = gr.Textbox(
                        value=CITATION_BUTTON_TEXT,
                        label=CITATION_BUTTON_LABEL,
                        elem_id="citation-button",
                        show_copy_button=True
                    )
    
            gr.Markdown(
                TABLE_INTRODUCTION
            )

            checkbox_group = gr.CheckboxGroup(
                choices=ALL_RESULTS,
                value=SELECTED_RESULTS,
                label="Select options",
                interactive=True,
            )

            data_component = gr.components.Dataframe(
                value=get_baseline_df, 
                headers=COLUMN_NAMES,
                type="pandas", 
                datatype=DATA_TITILE_TYPE,
                interactive=False,
                visible=True,
                )
    
            def on_checkbox_group_change(selected_columns):
                selected_columns = [item for item in ALL_RESULTS if item in selected_columns]
                present_columns = MODEL_INFO + selected_columns
                updated_data = get_all_df()[present_columns]
                updated_data = updated_data.sort_values(by=present_columns[1], ascending=False)
                updated_headers = present_columns
                update_datatype = [DATA_TITILE_TYPE[COLUMN_NAMES.index(x)] for x in updated_headers]

                filter_component = gr.components.Dataframe(
                    value=updated_data, 
                    headers=updated_headers,
                    type="pandas", 
                    datatype=update_datatype,
                    interactive=False,
                    visible=True,
                    )
        
                return filter_component

            checkbox_group.change(fn=on_checkbox_group_change, inputs=checkbox_group, outputs=data_component)

        # table 2
        with gr.TabItem("🏅 ChronoMagic-Bench-150", elem_id="ChronoMagic-Bench-150-tab-table", id=1):
            with gr.Row():
                with gr.Accordion("Citation", open=False):
                    citation_button = gr.Textbox(
                        value=CITATION_BUTTON_TEXT,
                        label=CITATION_BUTTON_LABEL,
                        elem_id="citation-button",
                        show_copy_button=True
                    )
    
            gr.Markdown(
                TABLE_INTRODUCTION
            )

            checkbox_group_150 = gr.CheckboxGroup(
                choices=ALL_RESULTS,
                value=SELECTED_RESULTS_150,
                label="Select options",
                interactive=True,
            )

            data_component_150 = gr.components.Dataframe(
                value=get_baseline_df_150, 
                headers=COLUMN_NAMES,
                type="pandas", 
                datatype=DATA_TITILE_TYPE,
                interactive=False,
                visible=True,
                )
    
            def on_checkbox_group_150_change(selected_columns):
                selected_columns = [item for item in ALL_RESULTS if item in selected_columns]
                present_columns = MODEL_INFO + selected_columns
                updated_data = get_all_df_150()[present_columns]
                updated_data = updated_data.sort_values(by=present_columns[1], ascending=False)
                updated_headers = present_columns
                update_datatype = [DATA_TITILE_TYPE[COLUMN_NAMES.index(x)] for x in updated_headers]

                filter_component = gr.components.Dataframe(
                    value=updated_data, 
                    headers=updated_headers,
                    type="pandas", 
                    datatype=update_datatype,
                    interactive=False,
                    visible=True,
                    )
        
                return filter_component

            checkbox_group_150.change(fn=on_checkbox_group_150_change, inputs=checkbox_group_150, outputs=data_component_150)

        # table 3 
        with gr.TabItem("🚀 Submit here! ", elem_id="seed-benchmark-tab-table", id=2):
            with gr.Row():
                gr.Markdown(SUBMIT_INTRODUCTION, elem_classes="markdown-text")

            with gr.Row():
                gr.Markdown("# ✉️✨ Submit your model evaluation json file here!", elem_classes="markdown-text")

            with gr.Row():
                with gr.Column():
                    model_name_textbox = gr.Textbox(
                        label="Model name", placeholder="MagicTime"
                        )
                    revision_name_textbox = gr.Textbox(
                        label="Revision Model Name", placeholder="MagicTime"
                    )
                    backbone_type_dropdown = gr.Dropdown(
                        label="Backbone Type",
                        choices=["DiT", "U-Net"],
                        value="DiT"
                    )
                    model_link = gr.Textbox(
                        label="Model Link", placeholder="https://github.com/PKU-YuanGroup/MagicTime"
                    )

            with gr.Column():
                input_file = gr.File(label="Click to Upload a json File", type='binary')
                submit_button = gr.Button("Submit Eval (ChronoMagic-Bench)")
                submit_button_150 = gr.Button("Submit Eval (ChronoMagic-Bench-150)")

                submission_result = gr.Markdown()
                submit_button.click(
                    add_new_eval,
                    inputs=[
                        input_file,
                        model_name_textbox,
                        revision_name_textbox,
                        backbone_type_dropdown,
                        model_link,
                    ],
                    outputs=submission_result,
                )
                submit_button_150.click(
                    add_new_eval_150,
                    inputs=[
                        input_file,
                        model_name_textbox,
                        revision_name_textbox,
                        backbone_type_dropdown,
                        model_link,
                    ],
                    outputs = submission_result,
                )

    with gr.Row():
        data_run = gr.Button("Refresh")
        data_run.click(
            get_baseline_df, outputs=data_component
        )
        data_run.click(
            get_baseline_df_150, outputs=data_component_150
        )
        
block.launch()