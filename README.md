# LLM Evaluation Project

This repo contains an exploratory project to evaluate Large Language Models (LLMs) (Azure OpenAI) for:

1. **Analytical tasks** on real datasets (MIMIC ICU mortality and Titanic survival).
2. **Simple question–answer & chatbot use cases**, via:
   - A **command-line chatbot**.
   - A **Streamlit analytical chatbot**.

The project was designed as a learning exercise for model selection, evaluation, and basic tooling around Azure OpenAI.

---

## Project goals

- Compare different LLMs on:
  - **Analytical prompts** (EDA, missing values, modeling strategy, etc.).
  - (Optionally) **simple extraction tasks**.
- Log responses and basic metrics (latency, token usage).
- Manually score analytical answers on:
  - Clarity  
  - Technical correctness  
  - Depth of insight
- Build a small **analytical chatbot** powered by Azure OpenAI:
  - CLI version.
  - Web UI using Streamlit.

---

## Repository structure

- `eval_models.ipynb`  
  Main notebook:
  - Loads the MIMIC and Titanic datasets.
  - Builds analytical prompts using real summaries / missing-value profiles.
  - Calls one or more models (Azure OpenAI + others) and logs:
    - model name  
    - task id  
    - prompt  
    - model output  
    - latency (seconds)  
    - input / output tokens  
  - Exports results to CSV / Excel for manual scoring.

- `app.py` – **Streamlit analytical chatbot** using Azure OpenAI and environment variables. :contentReference[oaicite:0]{index=0}  

- `chat_terminal.py` – **command-line chatbot** that keeps the conversation history and talks in Spanish. :contentReference[oaicite:1]{index=1}  

- `mimic_train.csv`  
  Sample ICU stay data derived from the MIMIC project (predicting in-hospital mortality, `HOSPITAL_EXPIRE_FLAG`).

- `titanic3.csv`  
  Classic Titanic passenger dataset used for survival prediction and missing-value handling exercises.

- `analytical_results.csv`  
- `analytical_results_mimic.xlsx`  
- `analytical_results_titanic.csv`  
- `analytical_results.xlsx`  
  Logged analytical model outputs and (optionally) manual scores for clarity / technical quality / insight.

- `.gitignore`  
  Ensures local secrets (e.g. `.env`) are not committed.

> **Important:** The `.env` file with API keys is intentionally **not** included in this repository.

---

## Tech stack

- Python 3.x
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- `openai` Python SDK (AzureOpenAI client)
- `python-dotenv`
- `pandas`
- `streamlit`

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/ragaco1117/excelexorcist_project.git
cd excelexorcist_project
