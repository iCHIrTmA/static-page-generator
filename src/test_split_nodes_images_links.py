import unittest

from split_nodes_images_links import *
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

    def test_split_links_with_no_links_returns_only_raw_text_nodes(self):
        orig_text_node = TextNode("This is text with no links", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no links", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)

    def test_split_links_with_no_images_returns_only_raw_text_nodes(self):
        orig_text_node = TextNode("This is text with no images", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no images", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)

    # def test_split_links_of_text_with_only_images_and_raw_text_only_returns_raw_text_nodes(self):
    #     orig_text_node = TextNode("This is text with an ![boot dev mascot image](https://www.boot.dev/mascot-image.png) and also a ![random photo](https://www.boot.dev/random-image-generated.png)", TextType.TEXT)
        
    #     with self.assertRaises(Exception) as context:
    #         text_nodes = split_nodes_link(old_nodes=[orig_text_node])
    #     # expected = [
    #     #     TextNode("This is text with an ", TextType.TEXT),
    #     #     TextNode(" and also a ", TextType.TEXT),
    #     # ]

    #     # self.assertRaises("Only TextNode with type link is allowed")
    #     self.assertTrue('Only TextNode with type link is allowed' in str(context.exception))

