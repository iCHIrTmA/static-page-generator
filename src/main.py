from textnode import TextType, TextNode
from init_public_assets import *
from generate_page import *
from generate_pages_recursive import *

def main():
    # node = TextNode('hello world', TextType.ITALIC, 'https://scinai.fly.dev')
    init_public_assets()
    # generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_pages_recursive('content/', 'template.html', 'public/')

main()
