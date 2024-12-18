import unittest

from inline_markdown import *
from textnode import TextType, TextNode
from text_to_textnodes import *


class TestTextToTextNode(unittest.TestCase):
    def test_raw_text(self):
        raw_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(raw_text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        # print('test_raw_text', text_nodes)

        for node in expected:
            self.assertIn(node, text_nodes)

    def test_raw_text_image_and_links_first_variation_1(self):
        raw_text = "Here is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev). And here, is **a bold text** with an *italic* word and a `code block`."
        text_nodes = text_to_textnodes(raw_text)
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(". And here, is ", TextType.TEXT),
            TextNode("a bold text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]

        # print('test_raw_text_image_and_links_first_variation_1', text_nodes)

        for node in expected:
            self.assertIn(node, text_nodes)
        
    def test_raw_text_links_and_image_first_variation_2(self):
        raw_text = "Here are some links: [first link](https://boot.dev), [second link](https://frontendmasters.io), and a ![random image](https://random-image.net/some-img.jpeg). This is a `php code block php`, *an italic text*, and lastly, **a bold**."
        text_nodes = text_to_textnodes(raw_text)

        expected = [
            TextNode("Here are some links: ", TextType.TEXT),
            TextNode("first link", TextType.LINK, "https://boot.dev"),
            TextNode(", ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://frontendmasters.io"),
            TextNode(", and a ", TextType.TEXT),
            TextNode("random image", TextType.IMAGE, "https://random-image.net/some-img.jpeg"),
            TextNode(". This is a ", TextType.TEXT),
            TextNode("php code block php", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("an italic text", TextType.ITALIC),
            TextNode(", and lastly, ", TextType.TEXT),
            TextNode("a bold", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]

        # print('test_raw_text_links_and_image_first_variation_2', text_nodes)

        for node in expected:
            self.assertIn(node, text_nodes)
