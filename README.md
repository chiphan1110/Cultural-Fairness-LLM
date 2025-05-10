# Exploring Cultural Alignment and Bias in Large Language Model: A Vietnamese Contextual Study

## 1. Overview
As large language models (LLMs) increasingly influence global communication and decision-making, their ability to align with diverse cultural contexts and avoid reinforcing stereotypes is of critical importance. In this paper, we evaluate the cultural alignment and biases of state-of-the-art LLMs, including GPT-4, Llama-3, and Gemini-1.5, using Hofstede’s cultural dimensions and a generative analysis of stereotypes in language. 

In this project, we seek to address three fundamental questions: *(1) How accurately do LLM-generated responses align with Vietnamese cultural values compared to other countries? (2) To what extent can LLMs differentiate between Vietnamese cultural values and those of other nations? (3) What specific biases or stereotypes do LLMs exhibit toward Vietnamese culture?*

Our findings reveal that while LLMs exhibit strong intrinsic alignment with US cultural values,
they face significant challenges in representing underrepresented contexts, such as Vietnam. Furthermore, LLM-generated content reinforces cultural and gender stereotypes, associating Western names with traits of strength and refinement, while Vietnamese names are linked to modesty and tradition. These results highlight the need for more diverse training datasets, culturally sensitive model designs, and robust evaluation frameworks to mitigate bias and promote fairness in language technologies

## 2. Methodology

Our approach consists of two key components:

* **Discriminative Probing**: Leveraging Hofstede’s cultural dimensions (PDI, IDV, MAS, UAI, LTO, IVR), we design prompt templates to evaluate how LLMs respond under different cultural cues:

  * *Baseline prompting*: No cultural context
  * *Country-specific prompting*: Explicit country reference
  * *Citizenship prompting*: Role-playing as a citizen
  * *Language-specific prompting*: Questions in native language

* **Generative Probing**: We analyze stereotypes in model-generated stories by prompting LLMs to generate character descriptions for Vietnamese and Western names. Adjectives are extracted and evaluated using **Odds Ratio** to identify potential biases.

## 3. Findings

Key findings reveal that:

* All LLMs demonstrate a strong intrinsic alignment with U.S. cultural values.
* Vietnamese culture is consistently underrepresented and misranked in model responses.
* Generated content reinforces cultural and gender stereotypes—Vietnamese names are associated with modesty and tradition, while Western names are linked to strength and prominence.

👉 *Please refer to the [full report](COMP4040_FinalReport.pdf) for detailed results, visualizations, and statistical evaluations.*

## 4. Repository Structure

```
├── dataset/                      # All name datasets and translated survey questions
├── discriminative/               # Code and results for cultural dimension scoring
│   ├── data-processing/
│   ├── prompts/
│   └── results/
├── generative/                   # Code and outputs for story generation and adjective analysis
│   ├── data-processing/
│   ├── extracted-adj/
│   └── generated-stories/
├── scripts/                      # Shell and Python scripts to automate experiment pipeline
├── src/                          # Core implementation of the probing logic and prompt utilities
├── exploration.ipynb            # Jupyter notebook for exploratory analysis and visualization
├── README.md                    # Project documentation 
```

## 5. Acknowledgment

This project was conducted as part of the course COMP4040 - Data Mining at VinUniversity. We would like to express our gratitude for the course instructor Prof. Khoa Doan and TA Quang Nguyen for their supportive guidance and feedback.


