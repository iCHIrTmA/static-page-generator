from textnode import TextType, TextNode

def markdown_to_blocks(md_text:str) -> list:
    orig_blocks = md_text.split("\n")

    blocks = []
    for orig_block in orig_blocks:
        if orig_block == "":
            continue

        blocks.append(orig_block.strip())

    blocks = list(filter(None, blocks))

    return blocks
