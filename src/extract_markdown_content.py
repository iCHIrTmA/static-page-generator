import re

def extract_images(text:str) -> list:
    # img_texts = re.findall(r"(?<=!\[)(.*?)(?=\])", raw_text)
    # img_texts = re.findall(r"(?<=!\[)(.*?)(?=\])", raw_text)
    # img_urls = re.findall(r"\((.*?)\)", raw_text)

    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # print(imgs)

    # images = list(zip(img_texts, img_urls))

    return images

def extract_links(text:str) -> list:
    # anchor_tags = re.findall(r"(?<!!)\[(.*?)\]", raw_text)
    # urls = re.findall(r"\((.*?)\)", raw_text)
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # print(links)

    # links = list(zip(anchor_tags, urls))

    return links