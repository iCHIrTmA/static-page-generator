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
        self.assertEqual(node.props_to_html(), " class=\"mt-2 px-4\" action=\"/save-url\"")

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag: p, value: What a strange world, children: None, props: {'class': 'primary'})",
        )

