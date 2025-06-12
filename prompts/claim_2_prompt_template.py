# prompts/claim_2_prompt_template.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import format_caption_and_table
import json

def build_zero_shot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, determine whether the claim is Supported or Refuted based on the information in the table.
        {table}
        Claim: {claim} 
        Please respond with one of the following labels: Supported or Refuted.
        Please format your final answer within brackets as follows: 
		"<ans> YOUR ANSWER </ans>"
		"""
    return prompt


def format_examples(examples, cot=False):
    formatted_examples = []
    #
    for idx, example in enumerate(examples, start=1):
        # Extracting values from the dictionary
        claim = example.get("claim")
        label = example.get("label")
        table_caption = example.get("table_caption")
        table_column_names = example.get("table_column_names")
        table_content_values = example.get("table_content_values")
        explanation_cot = example.get("explanation_cot")
        #
        table = format_caption_and_table(table_column_names, table_content_values, table_caption)
        # Formatting the example
        formatted_example = f"### Example {idx}:\n"
        formatted_example += f"  * {table}\n"
        formatted_example += f"  * Claim: {claim}\n"
        formatted_example += f"  * Label: <ans> {label} </ans>\n"
        if cot == True:
            formatted_example += f"  * Explanation: {explanation_cot}\n"
        #
        formatted_examples.append(formatted_example)
    #
    return "\n".join(formatted_examples)


with open("data/demonstrations_use.json", "r", encoding="utf-8") as f:
    demonstrations = json.load(f)

examplar_format = format_examples(demonstrations)
examplar_format_cot = format_examples(demonstrations, cot=True)


def build_few_shot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, determine whether the claim is Supported or Refuted based on the information in the table.
        {table}
        Claim: {claim} 
        Please respond with one of the following labels: Supported or Refuted.
        Please format your final answer within brackets as follows: 
		"<ans> YOUR ANSWER </ans>"
		## Here are some examples:
		{examplar_format}
		"""
    return prompt
    

def build_cot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, determine whether the claim is Supported or Refuted based on the information in the table.
        {table}
        Claim: {claim} 
        Please respond with one of the following labels: Supported or Refuted.
        Please format your final answer within brackets as follows: 
		"<ans> YOUR ANSWER </ans>"
		## Here are some examples:
		{examplar_format_cot}
		"""
    return prompt

