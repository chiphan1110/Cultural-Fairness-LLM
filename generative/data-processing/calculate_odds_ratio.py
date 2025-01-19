import os
from collections import Counter
from operator import itemgetter
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm


def calculate_dict(viet_array, west_array):
    """
    Create Counter dictionaries for Vietnamese and Western adjectives.
    """
    counter_v = Counter(viet_array)
    counter_w = Counter(west_array)

    # Ensure no key lookup errors by balancing keys across both counters
    for key in set(counter_v) - set(counter_w):
        counter_w[key] = 0
    for key in set(counter_w) - set(counter_v):
        counter_v[key] = 0

    return counter_v, counter_w


def odds_ratio(v_dict, w_dict, topk=50, threshold=20):
    """
    Calculate Odds Ratio (OR) for adjectives based on their counts in Vietnamese and Western stories.

    Args:
        v_dict: Counter for Vietnamese adjectives.
        w_dict: Counter for Western adjectives.
        topk: Number of top results to return.
        threshold: Minimum occurrence threshold for adjectives.

    Returns:
        tuple: Top adjectives more common in Western and Vietnamese stories.
    """
    odds_ratio = {}
    total_num_v = sum(v_dict.values())
    total_num_w = sum(w_dict.values())

    for key in v_dict.keys():
        v_num = v_dict[key]
        w_num = w_dict[key]
        non_v_num = total_num_v - v_num
        non_w_num = total_num_w - w_num

        if v_num >= threshold and w_num >= threshold:
            # Calculate Odds Ratio
            or_value = (w_num / v_num) / (non_w_num / non_v_num)
            odds_ratio[key] = round(or_value, 2)

    # Return sorted Odds Ratios
    sorted_odds_ratio = dict(sorted(odds_ratio.items(), key=itemgetter(1), reverse=True))
    return sorted_odds_ratio


def load_adjectives_by_gender(input_dir, model, gender):
    """
    Load adjectives from text files for the given model and gender, grouped by culture.

    Args:
        input_dir: Directory containing text files.
        model: Model name to filter files.
        gender: Gender to filter files.

    Returns:
        tuple: Lists of Vietnamese and Western adjectives.
    """
    viet_adjectives = []
    west_adjectives = []

    for file in os.listdir(input_dir):
        if file.startswith(model) and gender in file:
            if "Vietnamese" in file:
                with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
                    viet_adjectives.extend(f.read().splitlines())
            elif "Western" in file:
                with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
                    west_adjectives.extend(f.read().splitlines())

    return viet_adjectives, west_adjectives


def save_results(odds_ratios, output_file):
    """
    Save Odds Ratio results to a CSV file, sorted by odds_ratio.

    Args:
        odds_ratios: Odds Ratios for adjectives.
        output_file: Path to save the CSV file.
    """
    # Prepare results
    results = [
        {"adjective": adj, "odds_ratio": or_value}
        for adj, or_value in odds_ratios.items()
    ]

    # Sort results by odds_ratio in descending order
    results = sorted(results, key=lambda x: x["odds_ratio"], reverse=True)

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input_folder", type=str, required=True, help="Folder containing input text files.")
    parser.add_argument("-t", "--threshold", type=int, default=20, help="Threshold for Odds Ratio calculation.")
    parser.add_argument("-o", "--output_folder", type=str, required=True, help="Folder to save output CSV files.")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    threshold = args.threshold

    # Analyze each model and gender separately
    analyzed_files = set()
    for file in tqdm(os.listdir(input_folder), desc="Processing files"):
        if not file.endswith(".txt"):
            continue

        # Parse the model and gender from the file name
        parts = file.split("_")
        if len(parts) < 3:
            print(f"Skipping invalid file: {file}")
            continue

        model = parts[0]
        gender = parts[1]
        key = (model, gender)
        if key in analyzed_files:
            continue

        analyzed_files.add(key)

        # Load adjectives for the current model and gender
        viet_adjectives, west_adjectives = load_adjectives_by_gender(input_folder, model, gender)

        if not viet_adjectives or not west_adjectives:
            print(f"Skipping {model} {gender}: insufficient data for Vietnamese or Western.")
            continue

        # Calculate Odds Ratios
        adj_counter_v, adj_counter_w = calculate_dict(viet_adjectives, west_adjectives)
        odds_ratios = odds_ratio(adj_counter_v, adj_counter_w, topk=50, threshold=threshold)

        # Save results to a CSV file
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, f"{model}_{gender}_odd-ratios.csv")
        save_results(odds_ratios, output_file)