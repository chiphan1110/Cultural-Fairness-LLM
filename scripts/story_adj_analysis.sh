#!/bin/bash
BASE_DIR="$(dirname "$PWD")"  # Cultural-Fairness-LLM

python $BASE_DIR/generative/data-processing/calculate_odds_ratio.py \
     --input_folder $BASE_DIR/generative/extracted-adj \
     --threshold 5 \
     --output_folder $BASE_DIR/generative/extracted-adj/output_odds_ratios

