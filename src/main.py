from textnode import TextType, TextNode
from init_public_assets import *

def main():
    node = TextNode('hello world', TextType.ITALIC, 'https://scinai.fly.dev')
    init_public_assets()
main()
