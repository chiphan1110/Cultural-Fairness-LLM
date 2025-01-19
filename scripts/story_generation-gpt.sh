#!/bin/bash
BASE_DIR="$(dirname "$PWD")"  # Cultural-Fairness-LLM

python $BASE_DIR/src/generative_prompting.py \
    --model_id gpt-4 \
    --input_file $BASE_DIR/dataset/compiled_name.csv \
    --output_dir $BASE_DIR/generative/generated-stories \
    --culture Western Vietnamese
