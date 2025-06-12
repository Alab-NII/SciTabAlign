# utils
import re

def extract_answer(text):
    match = re.search(r"<ans>(.*?)</ans>", text, re.DOTALL)
    return match.group(1).strip() if match else ""


def format_cells(list_of_lists):
    # Minor -1 for row index (The row in our ground truth index need to be -1. Because the header is row 0.)
    list_of_lists_2 = [[row - 1, col] for row, col in list_of_lists]
    # Convert to list of tuple 
    return [tuple(pair) for pair in list_of_lists_2]


def format_table_as_markdown(table_column_names, table_content_values):
    table_content_values = [[str(element) for element in row] for row in table_content_values]
    # Header
    header = "| " + " | ".join(table_column_names) + " |"
    
    # Rows
    rows = [
        "| " + " | ".join(row) + " |"
        for row in table_content_values
    ]

    # Combine all parts
    markdown_table = "\n".join([header] + rows)
    return markdown_table


def format_table_as_pipe_tag(table_column_names, table_content_values):
    """
    """
    # Convert all elements to strings
    table_content_values = [[str(element) for element in row] for row in table_content_values]
    #
    # Start with the column header line
    output_lines = ["col : " + " | ".join(table_column_names)]
    #
    # Add each row with row number
    for idx, row in enumerate(table_content_values, 1):
        output_lines.append(f"row {idx} : " + " | ".join(row))
    #
    # Join all lines into a single string
    return "\n".join(output_lines)


def format_caption_and_table(table_column_names, table_content_values, caption, type_="pipe_tagging"):
    if type_ == "markdown":
        table = format_table_as_markdown(table_column_names, table_content_values)
    if type_ == "pipe_tagging":
        table = format_table_as_pipe_tag(table_column_names, table_content_values)
    return f"Caption: {caption}\n\nTable:\n{table}\n"