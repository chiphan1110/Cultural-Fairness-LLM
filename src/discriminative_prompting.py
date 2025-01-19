import os
import sys
import json
import argparse
from tqdm import tqdm
from prompt_client import PromptClient
from llm_utils import _MODEL_ID_TO_FILE_PATH, TEMPERATURE, TOP_P, TRIALS

class PromptProcessor:
    def __init__(self, model_id, prompting_technique, country_codes, input_dir, output_dir):
        self.model_id = model_id
        self.prompting_technique = prompting_technique
        self.country_codes = country_codes
        self.input_dir = input_dir
        # Create a folder for the model inside the output directory
        self.model_name = _MODEL_ID_TO_FILE_PATH[model_id]
        self.output_dir = os.path.join(output_dir, self.model_name)
        self.client = PromptClient(model_id)

        # Ensure the model-specific output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def construct_input_file(self, country_code=None):
        """
        Construct the input file path based on the prompting technique and country code.
        """
        if self.prompting_technique == "baseline":
            return os.path.join(self.input_dir, "baseline.json")
        else:
            input_file = f"{self.prompting_technique}-{country_code}.json"
            return os.path.join(self.input_dir, input_file)

    def load_prompts(self, country_code=None):
        """
        Load input prompts from a dynamically constructed file.
        """
        input_file = self.construct_input_file(country_code)
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        with open(input_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_results(self, results, country_code=None, trial=None):
        """
        Save the generated results for a specific trial to a JSON file.
        """
        if self.prompting_technique == "baseline":
            # File name for baseline (no country code, trial-specific)
            output_file = os.path.join(
                self.output_dir,
                f"{self.model_name}_{self.prompting_technique}_trial{trial}.json"
            )
        else:
            # File name for other techniques (with country code and trial-specific)
            output_file = os.path.join(
                self.output_dir,
                f"{self.model_name}_{self.prompting_technique}_{country_code}_trial{trial}.json"
            )

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4, ensure_ascii=False)

        print(f"Results for trial {trial} saved to {output_file}")

    def process_for_country(self, country_code=None):
        """
        Process prompts and generate model responses for a specific country, saving each trial to a separate file.
        """
        prompts = self.load_prompts(country_code)

        for trial in range(TRIALS):
            results = []

            for item in tqdm(prompts, desc=f"Processing prompts for {country_code if country_code else 'baseline'} (Trial {trial + 1})"):
                messages = [{"role": "user", "content": item["prompt"]}]
                try:
                    response = self.client.call_model(messages, temperature=TEMPERATURE, top_p=TOP_P)
                    results.append({
                        "question_id": item["question_id"],
                        "prompt": item["prompt"],
                        "response": response
                    })
                except Exception as e:
                    print(f"Error processing question_id {item['question_id']} (Trial {trial + 1}): {e}")
                    results.append({
                        "question_id": item["question_id"],
                        "prompt": item["prompt"],
                        "response": "ERROR"
                    })

            # Save results for this trial
            self.save_results(results, country_code, trial + 1)

    def process(self):
        """
        Main process function that handles multiple countries if specified.
        """
        if self.prompting_technique == "baseline":
            # Process baseline (no country codes)
            self.process_for_country()
        else:
            # Process for each specified country
            for country_code in self.country_codes:
                self.process_for_country(country_code)


def parse_args():
    parser = argparse.ArgumentParser(description="Prompting client for multiple models and techniques.")
    parser.add_argument("--model_id", required=True, choices=list(_MODEL_ID_TO_FILE_PATH.keys()),
                        help="Specify the model ID.")
    parser.add_argument("--prompting_technique", required=True,
                        choices=["baseline", "prompt1-country", "prompt2-citizenship", "prompt3-language"],
                        help="Specify the prompting technique.")
    parser.add_argument("--country_codes", nargs="*", choices=["US", "CN", "VN"],
                        help="Specify the list of country codes (e.g., US CN VN). Not required for baseline.")
    parser.add_argument("--input_dir", required=True, help="Directory containing input JSON files.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the output results.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # Validate arguments
    if args.prompting_technique != "baseline" and not args.country_codes:
        raise ValueError("country_codes must be provided for non-baseline prompting techniques.")

    processor = PromptProcessor(
        model_id=args.model_id,
        prompting_technique=args.prompting_technique,
        country_codes=args.country_codes if args.country_codes else [],
        input_dir=args.input_dir,
        output_dir=args.output_dir
    )
    processor.process()