import unittest

from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_basic_blocks(self):
        md_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(md_text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        # print("test_basic_convert", blocks)

        for block in expected:
            self.assertIn(block, blocks)
        # self.assertEqual(blocks, expected)

    def test_blocks_w_empty_blocks_var_1(self):
        md_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item


"""
        blocks = markdown_to_blocks(md_text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        # print("test_blocks_w_empty_blocks", {"md_text": md_text}, {"blocks": blocks})

        for block in expected:
            self.assertIn(block, blocks)

    def test_blocks_numbered_list_variation_2(self):
        md_text = """
1. This is the first list item in a list block
2. This is a list item
3. This is another list item

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#### Small heading
"""
        blocks = markdown_to_blocks(md_text)
        expected = [
            "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "#### Small heading"
        ]

        # print("test_basic_convert", blocks)

        for block in expected:
            self.assertIn(block, blocks)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
