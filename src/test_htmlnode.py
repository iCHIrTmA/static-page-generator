import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_basic(self):
        node = HTMLNode("p", "hello world")
        node2 = HTMLNode("p", "hello world")
        self.assertEqual(node, node2)

    def test_eq_full(self):
        child_node_1 = HTMLNode("p", "hello world")
        child_node_2 = HTMLNode("p", "my name iss...")
        node = HTMLNode(tag="div", children=[child_node_1, child_node_2], props={"class": "mt-2 px-4", "action": "/save-url"})
        node2 = HTMLNode(tag="div", children=[child_node_1, child_node_2], props={"class": "mt-2 px-4", "action": "/save-url"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "mt-2 px-4", "action": "/save-url"})
        self.assertEqual(node.props_to_html(), "class=\"mt-2 px-4\" action=\"/save-url\"")

if __name__ == "__main__":
    unittest.main()
