#!/bin/bash
BASE_DIR="$(dirname "$PWD")"  # Cultural-Fairness-LLM

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/Llama-3.3-70B-Instruct-Turbo_Western.json \
        --output_dir $BASE_DIR/generative/extracted-adj

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/Llama-3.3-70B-Instruct-Turbo_Vietnamese.json \
        --output_dir $BASE_DIR/generative/extracted-adj

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/GPT-4_Western.json \
        --output_dir $BASE_DIR/generative/extracted-adj

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/GPT-4_Vietnamese.json \
        --output_dir $BASE_DIR/generative/extracted-adj

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/Gemini-1.5-flash_Western.json \
        --output_dir $BASE_DIR/generative/extracted-adj

python $BASE_DIR/generative/data-processing/adj_extraction.py \
        --input_file $BASE_DIR/generative/generated-stories/Gemini-1.5-flash_Vietnamese.json \
        --output_dir $BASE_DIR/generative/extracted-adj