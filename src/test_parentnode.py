import unittest

from parentnode import *
from leafnode import *


class TestParentNode(unittest.TestCase):
    def test_eq_basic(self):
        node = ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ])

        node2 = ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ])

        self.assertEqual(node, node2)

    def test_eq_full(self):
        node = ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ],
                props={"class": "mt-2 px-4", "type": "submit"})

        node2 = ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ],
                props={"class": "mt-2 px-4", "type": "submit"})

        self.assertEqual(node, node2)

    def test_to_html(self):
        node = ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ],
                props={"class": "mt-2 px-4", "type": "submit"})

        self.assertEqual(node.to_html(), "<p class=\"mt-2 px-4\" type=\"submit\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    