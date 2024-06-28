models=(
    test
)
type=150  # 150 or 1649
seeds=(12 22 32 42)
current_dir=$(pwd)

run_script() {
    local model=$1
    local seed=$2
    echo "Computing FVD for model $model with seed $seed"
    cd main
    CUDA_VISIBLE_DEVICES=1 python src/scripts/calc_metrics_for_dataset.py \
        --real_feat_path ${current_dir}/gt_feature/gt${type}_feats.pt \
        --fake_feat_path ${current_dir}/results/UMTFVD/feature/${type}/${model}/${model}.pt \
        --save_path ${current_dir}/results/UMTFVD/scores/${type}/${model} \
        --metrics fvd32_16f,fvd64_16f,fvd128_16f,fvd256_16f,fvd300_16f,fvd512_16f,fvd1024_16f \
        --mirror 1 \
        --gpus 1 \
        --resolution 256 \
        --verbose 0 \
        --use_cache 0 \
        --seed $seed
}

export type
export current_dir
export -f run_script

parallel -j 8 run_script ::: "${models[@]}" ::: "${seeds[@]}"