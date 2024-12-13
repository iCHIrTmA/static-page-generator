import unittest

from split_nodes_delimiter import *
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_normal_text(self):
        orig_text_node = TextNode("This is a text node in normal", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)

        expected = [
                TextNode(text="This is a text node in normal", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes, expected)

    def test_split_bold_text(self):
        orig_text_node = TextNode("This is a **text in bold** see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]
        # self.assertCountEqual(text_nodes, expected)
        # print("test_split_bold_text", text_nodes)
        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_split_bold_and_italic_text(self):
        orig_text_node = TextNode("This is a **text in bold**, while *this is in italic*, see?", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=", while ", text_type=TextType.TEXT),
                TextNode(text="this is in italic", text_type=TextType.ITALIC),
                TextNode(text=", see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes[0], expected[0])
        self.assertEqual(nodes[1], expected[1])
        self.assertEqual(nodes[2], expected[2])
        self.assertEqual(nodes[3], expected[3])
        self.assertEqual(nodes[4], expected[4])

    def test_italic_text(self):
        orig_text_node = TextNode("This is an *italic text* see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="*", text_type=TextType.ITALIC)
        expected = [
                TextNode(text="This is an ", text_type=TextType.TEXT),
                TextNode(text="italic text", text_type=TextType.ITALIC),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_code_text(self):
        orig_text_node = TextNode("This is a `code snippet` see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="`", text_type=TextType.CODE)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="code snippet", text_type=TextType.CODE),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_split_bold_italic_and_code_text(self):
        orig_text_node = TextNode("This is a **text in bold**, while *this is in italic*, and `this for code;`, see?", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=", while ", text_type=TextType.TEXT),
                TextNode(text="this is in italic", text_type=TextType.ITALIC),
                TextNode(text=", and ", text_type=TextType.TEXT),
                TextNode(text="this for code;", text_type=TextType.CODE),
                TextNode(text=", see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes[0], expected[0])
        self.assertEqual(nodes[1], expected[1])
        self.assertEqual(nodes[2], expected[2])
        self.assertEqual(nodes[3], expected[3])
        self.assertEqual(nodes[4], expected[4])
