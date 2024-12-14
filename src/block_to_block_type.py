import re

def block_to_block_type(block:str) -> str:
    heading_regex = re.compile("^#{1,6} .+")
    match block:
        case block if heading_regex.match(block):
            return 'heading'
        case block if block.startswith("```") and block.endswith("```"):
          return 'code'
        case block if block.startswith(">"):
          return 'quote'
        case block if is_unordered_list(block):
          return 'unordered_list'
        case block if is_ordered_list(block):
          return 'ordered_list'
        case _:
          return 'paragraph'
        # print("Number not between 1 and 3")

# def all_lines_start_with(block: str) -> bool:
#    lines = block.split()
#    return all((line.startswith("* ") or line.startswith("- ")) for line in lines)

def is_unordered_list(block: str) -> bool:
    items = block.split("\n")
    items = [item.strip() for item in items]

    return all(item.startswith("* ") for item in items)

def is_ordered_list(block: str) -> bool:
    items = block.split("\n")
    items = [item.strip() for item in items]
    ordered_item_regex = re.compile("^\d+\. ")

    return all(ordered_item_regex.match(item) for item in items)



