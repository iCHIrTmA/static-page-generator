from textnode import TextType, TextNode

def main():
    node = TextNode('hello world', TextType.ITALIC, 'https://scinai.fly.dev')
    print(node)

main()