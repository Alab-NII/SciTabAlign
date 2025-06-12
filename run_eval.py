import json
import sys
import ast
from evaluation.eval_claim import evaluate_claim_verification, evaluate_evidence_cell

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_prediction(label):
    if not label or "row" in label or "-" in label:
        return []
    try:
        return ast.literal_eval(label)
    except (SyntaxError, ValueError):
        return []

def parse_ground_truth(label):
    if isinstance(label, str):
        try:
            return ast.literal_eval(label)
        except (SyntaxError, ValueError):
            return []
    return label

def evaluate_claim_task(models, prompt_types, base_path):
    print("Running Claim Verification Task Evaluation")
    for prompt_type in prompt_types:
        print(f"\nPrompt type: {prompt_type}")
        for model_name in models:
            input_path = f"{base_path}/claim_task/pipe_tagging/{model_name}_{prompt_type}.json"
            data = load_json(input_path)

            predictions = [item["pred_label"] for item in data]
            ground_truth = [item["label"] for item in data]

            scores = evaluate_claim_verification(predictions, ground_truth)
            print(scores["macro_f1"])

def evaluate_evi_task(models, prompt_types, base_path):
    print("Running Evidence Cell Retrieval Task Evaluation")
    for prompt_type in prompt_types:
        print(f"\nPrompt type: {prompt_type}")
        for model_name in models:
            input_path = f"{base_path}/evi_task/pipe_tagging/{model_name}_{prompt_type}.json"
            data = load_json(input_path)

            predictions = [parse_prediction(item.get("pred_label", "")) for item in data]
            ground_truth = [parse_ground_truth(item.get("label_cells", [])) for item in data]

            scores = evaluate_evidence_cell(predictions, ground_truth)
            print(scores["macro_f1"])

def main():
    task_type = sys.argv[1]  # claim_task / evi_task
    models = ["llama-3.1-8b", "llama-3.1-70b", "qwen-2.5-7b", "qwen-2.5-72b", "gpt-4o"]
    prompt_types = ["zeroshot", "fewshot", "cot"]
    base_path = "outputs"

    if task_type == "claim_task":
        evaluate_claim_task(models, prompt_types, base_path)
    elif task_type == "evi_task":
        evaluate_evi_task(models, prompt_types, base_path)
    else:
        print(f"Unknown task type: {task_type}")

if __name__ == "__main__":
    main()
