import re

def extract_images(raw_text:str) -> list:
    img_texts = re.findall(r"(?<=!\[)(.*?)(?=\])", raw_text)
    img_urls = re.findall(r"\((.*?)\)", raw_text)

    images = list(zip(img_texts, img_urls))

    return images

def extract_links(raw_text:str) -> list:
    anchor_tags = re.findall(r"(?<!!)\[(.*?)\]", raw_text)
    urls = re.findall(r"\((.*?)\)", raw_text)

    links = list(zip(anchor_tags, urls))

    return links
