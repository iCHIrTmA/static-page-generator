from textnode import TextType, TextNode
from extract_markdown_content import *
import re

def split_nodes_image(old_nodes:list) -> list:
    image_nodes = []
    raw_text_nodes = []

    for old_node in old_nodes:
        images = extract_images(old_node.text)
        for image in images:
            # print('alt_text:', image[0], 'img_src:', image[1])
            image_nodes.append(TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1]))

        raw_texts = extract_raw_texts(text=old_node.text, exclude_list=image_nodes)
        for raw_text in raw_texts:
            raw_text_nodes.append(TextNode(text=raw_text, text_type=TextType.TEXT))

    return [*image_nodes, *raw_text_nodes]

def split_nodes_link(old_nodes:list) -> list:
    link_nodes = []
    raw_text_nodes = []

    for old_node in old_nodes:
        links = extract_links(old_node.text)
        for link in links:
            # print('anchor_tag:', link[0], 'url:', link[1])
            link_nodes.append(TextNode(text=link[0], text_type=TextType.LINK, url=link[1]))

        raw_texts = extract_raw_texts(text=old_node.text, exclude_list=link_nodes)
        for raw_text in raw_texts:
            raw_text_nodes.append(TextNode(text=raw_text, text_type=TextType.TEXT))

    return [*link_nodes, *raw_text_nodes]

def extract_raw_texts(text:str, exclude_list: list) -> list:
    if not exclude_list:
        return [text]

    except_strings = []

    for node in exclude_list:
        if node.text_type == TextType.LINK:
            except_strings.append(f"[{node.text}]({node.url})") 
        if node.text_type == TextType.IMAGE:
            except_strings.append(f"![{node.text}]({node.url})")

    # Create a regex pattern to match any of the substrings to exclude
    pattern = '|'.join(map(re.escape, except_strings))
    # Split the text by the pattern
    parts = re.split(pattern, text)
    # Filter out empty strings
    raw_texts = [part for part in parts if part]

    return raw_texts