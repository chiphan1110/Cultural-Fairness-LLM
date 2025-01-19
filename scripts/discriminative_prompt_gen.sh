#!/bin/bash

BASE_DIR="$(dirname "$PWD")"    # Cultural-Fairness-LLM


# Baseline
python "$BASE_DIR/src/discriminative_prompt_generation.py" \
    --questionnaire_path "$BASE_DIR/dataset/base_prompt.csv" \
    --output_dir "$BASE_DIR/discriminative/prompts" \
    --prompting_method baseline


# Prompting method 1: Country-based
python "$BASE_DIR/src/discriminative_prompt_generation.py" \
    --questionnaire_path "$BASE_DIR/dataset/base_prompt.csv" \
    --output_dir "$BASE_DIR/discriminative/prompts" \
    --prompting_method prompt1-country 

# Prompting method 2: Citizenship-based
python "$BASE_DIR/src/discriminative_prompt_generation.py" \
    --questionnaire_path "$BASE_DIR/dataset/base_prompt.csv" \
    --output_dir "$BASE_DIR/discriminative/prompts" \
    --prompting_method prompt2-citizenship 

# Prompting method 3: Language-based
python "$BASE_DIR/src/discriminative_prompt_generation.py" \
    --questionnaire_path "$BASE_DIR/dataset/base_prompt.csv" \
    --output_dir "$BASE_DIR/discriminative/prompts" \
    --prompting_method prompt3-language