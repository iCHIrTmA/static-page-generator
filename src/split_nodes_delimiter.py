from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes:list, delimiter:str, text_type:TextType) -> list:
    nodes = []
    for orig_node in old_nodes:
        text = orig_node.text
        if orig_node.text_type != TextType.TEXT:
            nodes.append(orig_node)
            continue

        str_list = text.split(delimiter)
        for key, value in enumerate(str_list):
            if key == 1:
                node = TextNode(value, text_type)
                nodes.append(node)
            else:
                non_target_node = TextNode(value, orig_node.text_type)
                nodes.append(non_target_node)

    return nodes
