from textnode import TextType, TextNode
from htmlnode import *
from markdown_blocks import *
from block_to_block_type import *

# def markdown_to_html_node(md_text:str) -> HTMLNode:
#     block_nodes = []

#     blocks = markdown_to_blocks(md_text)
#     # print("markdown_to_html_node", md_text)
#     # print("markdown_to_html_node", blocks)

#     for block in blocks:
#         block_type = block_to_block_type(block)

#         # print(block_type)

#         if block_type == 'heading':
#             inline_nodes = text_to_children(block, block_type)
#             heading_block = ParentNode(tag='h1', children=inline_nodes)
#             block_nodes.append(heading_block)
#         if block_type == 'paragraph':
#             inline_nodes = text_to_children(block)
#             paragraph_block = ParentNode('p', children=inline_nodes)
#             block_nodes.append(paragraph_block)
#         # if block_type == 'code':
#         #     node = HTMLNode('code', block)
#         # if block_type == 'quote':
#         #     node = HTMLNode('blockquote', block)
#         # if block_type == 'ordered_list':
#         #     inline_nodes = text_to_children(block, block_type)
#         #     list_block = ParentNode('ol', children=inline_nodes)
#         #     block_nodes.append(list_block)
#         if block_type == 'unordered_list':
#             inline_nodes = text_to_children(block, block_type)
#             list_block = ParentNode('ul', children=inline_nodes)
#             block_nodes.append(list_block)

#         # print(node)
#     # print(block_nodes)

#     return ParentNode(tag="div", children=block_nodes)

# def text_to_children(block_md_text:str, block_type:str=None) -> list:
#     text_nodes = text_to_textnodes(block_md_text)

#     print("text_to_children", text_nodes, block_md_text)
        
#     html_nodes = []

#     if block_type in ["ordered_list", "unordered_list"]:
#         for text_node in text_nodes:
#             if not text_node.text:
#                 continue
#             html_node = LeafNode(tag="li",value=text_node.text.strip())
#             html_nodes.append(html_node)

#         return html_nodes


#     for text_node in text_nodes:
#         if text_node.text_type:
#             html_node = LeafNode(tag=None,value=text_node.text)
#         if text_node.text_type == TextType.TEXT and block_type == "heading":
#             html_node = LeafNode(tag=None,value=text_node.text.strip("# "))
#         if text_node.text_type == TextType.BOLD:
#             html_node = LeafNode(tag="b",value=text_node.text)
#         if text_node.text_type == TextType.ITALIC:
#             html_node = LeafNode(tag="i",value=text_node.text)
#         if text_node.text_type == TextType.CODE:
#             html_node = LeafNode(tag="code",value=text_node.text)
#         if text_node.text_type == TextType.LINK:
#             html_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
#         if text_node.text_type == TextType.IMAGE:
#             html_node = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.url})

#         html_nodes.append(html_node)

#     return html_nodes
