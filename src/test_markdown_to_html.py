import unittest
from markdown_blocks import *
from markdown_to_html_node import *

# class TestMarkdownToHtml(unittest.TestCase):
#     def test_markdown_to_html_node_basic(self):
#         md_text = """# This is a heading

#         This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#         * This is the first list item in a list block
#         * This is a list item
#         * This is another list item"""
#         html_root_node = markdown_to_html_node(md_text)

#         expected = [
#             ParentNode(tag="h1", children=[LeafNode(tag=None, value="This is a heading")]),
#             ParentNode(tag="p", children=[
#                 LeafNode(tag=None, value="This is a paragraph of text. It has some "),
#                 LeafNode(tag="b", value="bold"),
#                 LeafNode(tag=None, value=" and "),
#                 LeafNode(tag="i", value="italic"),
#                 LeafNode(tag=None, value=" words inside of it."),
#             ]),
#             ParentNode(tag="ul", children=[
#                 LeafNode(tag="li", value="This is the first list item in a list block"),
#                 LeafNode(tag="li", value="This is a list item"),
#                 LeafNode(tag="li", value="This is another list item"),
#             ]),
#         ]

#         for expected_node in expected:
#             self.assertIn(expected_node, html_root_node.children)

#     def test_paragraph(self):
#         md = """
#         This is **bolded** paragraph text in a p tag here

#             """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
#         )

#     def test_paragraphs(self):
#         md = """
#         This is **bolded** paragraph text in a p tag here

#         This is another paragraph with *italic* text and `code` here

#         """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

    # def test_lists(self):
    #     md = """
    #     - This is a list
    #     - with items
    #     - and *more* items

    #     """

    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     print("test_lists", html)
    #     self.assertEqual(
    #         html,
    #         "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
    #     )

    # def test_headings(self):
    #     md = """
    #     # this is an h1

    #     this is paragraph text

    #     ## this is an h2
    #     """

    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     self.assertEqual(
    #         html,
    #         "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
    #     )

    # def test_blockquote(self):
    #     md = """
    #         > This is a
    #         > blockquote block

    #         this is paragraph text

    #         """

    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     self.assertEqual(
    #         html,
    #         "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
    #     )

