import unittest

from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_eq_basic(self):
        node = LeafNode("p", "hello world")
        node2 = LeafNode("p", "hello world")
        self.assertEqual(node, node2)

    def test_eq_full(self):
        node = LeafNode(tag="div", value="hello world", props={"class": "mt-2 px-4", "action": "/save-url"})
        node2 = LeafNode(tag="div", value="hello world", props={"class": "mt-2 px-4", "action": "/save-url"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode(tag="div", value="some title", props={"class": "mt-2 px-4", "action": "/save-url"})
        self.assertEqual(node.to_html(), "<div class=\"mt-2 px-4\" action=\"/save-url\">some title</div>")

if __name__ == "__main__":
    unittest.main()
