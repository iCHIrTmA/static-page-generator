import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
