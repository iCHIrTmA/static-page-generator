from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes:list, delimiter:str, text_type:TextType) -> list:
    nodes = []

    for old_node in old_nodes:
        str_list = old_node.text.split(delimiter)
        for key, value in enumerate(str_list):
            if key == 1:
                node = TextNode(value, text_type)
                nodes.append(node)
            else:
                text_node = TextNode(value, TextType.NORMAL)
                nodes.append(text_node)

    return nodes
