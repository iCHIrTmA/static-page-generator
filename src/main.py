from textnode import TextType, TextNode
from leafnode import LeafNode

def main():
    node = TextNode('hello world', TextType.ITALIC, 'https://scinai.fly.dev')
    # print(node)

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text_type = text_node.text_type

    if text_type.value not in [member.value for member in TextType]:
        raise Exception("invalid text type")
    if text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    if text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    if text_type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    if text_type == TextType.LINK:
        return LeafNode(tag='a', value=text_node.text, props={"href": text_node.url})
    if text_type == TextType.IMAGE:
        return LeafNode(tag='img', value='', props={"alt": "image description", "src": text_node.url})

main()