import os
import sys
import json
from tqdm import tqdm
from tasks.evi_select.evi_runner import run_evi_task
# from models.openai import OpenAIModel
from models.llama import LlamaModel
from models.qwen import QwenModel
from utils import format_caption_and_table, extract_answer, format_cells


model_name = "qwen-2.5-7b" 
prompt_type = "zeroshot"
table_format = "pipe_tagging"

# ["qwen-2.5-7b", "qwen-2.5-72b", "llama-3.1-8b", "llama-3.1-70b"]

model_registry = {
    # "qwen-2.5-72b": lambda: QwenModel(model_name="Qwen2.5-72B"),
    "qwen-2.5-7b": lambda: QwenModel(model_name="Qwen2.5-7B"),
    # "llama-3.1-70b": lambda: LlamaModel(model_name="Llama-3.1-70B"),
    # "llama-3.1-8b": lambda: LlamaModel(model_name="Llama-3.1-8B")
}

model = model_registry[model_name]()

OUTPUT_DIR = f"outputs/evi_task/{table_format}"
os.makedirs(OUTPUT_DIR, exist_ok=True)


kwargs = {
    "temperature": 0,
    "max_tokens": 1024
}

dataset_file = "data/data_100.json"
with open(dataset_file, "r", encoding="utf-8") as f:
    samples = json.load(f)
    # samples = samples[0:5]

results = []
for item in tqdm(samples):
    # print(item["id"])
    table = format_caption_and_table(item["table_column_names"], item["table_content_values"], item["table_caption"], type_=table_format)
    prompt, response = run_evi_task(item["claim"], table, model, shots=prompt_type, **kwargs)
    #
    results.append({
        "id": item["id"],
        "claim": item["claim"],
        "label_cells": str(format_cells(item["explanation_cells"])),    
        "pred_label": extract_answer(response),
        "generated_response": response,
        "paper_id": item["paper_id"],
        "table_id": item["table_id"],
        "user_prompt": prompt
    })

output_path = os.path.join(
    OUTPUT_DIR, f"{model_name.lower()}_{prompt_type}.json")

print(f"Saving output to: {output_path}")
with open(output_path, "w", encoding="utf-8") as out_f:
    json.dump(results, out_f, indent=2, ensure_ascii=False)