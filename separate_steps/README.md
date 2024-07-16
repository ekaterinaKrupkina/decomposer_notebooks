# WIP
Separate steps for running experiments on HarmBench and Decomposer

Content:
- experiments_generate_completions - installs only the packages required to generate completions. Saves resulting json, config and token-price summary
- experiments_evaluate - evaluates the completions, merges the evaluated json with tooken-price summary and pushes to wandb. Creates a summary table for n runs

TODO
- add
  - requirements_generation.txt
  - requirements_full.txt
