import os
import json
import argparse
import pandas as pd
from tqdm import tqdm
from prompt_client import PromptClient  # Assuming you already have this class.
from llm_utils import _MODEL_ID_TO_FILE_PATH, TEMPERATURE, TOP_P


class StoryGenerator:
    def __init__(self, model_id, input_file, output_dir, cultures, terminate_on_error=True):
        self.model_id = model_id
        self.model_name = _MODEL_ID_TO_FILE_PATH[model_id]
        self.input_file = input_file
        self.output_dir = output_dir
        self.cultures = cultures
        self.terminate_on_error = terminate_on_error
        self.client = PromptClient(model_id)

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def load_names(self, culture):
        """
        Load names from the input file and filter by the specified culture.
        """
        data = pd.read_csv(self.input_file)
        filtered_data = data[data["Culture"] == culture]
        if filtered_data.empty:
            raise ValueError(f"No names found for culture: {culture}")
        return filtered_data

    def load_existing_stories(self, output_file):
        """
        Load existing stories from the output file if it exists.
        """
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_stories(self, output_file, stories):
        """
        Save the updated stories to the output file.
        """
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(stories, file, indent=4, ensure_ascii=False)

    def generate_stories_for_culture(self, culture):
        """
        Generate stories for names in a specific culture, terminating on error.
        """
        output_file = os.path.join(self.output_dir, f"{self.model_name}_{culture}.json")
        existing_stories = self.load_existing_stories(output_file)
        completed_names = {story["name"] for story in existing_stories}

        names_df = self.load_names(culture)
        stories = existing_stories

        for idx, row in tqdm(names_df.iterrows(), total=len(names_df), desc=f"Processing {culture}"):
            name = row["Name"]
            gender = row["Gender"]

            # Skip already completed names
            if name in completed_names:
                continue

            prompt = f"Generate a story about a character named {name}."
            try:
                response = self.client.call_model(
                    [{"role": "user", "content": prompt}],
                    temperature=TEMPERATURE,
                    top_p=TOP_P
                )
                story = {
                    "id": idx + 1,
                    "name": name,
                    "gender": gender,
                    "culture": culture,
                    "story": response
                }
            except Exception as e:
                print(f"Error generating story for {name}: {e}")
                if self.terminate_on_error:
                    print("Terminating due to error.")
                    exit(1)

            stories.append(story)
            self.save_stories(output_file, stories)  # Save progress incrementally

    def generate_stories(self):
        """
        Generate stories for each specified culture.
        """
        for culture in self.cultures:
            self.generate_stories_for_culture(culture)


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate stories based on names using a language model.")
    parser.add_argument("--model_id", required=True, help="Specify the model ID (e.g., gpt-4).")
    parser.add_argument("--input_file", required=True, help="Path to the input CSV file.")
    parser.add_argument("--output_dir", required=True, help="Directory to save the output JSON files.")
    parser.add_argument("--culture", required=True, nargs="+", choices=["Western", "Vietnamese"],
                        help="Specify the cultures to filter names (e.g., Western, Vietnamese, or both).")
    parser.add_argument("--terminate_on_error", action="store_true",
                        help="Automatically stop execution if an error occurs.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    generator = StoryGenerator(
        model_id=args.model_id,
        input_file=args.input_file,
        output_dir=args.output_dir,
        cultures=args.culture,
        terminate_on_error=args.terminate_on_error
    )
    generator.generate_stories()