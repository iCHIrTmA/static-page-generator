from textnode import TextType, TextNode
from inline_markdown import *
from split_nodes_images_links import *
from inline_markdown import *

def text_to_textnodes(text:str) -> list:
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="**", text_type=TextType.BOLD)
    nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
    nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)

    return nodes

