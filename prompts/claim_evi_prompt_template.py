# prompts/claim_evi_prompt_template.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import format_caption_and_table
import json


def build_zero_shot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, identify the list of table cells that are necessary to determine the correct label for the claim.
        {table}
        Claim: {claim} 
        Please provide your answer as a list of tuples, where each tuple represents a cell's location in the format (row_index, column_index).
        * Use the row numbers as indicated in the table (e.g., row 1, row 2, etc.).
        * For the column index: 
            ** The column labeled "col" is column 0.
            ** The next column to the right is column 1, and so on.
        Format your final answer within <ans> tags, like this:
		"<ans> [(row_index_1, column_index_1), (row_index_2, column_index_2), ...] </ans>"
		"""
    return prompt


def format_cells(list_of_lists):
    # Minor -1 for row index (The row in our ground truth index need to be -1. Because the header is row 0.)
    list_of_lists_2 = [[row - 1, col] for row, col in list_of_lists]
    # Convert to list of tuple 
    return [tuple(pair) for pair in list_of_lists_2]


def format_examples(examples, cot=False):
    formatted_examples = []
    #
    for idx, example in enumerate(examples, start=1):
        # Extracting values from the dictionary
        claim = example.get("claim")
        # label = example.get("label")
        table_caption = example.get("table_caption")
        table_column_names = example.get("table_column_names")
        table_content_values = example.get("table_content_values")
        # explanation_cot = example.get("explanation_cot")
        explanation_cot_cells = example.get("explanation_cot_cells")
        #
        explanation_cells = example.get("explanation_cells")
        explanation_cells_format = format_cells(explanation_cells)
        #
        table = format_caption_and_table(table_column_names, table_content_values, table_caption)
        # Formatting the example
        formatted_example = f"### Example {idx}:\n"
        formatted_example += f"  * {table}\n"
        formatted_example += f"  * Claim: {claim}\n"
        formatted_example += f"  * Evidence Cells: <ans> {explanation_cells_format} </ans>\n"
        if cot == True:
            formatted_example += f"  * Explanation: {explanation_cot_cells}\n"
        #
        formatted_examples.append(formatted_example)
    #
    return "\n".join(formatted_examples)


with open("data/demonstrations_use.json", "r", encoding="utf-8") as f:
    demonstrations = json.load(f)

examplar_format = format_examples(demonstrations)
examplar_format_cot = format_examples(demonstrations, cot=True)

def build_few_shot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, identify the list of table cells that are necessary to determine the correct label for the claim.
        {table}
        Claim: {claim} 
        Please provide your answer as a list of tuples, where each tuple represents a cell's location in the format (row_index, column_index).
        * Use the row numbers as indicated in the table (e.g., row 1, row 2, etc.).
        * For the column index: 
            ** The column labeled "col" is column 0.
            ** The next column to the right is column 1, and so on.
        Format your final answer within <ans> tags, like this:
		"<ans> [(row_index_1, column_index_1), (row_index_2, column_index_2), ...] </ans>"
        ## Here are some examples:
		{examplar_format}
		"""
    return prompt
    

def build_cot_prompt(claim, table):
    prompt = f"""Given the table and the claim below, identify the list of table cells that are necessary to determine the correct label for the claim.
        {table}
        Claim: {claim} 
        Please provide your answer as a list of tuples, where each tuple represents a cell's location in the format (row_index, column_index).
        * Use the row numbers as indicated in the table (e.g., row 1, row 2, etc.).
        * For the column index: 
            ** The column labeled "col" is column 0.
            ** The next column to the right is column 1, and so on.
        Format your final answer within <ans> tags, like this:
		"<ans> [(row_index_1, column_index_1), (row_index_2, column_index_2), ...] </ans>"
        ## Here are some examples:
		{examplar_format_cot}
		"""
    return prompt