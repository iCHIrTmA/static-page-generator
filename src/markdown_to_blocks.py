import re

def markdown_to_blocks(md_text:str) -> list:
    orig_blocks = md_text.split("\n\n")

    # print("markdown_to_blocks_before", orig_blocks)
    ordered_item_regex = re.compile("^\d+\. ")

    blocks = []
    for orig_block in orig_blocks:
        if orig_block == "":
            continue
        
        block = orig_block.strip()

        # block is either unordered or ordered list
        if block.startswith("- ") or block.startswith("* ") or ordered_item_regex.match(block):
            # print('list block', block)
            list_block = block
            items = list_block.split("\n")
            items = [item.strip() for item in items]

            # print('list items', items)
            block = "\n".join(items)
    
        blocks.append(block)

    blocks = list(filter(None, blocks))

    # print("markdown_to_blocks_after", blocks)

    return blocks
