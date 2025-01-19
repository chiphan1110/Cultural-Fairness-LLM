#!/bin/bash

BASE_DIR="$(dirname "$PWD")"  # Cultural-Fairness-LLM

# meta-llama/Llama-3.3-70B-Instruct-Turbo
## Baseline
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --prompting_technique baseline \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt1 country
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --prompting_technique prompt1-country \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt2 citizenship
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --prompting_technique prompt2-citizenship \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt3 language
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --prompting_technique prompt3-language \
    --country_codes CN VN \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/


# gemini-1.5-flash
## Baseline
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gemini-1.5-flash \
    --prompting_technique baseline \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt1 country
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gemini-1.5-flash \
    --prompting_technique prompt1-country \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

# Prompt2 citizenship
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gemini-1.5-flash \
    --prompting_technique prompt2-citizenship \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt3 language
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gemini-1.5-flash \
    --prompting_technique prompt3-language \
    --country_codes CN VN \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

##################################################

# gpt-4
## Baseline
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gpt-4 \
    --prompting_technique baseline \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt1 country
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gpt-4 \
    --prompting_technique prompt1-country \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

## Prompt2 citizenship
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gpt-4 \
    --prompting_technique prompt2-citizenship \
    --country_codes CN VN US \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

# Prompt3 language
python "$BASE_DIR/discriminative/src/prompting.py" \
    --model_id gpt-4 \
    --prompting_technique prompt3-language \
    --country_codes CN VN \
    --input_dir $BASE_DIR/discriminative/prompts/ \
    --output_dir $BASE_DIR/discriminative/results/

#################################################
