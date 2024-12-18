import unittest

from main import text_node_to_html_node
from textnode import TextType, TextNode
from leafnode import LeafNode


# class TestTextToLeafNode(unittest.TestCase):
    # def test_normal_text(self):
    #     text_node = TextNode("This is a text node in normal", TextType.TEXT)
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag=None, value="This is a text node in normal")

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "This is a text node in normal")

    # def test_bold_text(self):
    #     text_node = TextNode("This is a text node in bold", TextType.BOLD)
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag='b', value="This is a text node in bold")

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "<b>This is a text node in bold</b>")

    # def test_italic_text(self):
    #     text_node = TextNode("This is a text node in italic", TextType.ITALIC)
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag='i', value="This is a text node in italic")

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "<i>This is a text node in italic</i>")

    # def test_code_text(self):
    #     text_node = TextNode("This is a text node in code", TextType.CODE)
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag='code', value="This is a text node in code")

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "<code>This is a text node in code</code>")

    # def test_link_text(self):
    #     text_node = TextNode("This is a text node as link", TextType.LINK, url="https://www.boot.dev")
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag='a', value="This is a text node as link", props={"href": text_node.url})

    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "<a href=\"https://www.boot.dev\">This is a text node as link</a>")

    # def test_image(self):
    #     text_node = TextNode(text='', text_type=TextType.IMAGE, url="https://www.boot.dev.mascot.png")
    #     actual_leaf_node = text_node_to_html_node(text_node)
    #     expected_leaf_node = LeafNode(tag='img', value='', props={"src": text_node.url, "alt": "image description"})
    #     # return LeafNode(tag='img', value='', props={"src": text_node.url, "alt": "image description"})


    #     self.assertEqual(actual_leaf_node, expected_leaf_node)
    #     self.assertEqual(actual_leaf_node.to_html(), "<img alt=\"image description\" src=\"https://www.boot.dev.mascot.png\"></img>")

if __name__ == "__main__":
    unittest.main()
