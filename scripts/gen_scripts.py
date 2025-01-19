import os

def generate_bash_script(models, prompting_methods, country_codes, input_dir, output_dir, output_script_path):
    """
    Generates a Bash script for running the specified models, prompting methods, and country codes.
    
    Args:
        models (list): List of model IDs.
        prompting_methods (list): List of prompting techniques.
        country_codes (dict): Dictionary where keys are prompting methods requiring country codes and values are lists of codes.
        input_dir (str): Input directory path.
        output_dir (str): Output directory path.
        output_script_path (str): File path to save the generated Bash script.
    """
    base_dir_var = "$(dirname \"$PWD\")"  # Base directory variable for portability
    script_lines = [f"#!/bin/bash\n\nBASE_DIR=\"{base_dir_var}\"  # Cultural-Fairness-LLM\n"]

    for model in models:
        script_lines.append(f"# {model}")
        
        for prompting_method in prompting_methods:
            country_arg = ""
            if prompting_method in country_codes:
                # Generate country codes argument
                codes = " ".join(country_codes[prompting_method])
                country_arg = f"--country_codes {codes} \\"
            
            # Add script section
            script_lines.append(f"## {prompting_method.capitalize().replace('-', ' ')}")
            script_lines.append(f"python \"$BASE_DIR/discriminative/src/prompting.py\" \\")
            script_lines.append(f"    --model_id {model} \\")
            script_lines.append(f"    --prompting_technique {prompting_method} \\")
            if country_arg:
                script_lines.append(f"    {country_arg}")
            script_lines.append(f"    --input_dir {input_dir} \\")
            script_lines.append(f"    --output_dir {output_dir}\n")
        script_lines.append("#"*50+"\n")

    # Write the generated script to file
    with open(output_script_path, "w") as script_file:
        script_file.write("\n".join(script_lines))
    
    print(f"Bash script saved to: {output_script_path}")


if __name__ == "__main__":
    models = [
        "meta-llama/Llama-3.3-70B-Instruct-Turbo", 
        "gemini-1.5-flash",
        "gpt-4"
    ]

    prompting_methods = [
        "baseline",
        "prompt1-country",
        "prompt2-citizenship",
        "prompt3-language"
    ]

    country_codes = {
        "prompt1-country": ["CN", "VN", "US"],
        "prompt2-citizenship": ["CN", "VN", "US"],
        "prompt3-language": ["CN", "VN"]
    }

    input_dir = "$BASE_DIR/discriminative/prompts/"
    output_dir = "$BASE_DIR/discriminative/results/"
    output_script_path = "/Users/chiphan/Documents/Chi/1-Learning/2024-Fall/COMP4040-DataMining/Assignment/Project/code/Cultural-Fairness-LLM/scripts/discriminative_prompting.sh"

    # Generate the script
    generate_bash_script(models, prompting_methods, country_codes, input_dir, output_dir, output_script_path)