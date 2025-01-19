import os
import json
import spacy
import argparse
from collections import defaultdict
from pathlib import Path


def extract_adjectives(input_file, output_dir):
    """
    Extracts adjectives from stories in a JSON file and saves them to separate files by culture and gender.

    Args:
        input_file (str): Path to the input JSON file.
        output_dir (str): Directory where output files will be saved.
    """
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Load the JSON data
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Organize adjectives by culture and gender
    adjective_data = defaultdict(list)

    for entry in data:
        story_id = entry.get("id", "unknown")
        name = entry.get("name", "unknown")
        gender = entry.get("gender", "unknown")
        culture = entry.get("culture", "unknown")
        story = entry.get("story", "")

        # Process the story using spaCy
        doc = nlp(story)
        adjectives = [token.text for token in doc if token.pos_ == "ADJ"]

        # Create a unique key for output naming
        key = f"{gender}_{culture}"
        adjective_data[key].extend(adjectives)

    # Save adjectives to output files
    if os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    for key, adjectives in adjective_data.items():
        model_name = input_file.split("/")[-1].split("_")[0]
        output_file = os.path.join(output_dir, f"{model_name}_{key}.txt")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(adjectives))
        print(f"Saved adjectives for {key} to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Extract adjectives from LLM-generated stories.")
    parser.add_argument("--input_file", type=str, help="Path to the JSON file with LLM-generated stories.")
    parser.add_argument(
        "--output_dir", type=str, default="output", help="Directory where extracted adjectives will be saved."
    )
    args = parser.parse_args()

    extract_adjectives(args.input_file, args.output_dir)


if __name__ == "__main__":
    main()