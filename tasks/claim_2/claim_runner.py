# tasks/claim_2/claim_runner.py

from prompts.claim_2_prompt_template import build_zero_shot_prompt, build_few_shot_prompt, build_cot_prompt
from models.base_model import BaseModel


def run_claim_task(input: str, table: str, model: BaseModel, shots="", **kwargs) -> str:
    if shots == "fewshot":  # few-shot
        prompt = build_few_shot_prompt(input, table)
    elif shots == "zeroshot":  # zero-shot
        prompt = build_zero_shot_prompt(input, table)
    elif shots == "cot":
        prompt = build_cot_prompt(input, table)
    return model.call(prompt)