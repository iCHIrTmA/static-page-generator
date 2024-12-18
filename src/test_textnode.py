import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a URL node", TextType.ITALIC, "http://wwww.google.com")
        node2 = TextNode("This is a URL node", TextType.ITALIC, "http://wwww.google.com")
        self.assertEqual(node, node2)

    def test_eq_explicit_none_url(self):
        node = TextNode("This is a URL node", TextType.ITALIC, None)
        node2 = TextNode("This is a URL node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a URL node", TextType.ITALIC, "http://wwww.someurl.com")
        self.assertNotEqual(node, node3)

    def test_eq_text_type(self):
        image_node = TextNode("This is a node", TextType.IMAGE)
        code_node = TextNode("This is a node", TextType.CODE)
        self.assertNotEqual(image_node, code_node)

        code_node_2 = TextNode("This is a node", TextType.CODE)
        self.assertEqual(code_node, code_node_2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal_text(self):
        text_node = TextNode("This is a text node in normal", TextType.TEXT)
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag=None, value="This is a text node in normal")

        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "This is a text node in normal")

    def test_bold_text(self):
        text_node = TextNode("This is a text node in bold", TextType.BOLD)
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag='b', value="This is a text node in bold")

        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "<b>This is a text node in bold</b>")

    def test_italic_text(self):
        text_node = TextNode("This is a text node in italic", TextType.ITALIC)
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag='i', value="This is a text node in italic")

        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "<i>This is a text node in italic</i>")

    def test_code_text(self):
        text_node = TextNode("This is a text node in code", TextType.CODE)
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag='code', value="This is a text node in code")

        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "<code>This is a text node in code</code>")

    def test_link_text(self):
        text_node = TextNode("This is a text node as link", TextType.LINK, url="https://www.boot.dev")
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag='a', value="This is a text node as link", props={"href": text_node.url})

        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "<a href=\"https://www.boot.dev\">This is a text node as link</a>")

    def test_image(self):
        text_node = TextNode(text='', text_type=TextType.IMAGE, url="https://www.boot.dev.mascot.png")
        actual_leaf_node = text_node_to_html_node(text_node)
        expected_leaf_node = LeafNode(tag='img', value='', props={"src": text_node.url, "alt": "image description"})
        # return LeafNode(tag='img', value='', props={"src": text_node.url, "alt": "image description"})


        self.assertEqual(actual_leaf_node, expected_leaf_node)
        self.assertEqual(actual_leaf_node.to_html(), "<img alt=\"image description\" src=\"https://www.boot.dev.mascot.png\"></img>")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
