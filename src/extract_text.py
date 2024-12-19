from markdown_blocks import *

def extract_title(markdown:str) -> str:
    blocks = markdown_to_blocks(markdown)
    # print(blocks)

    heading_block = next(filter(lambda block: block_to_block_type(block) == block_type_heading, blocks), None)

    heading = heading_block.split("# ")[-1]
    heading = heading.strip()

    # print("extract_title", heading)
    return heading