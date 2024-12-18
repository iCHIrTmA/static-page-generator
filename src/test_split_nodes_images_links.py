import unittest

from split_nodes_images_links import *
from inline_markdown import *
from textnode import TextType, TextNode


class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_split_links(self):
        orig_text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]

        for node in text_nodes:
            self.assertIn(node, expected)

    def test_split_images(self):
        orig_text_node = TextNode("This is text with an ![boot dev mascot image](https://www.boot.dev/mascot-image.png) and also a ![random photo](https://www.boot.dev/random-image-generated.png)", TextType.TEXT)
        text_nodes = split_nodes_image(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("boot dev mascot image", TextType.IMAGE, "https://www.boot.dev/mascot-image.png"),
            TextNode(" and also a ", TextType.TEXT),
            TextNode("random photo", TextType.IMAGE, "https://www.boot.dev/random-image-generated.png")
        ]

        for node in text_nodes:
            self.assertIn(node, expected)

    def test_split_links_with_no_links_returns_original_text_nodes(self):
        orig_text_node = TextNode("This is text with no links", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no links", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)

    def test_split_nodes_image_with_no_images_returns_original_text_nodes(self):
        orig_text_node = TextNode("This is text with no images", TextType.TEXT)
        text_nodes = split_nodes_image(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no images", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)
    def test_split_links_then_images(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_link(old_nodes=[orig_text_node])
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is **text** with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_links_and_images', nodes)

        for node in nodes:
            self.assertIn(node, expected)

    def test_split_images_then_links(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_image(old_nodes=[orig_text_node])
        nodes = split_nodes_link(old_nodes=nodes)

        expected = [
            TextNode("This is **text** with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_images_then_links', nodes)

        for node in nodes:
            self.assertIn(node, expected)

    def test_split_delimiter_then_images_no_split_link_returns_orig_link_as_text_nodes(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            # TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT),
            # TextNode(" and ", TextType.TEXT),
            # TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_delimiter_then_images', nodes)

        for node in expected:
            self.assertIn(node, nodes)

    def test_split_delimiter_then_link_then_images_returns_proper_text_nodes(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_link(old_nodes=nodes)
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_delimiter_then_link_then_images', nodes)

        for node in expected:
            self.assertIn(node, nodes)

