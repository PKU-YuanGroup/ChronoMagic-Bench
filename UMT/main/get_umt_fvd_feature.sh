export MASTER_PORT=$((12000 + $RANDOM % 20000))
export OMP_NUM_THREADS=1
which_python=$(which python)
export PYTHONPATH=${PYTHONPATH}:${which_python}
export PYTHONPATH=${PYTHONPATH}:.

PARTITION='video'
NNODE=1
NUM_GPUS=1
NUM_CPU=64


if [[ ${TYPE} == 150 ]]; then
    TEMP_OUTPUT_DIR="$OUTPUT_DIR/150/$MODEL_NAME"
    LOG_DIR="$OUTPUT_DIR/150/$MODEL_NAME/logs"

    TEST_FILE=(
        "data/chronomagic_fvd_${TYPE}.json"
        "${VIDEO_FOLDER}/${MODEL_NAME}"
        "video"
    )

    CUDA_VISIBLE_DEVICES=0 torchrun \
        --nnodes=${NNODE} \
        --nproc_per_node=${NUM_GPUS} \
        --rdzv_backend=c10d \
        --rdzv_endpoint=localhost:12345 \
        tasks/video_feature_extract.py \
        --config_file configs/chronomagic_umtfvd_config.py \
        pretrained_path ${PRETRAINED} \
        batch_size 16 \
        output_dir ${TEMP_OUTPUT_DIR} \
        --test_file ${TEST_FILE[@]}
fi

if [[ ${TYPE} == 1649 ]]; then
    for part in {1..3}; do
        TEMP_OUTPUT_DIR="$OUTPUT_DIR/1649/${MODEL_NAME}_${part}"
        LOG_DIR="$OUTPUT_DIR/1649/${MODEL_NAME}_${part}/logs"

        TEST_FILE=(
            "data/chronomagic_fvd_${TYPE}.json"
            "${VIDEO_FOLDER}/${MODEL_NAME}/${part}"
            "video"
        )
        CUDA_VISIBLE_DEVICES=0 torchrun \
            --nnodes=${NNODE} \
            --nproc_per_node=${NUM_GPUS} \
            --rdzv_backend=c10d \
            --rdzv_endpoint=localhost:12345 \
            tasks/video_feature_extract.py \
            --config_file configs/chronomagic_umtfvd_config.py \
            pretrained_path ${PRETRAINED} \
            batch_size 16 \
            output_dir ${TEMP_OUTPUT_DIR} \
            --test_file ${TEST_FILE[@]}
    done
fi