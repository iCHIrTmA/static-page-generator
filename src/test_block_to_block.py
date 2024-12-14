import unittest

from markdown_to_blocks import *
from block_to_block_type import *


class TestBlockToBlockType(unittest.TestCase):
    def test_get_block_type(self):
        block_list = {
            "heading": "# This is a heading",
            "paragraph": "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "code": "```php code here ```",
            "quote": "> here is an instruction to quote",
            "unordered_list": """* This is the first list item in a list block
                                 * This is a list item
                                 * This is another list item""",
            "ordered_list": """1. first item
                               2. second item
                               3. final item"""
        }

        for block_type, block_text in block_list.items():
            self.assertTrue(block_type == block_to_block_type(block_text))

