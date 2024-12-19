import unittest

from extract_text import *

class TestExtractText(unittest.TestCase):
    def test_extract_heading_1(self):
        md_text = """
# This is the heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        title = extract_title(md_text)


        self.assertEqual(title, "This is the heading")

    def test_extract_heading_2(self):
        md_text = """
This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# This is the heading
"""
        title = extract_title(md_text)


        self.assertEqual(title, "This is the heading")

    def test_extract_heading_3(self):
        md_text = """

#### This is the heading
"""
        title = extract_title(md_text)


        self.assertEqual(title, "This is the heading")
