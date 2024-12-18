from textnode import TextType, TextNode
from inline_markdown import *

def split_nodes_image(old_nodes:list) -> list:
    nodes = []

    for orig_node in old_nodes:
        images = extract_images(orig_node.text)
        # if no images in the current node do not change
        if not images:
            # text_node = TextNode(text=old_node.text, text_type=old_node.text_type, url=old_node.url)
            nodes.append(orig_node)
            continue

        text_to_search = None
        for image in images:
            # print('image', image)
            if not text_to_search:
                sections = orig_node.text.split(f"![{image[0]}]({image[1]})", 1)
            if text_to_search:
                sections = text_to_search.split(f"![{image[0]}]({image[1]})", 1)

            # create node for the first half (searched part) of the section
            text_node = TextNode(sections[0], TextType.TEXT)
            nodes.append(text_node)

            # create node for the image found in the searched part of the text
            image_node = TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1])
            nodes.append(image_node)

            # store second half (unsearched part) to a variable to be searched for images in the next iteration
            text_to_search = sections[1]

        # create node for unsearched text if existing and if all images have been extracted
        if text_to_search:
            nodes.append(TextNode(text_to_search, TextType.TEXT))

    # print("split_nodes_image", nodes)

    return nodes

def split_nodes_link(old_nodes:list) -> list:
    nodes = []

    for orig_node in old_nodes:
        links = extract_links(orig_node.text)
        # print("split_nodes_link", links)
        if not links:
            nodes.append(orig_node)
            continue

        text_to_search = None
        for link in links:
            if not text_to_search:
                sections = orig_node.text.split(f"[{link[0]}]({link[1]})", 1)
            if text_to_search:
                sections = text_to_search.split(f"[{link[0]}]({link[1]})", 1)


            # Create node for the searched part of the section
            nodes.append(TextNode(sections[0], TextType.TEXT))

            # Create node for the link found
            nodes.append(TextNode(text=link[0], text_type=TextType.LINK, url=link[1]))
            
            # Store unsearched part of the section to a variable be searched in the next iteration
            text_to_search = sections[1]

        # Create node for the unsearched text if all links have been found
        if text_to_search:
            nodes.append(TextNode(text_to_search, TextType.TEXT))

    return nodes
