# WIP
Separate steps for running experiments on HarmBench and Decomposer. Each notebook requires a separate requirements file 

## Content:
### Colab Notebooks
- **experiments_generate_completions.ipynb** - installs only the packages required to generate completions. Saves resulting json, config and token-price summary. Should use _generate_completions.py_ from these repo to work
- **experiments__evaluate.ipynb** - evaluates the completions, merges the evaluated json with tooken-price summary and pushes to wandb. Creates a summary table for n runs
### Scripts
- **generate_completions.py** - Harmbench script without vllm and transformers import
### Txt files
- **requirements_generate_completions.txt** - requirements for running _experiments_generate_completions_ notebook
- **requirements_full.txt** - requirements for running _experiments__evaluate_ notebook
