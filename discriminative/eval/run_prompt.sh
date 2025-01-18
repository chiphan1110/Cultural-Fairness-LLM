export PYTHONPATH="$PWD:$PYTHONPATH"
# export CUDA_VISIBLE_DEVICES=5

python prompting/prompting.py --model_id "Qwen/QwQ-32B-Preview" \
                    --domain MULTISTEP_ARITHMETIC \
                    --prompting_technique selfcheck
