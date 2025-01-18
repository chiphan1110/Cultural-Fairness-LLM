import os
import torch
import json
import time
import copy
import random
import getpass
import textwrap
import pandas as pd
import argparse


from tqdm import tqdm
# from langchain_google_genai import ChatGoogleGenerativeAI
from transformers import pipeline
from together import Together

from utils import _DOMAIN_TO_FILE_PATH, _MODEL_ID_TO_FILE_PATH
from prompt_utils import (
    MULTISTEP_ARITHMETIC_PROMPTS,
    DYCK_LANGUAGES_PROMPTS,
    LOGICAL_DEDUCTION_PROMPTS,
    TRACKING_SHUFFLED_OBJECTS_PROMPTS,
    WORD_SORTING_PROMPTS, 
    SelfCheck
)

os.environ['TOGETHER_API_KEY'] = "ebbe80af6da09a2c18bccff9c1785a9cef0ffcb3a13725c3a50b8707a5de651c"



class PromptClient:
    def __init__(self, model_id, prompting_technique):
        self.model_id = model_id
        self.llm = None
        self.prompting_technique = prompting_technique
        self.selfcheck = None
        self.prompt_template = None
        self.domain = None

    def init_domain(self, domain):
        self.domain = domain
        if self.prompting_technique == "selfcheck":
            self.selfcheck = SelfCheck()
        exec(f"self.prompt_template = {self.domain + '_PROMPTS'}")

    def format_messages(self, messages):
        """
        Convert the list of messages into a single string prompt.
        """
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    
    def model_call(self, messages):
        if self.model_id.startswith("Qwen/"):
            if self.llm is None:
                self.llm = Together()
            response = self.llm.chat.completions.create(
                model=self.model_id,
                messages=messages,
                max_tokens=100,
                temperature=0.7,
                top_p=0.7,
                top_k=50,
                repetition_penalty=1,
                stop=["<|im_end|>","<|endoftext|>"],
                stream=False
            )
            out = response.choices[0].message.content
            
        if self.model_id.startswith("meta-llama/Llama"):
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            device = torch.device("cpu")
            pipe = pipeline("text-generation", 
                            model=self.model_id, 
                            max_new_tokens=10,
                            device=device
                    )
            out = pipe(messages)[0]['generated_text'][-1]['content']
            
        elif self.model_id.startswith("gemini") :
            if "GOOGLE_API_KEY" not in os.environ:
                os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
            if self.llm is None:
                self.llm = ChatGoogleGenerativeAI(
                    model=self.model_id,
                    max_tokens=None,
                    temperature=0,
                    max_retries=2,
                )
            out = self.llm.invoke(messages).content
            out = out.strip()
            time.sleep(3.5)

        return out.strip()
    
    def direct_messages(self, input, steps):
        joined_steps = '\n'.join(
            [f"Thought {i+1}: {step}"
            for i, step in enumerate(steps)]
        )
        message = {
            "role": "user",
            "content": self.prompt_template['DIRECT_TEMPLATE'].format(input=input, steps=joined_steps)
        }
        messages = (self.prompt_template['DIRECT_MESSAGES'][0], )
        messages += (message, )
        return messages
    
    def direct_perstep_messages(self, input, cur_messages, cur_steps, step_id):
        message = {
            "role": "user",
            "content": self.prompt_template['DIRECT_PERSTEP_TEMPLATE'].format(input=input, steps=cur_steps, current_step=step_id)
        }
        return cur_messages + (message,)
    
    def cot_perstep_messages(self, input, cur_messages, cur_steps, step_id):
        message = {
            "role": "user",
            "content": self.prompt_template['COT_PERSTEP_TEMPLATE'].format(input=input, steps=cur_steps, current_step=step_id)
        }
        return cur_messages + (message,)
    
    def direct_output(self, input, steps):
        messages = self.direct_messages(input, steps)
        output = self.model_call(messages).strip()
        output = int(output) - 1 if output.isdigit() else -1
        return output
    
    def direct_perstep_output(self, input, steps):
        start_time = time.time()
        cur_messages = (self.prompt_template['DIRECT_PERSTEP_MESSAGES'][0], )
        joined_steps = ""
        false_step_idx = -1
        for idx, step in enumerate(steps):
            joined_steps += f"Thought {idx+1}: {step}\n"
            cur_messages = self.direct_perstep_messages(input, cur_messages, joined_steps.strip(), idx+1)
            cur_response = self.model_call(cur_messages)
            cur_messages += ({
                "role": "assistant",
                "content": cur_response
            },)
            if "No" in cur_response:
                false_step_idx = idx
                break
        # print("Inference time:", time.time() - start_time, "seconds")
        return false_step_idx
    
    def cot_perstep_output(self, input, steps):
        start_time = time.time()
        cur_messages = (self.prompt_template['COT_PERSTEP_MESSAGES'][0], )
        joined_steps = ""
        false_step_idx = -1
        for idx, step in enumerate(steps):
            joined_steps += f"Thought {idx+1}: {step}\n"
            cur_messages = self.cot_perstep_messages(input, cur_messages, joined_steps.strip(), idx+1)
            cur_response = self.model_call(cur_messages)
            cur_messages += ({
                "role": "assistant",
                "content": cur_response
            },)
            if "No" in cur_response:
                false_step_idx = idx
                break
        # print("Inference time:", time.time() - start_time, "seconds")
        return false_step_idx
    
    def selfcheck_output(self, input, steps):
        """ Adapt from https://arxiv.org/pdf/2308.00436
        """
        start_time = time.time()
        record_list = self.selfcheck.initialize_record_list([{"input": input, "steps": steps}])
        false_step_idx = self.selfcheck.verify_steps(record_list, self.model_call)
        # print("Inference time:", time.time() - start_time, "seconds")
        return false_step_idx

    def process(self, input, steps):
        return getattr(self, self.prompting_technique + "_output")(input, steps)

