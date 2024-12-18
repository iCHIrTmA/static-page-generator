block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block) -> str:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

# def block_to_block_type(block:str) -> str:
#     heading_regex = re.compile("^#{1,6} .+")
#     match block:
#         case block if heading_regex.match(block):
#             return 'heading'
#         case block if block.startswith("```") and block.endswith("```"):
#           return 'code'
#         case block if block.startswith(">"):
#           return 'quote'
#         case block if is_unordered_list(block):
#           return 'unordered_list'
#         case block if is_ordered_list(block):
#           return 'ordered_list'
#         case _:
#           return 'paragraph'
       
# def is_unordered_list(block: str) -> bool:
#     items = block.split("\n")
#     items = [item.strip() for item in items]

#     return all((item.startswith("* ") or item.startswith("- ")) for item in items)

# def is_ordered_list(block: str) -> bool:
#     items = block.split("\n")
#     items = [item.strip() for item in items]
#     ordered_item_regex = re.compile("^\d+\. ")

#     return all(ordered_item_regex.match(item) for item in items)


