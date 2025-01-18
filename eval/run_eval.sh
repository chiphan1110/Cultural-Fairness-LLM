#!/bin/bash

reference_paths="prompting/results/QwQ-32B-Preview__MULTISTEP_ARITHMETIC__selfcheck.json"

python eval/eval.py --references "[$reference_paths]" --output_csv eval/results.csv