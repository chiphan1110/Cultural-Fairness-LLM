import os
import json
import argparse
import pandas as pd

from prompt_utils import COUNTRY_NATIONALITY_MAP, OPENING_TEMPLATES, BASE_PROMPT, SUBJECT_MAP, LANGUAGE_PATH_MAP


class PromptGenerator:
    def __init__(self, questionnaire_path, output_dir, prompting_method):
        self.questionnaire_path = questionnaire_path
        self.output_dir = output_dir
        self.prompting_method = prompting_method
        self.data = None
        
    def generate_prompts(self, prompting_method, country_code=None):     
        if prompting_method == "prompt3-language":
            self.data = pd.read_csv(LANGUAGE_PATH_MAP[country_code])
        else:
            self.data = pd.read_csv(self.questionnaire_path)
            country = COUNTRY_NATIONALITY_MAP[country_code]["country"] if country_code else None
            nationality = COUNTRY_NATIONALITY_MAP[country_code]["nationality"] if country_code else None
            subject = SUBJECT_MAP[prompting_method]["subject"] 
            possessive = SUBJECT_MAP[prompting_method]["possessive"]
            object_ = SUBJECT_MAP[prompting_method]["object"]
        
        prompts = []
        
        for _, row in self.data.iterrows():
            if prompting_method == "prompt3-language":
                # For prompt3-language, structure includes nationality + aspect + question + choices
                full_prompt = (
                    f"{row['Nationality']} {row['Aspect']} {row['Question']}? {row['Choices']}"
                )
            else:
                # Replace placeholders in the question text
                question = row["Question"].replace("<SUBJECT>", subject).replace("<POSSESSIVE>", possessive).replace("<OBJECT>", object_)
                aspect = row["Aspect"].replace("<SUBJECT>", subject).replace("<POSSESSIVE>", possessive).replace("<OBJECT>", object_)

                if prompting_method == "prompt1-country":
                    opening = OPENING_TEMPLATES[prompting_method].replace("<NATIONALITY>", nationality)
                elif prompting_method == "prompt2-citizenship":
                    opening = OPENING_TEMPLATES[prompting_method].replace("<COUNTRY>", nationality)
                else:  # baseline
                    opening = OPENING_TEMPLATES[prompting_method]

                full_prompt = (
                    f"{opening} {BASE_PROMPT} {aspect} {question}? "
                    f"{row['Choices']}"
                )

            prompts.append(
                {
                    "question_id": row["QuestionID"],
                    "prompt": full_prompt,
                }
            )
        return prompts
        
    def save_prompts(self, prompting_method, prompts, country_code=None):
        if prompting_method == "baseline":
            output_path = os.path.join(self.output_dir, f"{prompting_method}.json")
        else:
            output_path = os.path.join(self.output_dir, f"{prompting_method}-{country_code}.json")
            
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(prompts, f, indent=4, ensure_ascii=False)
        print(f"Prompts saved to {output_path}.")
        
    def generate_and_save_prompts(self):
        if self.prompting_method in ["prompt1-country", "prompt2-citizenship"]:
            # Generate prompts for all countries
            for country_code in COUNTRY_NATIONALITY_MAP.keys():
                prompts = self.generate_prompts(self.prompting_method, country_code)
                self.save_prompts(self.prompting_method, prompts, country_code)
                
        elif self.prompting_method == "prompt3-language":
            for country_code in LANGUAGE_PATH_MAP.keys():
                prompts = self.generate_prompts(self.prompting_method, country_code)
                self.save_prompts(self.prompting_method, prompts, country_code)
        else:
            # Generate prompts for baseline
            prompts = self.generate_prompts(self.prompting_method)
            self.save_prompts(self.prompting_method, prompts)


def argument_parser():
    parser = argparse.ArgumentParser(description="Generate prompts from a CSV file.")
    parser.add_argument("--questionnaire_path", required=False, help="Path to the CSV file")
    parser.add_argument("--output_dir", required=True, help="Directory to save the generated prompts (JSON format)")
    parser.add_argument("--prompting_method", required=True, choices=["baseline", "prompt1-country", "prompt2-citizenship", "prompt3-language"],
                        help="Prompting method to use: baseline, prompt1-country, or prompt2-citizenship")
    return parser.parse_args()


def main():
    args = argument_parser()
    generator = PromptGenerator(args.questionnaire_path, args.output_dir, args.prompting_method)
    generator.generate_and_save_prompts()


if __name__ == "__main__":
    main()