def parse_args():
    parser = argparse.ArgumentParser(description="Script to configure prompting techniques")
    
    parser.add_argument(
        "--model_id", 
        choices=["meta-llama/Llama-3.2-3B-Instruct", "meta-llama/Llama-3.1-8B-Instruct", 
                 "gemini-1.5-pro", "gemini-1.5-flash", 
                 "Qwen/QwQ-32B-Preview", "Qwen/Qwen2.5-Coder-32B-Instruct",  "Qwen/Qwen2-72B-Instruct"], 
        default="gemini-1.5-pro", 
        help="Choose your model"
    )
    
    parser.add_argument(
        "--domain", 
        choices=["DYCK_LANGUAGES", "MULTISTEP_ARITHMETIC", "TRACKING_SHUFFLED_OBJECTS", "WORD_SORTING", "LOGICAL_DEDUCTION"], 
        default="MULTISTEP_ARITHMETIC", 
        help="Choose your domain knowledge"
    )
    
    parser.add_argument(
        "--prompting_technique", 
        choices=["direct", "direct_perstep", "cot_perstep", "selfcheck"], 
        default="direct", 
        help="Choose your prompting technique"
    )
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    # Load data
    pth_to_data = _DOMAIN_TO_FILE_PATH[args.domain]
    pd_dataframe = pd.read_json(path_or_buf=pth_to_data, lines=True)
    num_samples = len(pd_dataframe)
    print(f"Number of samples in {args.domain} domain:", num_samples)
    
    # Create prompting agent
    prompt_agent = PromptClient(args.model_id, args.prompting_technique)
    prompt_agent.init_domain(args.domain)

    # Prepare save file
    save_file_name = f"{_MODEL_ID_TO_FILE_PATH[args.model_id]}__{args.domain}__{args.prompting_technique}.json"
    os.makedirs("prompting/results", exist_ok=True)
    save_file_path = os.path.join("prompting/results", save_file_name)
    
    # Load existing results if the file exists
    if os.path.exists(save_file_path):
        with open(save_file_path, "r") as file:
            predictions = json.load(file)
            processed_ids = {pred["id"] for pred in predictions}
            print(f"Resuming from {len(processed_ids)} processed samples.")
    else:
        predictions = []
        processed_ids = set()
        print("Starting from scratch.")
    
    # Iterating through samples
    start = time.time()
    try:
        for idx, sample in tqdm(pd_dataframe.iterrows(), total=num_samples):
            if idx in processed_ids:
                continue  # Skip already processed samples

            input = sample['input']
            steps = sample['steps']
            prediction = prompt_agent.process(input, steps)
            output = int(sample['mistake_index']) if sample['mistake_index'] == sample['mistake_index'] else -1 
            predictions.append({
                "id" : idx,
                "input" : input,
                "predicted_mistake_index" : prediction,
                "output" : output
            })

            # Save progress after each prediction
            with open(save_file_path, "w") as file:
                json.dump(predictions, file, indent=4)
    except KeyboardInterrupt:
        print("Execution interrupted. Saving progress...")
    except Exception as e:
        print(f"An error occurred: {e}. Saving progress...")

    # Final save after completing all samples
    with open(save_file_path, "w") as file:
        json.dump(predictions, file, indent=4)

    end = time.time()
    print(f"Total inference time: {end - start} seconds")