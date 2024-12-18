import unittest

from inline_markdown import *
from textnode import TextType, TextNode


class TestInlineMarkdown(unittest.TestCase):
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

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

