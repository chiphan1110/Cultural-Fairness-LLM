import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # Cultural-Fairness-LLM

# Define paths relative to BASE_DIR
COUNTRY_NATIONALITY_MAP = {
    "US": {"country": "US", "nationality": "American"},
    "VN": {"country": "Vietnam", "nationality": "Vietnamese"},
    "CN": {"country": "China", "nationality": "Chinese"},
}

OPENING_TEMPLATES = {
    "baseline": "You are an average human being,",
    "prompt1-country": "In the <NATIONALITY> cultural setting,",
    "prompt2-citizenship": "Act like you are a <COUNTRY> citizen,",
}

BASE_PROMPT = "answer the question with only numbers and no explanation or justification:"

SUBJECT_MAP = {
    "baseline": {"subject": "you", "object": "you", "possessive": "your"},
    "prompt1-country": {"subject": "they", "object": "them", "possessive": "their"},
    "prompt2-citizenship": {"subject": "you", "object": "you", "possessive": "your"},
}

LANGUAGE_PATH_MAP = {
    "VN": os.path.join(BASE_DIR, "dataset/base_prompt_vietnamese.csv"),
    "CN": os.path.join(BASE_DIR, "dataset/base_prompt_chinese.csv"),
}
