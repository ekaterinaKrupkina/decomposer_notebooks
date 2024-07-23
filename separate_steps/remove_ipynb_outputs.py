import json
import sys

def remove_outputs(notebook):
    for cell in notebook['cells']:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = None
    return notebook

def process_notebook(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    notebook = remove_outputs(notebook)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_notebook.ipynb> <output_notebook.ipynb>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    process_notebook(input_path, output_path)
    print(f"Outputs removed. Notebook saved to {output_path}")
