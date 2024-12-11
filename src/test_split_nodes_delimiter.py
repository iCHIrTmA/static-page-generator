import unittest

from split_nodes_delimiter import *
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    # def test_normal_text(self):
    #     text_node = TextNode("This is a text node in normal", TextType.NORMAL)
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag=None, value="This is a text node in normal")

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "This is a text node in normal")

    def test_bold_text(self):
        orig_text_node = TextNode("This is a **text in bold** see?", TextType.NORMAL)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        expected = [
                TextNode(text="This is a ", text_type=TextType.NORMAL),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=" see?", text_type=TextType.NORMAL),
            ]
        # self.assertCountEqual(text_nodes, expected)
        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_italic_text(self):
        orig_text_node = TextNode("This is an *italic text* see?", TextType.NORMAL)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="*", text_type=TextType.ITALIC)
        expected = [
                TextNode(text="This is an ", text_type=TextType.NORMAL),
                TextNode(text="italic text", text_type=TextType.ITALIC),
                TextNode(text=" see?", text_type=TextType.NORMAL),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_code_text(self):
        orig_text_node = TextNode("This is a `code snippet` see?", TextType.NORMAL)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="`", text_type=TextType.CODE)
        expected = [
                TextNode(text="This is a ", text_type=TextType.NORMAL),
                TextNode(text="code snippet", text_type=TextType.CODE),
                TextNode(text=" see?", text_type=TextType.NORMAL),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

if __name__ == "__main__":
    unittest.main()
