#!/bin/bash
BASE_DIR="$(dirname "$PWD")"  # Cultural-Fairness-LLM

# python $BASE_DIR/src/generative_prompting.py \
#     --model_id gpt-4 \
#     --input_file $BASE_DIR/dataset/compiled_name.csv \
#     --output_dir $BASE_DIR/generative/generated-stories \
#     --culture Western Vietnamese

# python $BASE_DIR/src/generative_prompting.py \
#     --model_id meta-llama/Llama-3.3-70B-Instruct-Turbo \
#     --input_file $BASE_DIR/dataset/compiled_name.csv \
#     --output_dir $BASE_DIR/generative/generated-stories \
#     --culture Western Vietnamese

python $BASE_DIR/src/generative_prompting.py \
    --model_id gemini-1.5-flash \
    --input_file $BASE_DIR/dataset/compiled_name.csv \
    --output_dir $BASE_DIR/generative/generated-stories \
    --culture Western Vietnamese