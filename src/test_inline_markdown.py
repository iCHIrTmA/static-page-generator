import unittest

from inline_markdown import *
from textnode import TextType, TextNode


class TestInlineMarkdown(unittest.TestCase):
    def test_normal_text(self):
        orig_text_node = TextNode("This is a text node in normal", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)

        expected = [
                TextNode(text="This is a text node in normal", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes, expected)

    def test_split_bold_text(self):
        orig_text_node = TextNode("This is a **text in bold** see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]
        # self.assertCountEqual(text_nodes, expected)
        # print("test_split_bold_text", text_nodes)
        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_split_bold_and_italic_text(self):
        orig_text_node = TextNode("This is a **text in bold**, while *this is in italic*, see?", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=", while ", text_type=TextType.TEXT),
                TextNode(text="this is in italic", text_type=TextType.ITALIC),
                TextNode(text=", see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes[0], expected[0])
        self.assertEqual(nodes[1], expected[1])
        self.assertEqual(nodes[2], expected[2])
        self.assertEqual(nodes[3], expected[3])
        self.assertEqual(nodes[4], expected[4])

    def test_italic_text(self):
        orig_text_node = TextNode("This is an *italic text* see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="*", text_type=TextType.ITALIC)
        expected = [
                TextNode(text="This is an ", text_type=TextType.TEXT),
                TextNode(text="italic text", text_type=TextType.ITALIC),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_code_text(self):
        orig_text_node = TextNode("This is a `code snippet` see?", TextType.TEXT)
        text_nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="`", text_type=TextType.CODE)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="code snippet", text_type=TextType.CODE),
                TextNode(text=" see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(text_nodes[0], expected[0])
        self.assertEqual(text_nodes[1], expected[1])
        self.assertEqual(text_nodes[2], expected[2])

    def test_split_bold_italic_and_code_text(self):
        orig_text_node = TextNode("This is a **text in bold**, while *this is in italic*, and `this for code;`, see?", TextType.TEXT)
        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="*", text_type=TextType.ITALIC)
        nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
        expected = [
                TextNode(text="This is a ", text_type=TextType.TEXT),
                TextNode(text="text in bold", text_type=TextType.BOLD),
                TextNode(text=", while ", text_type=TextType.TEXT),
                TextNode(text="this is in italic", text_type=TextType.ITALIC),
                TextNode(text=", and ", text_type=TextType.TEXT),
                TextNode(text="this for code;", text_type=TextType.CODE),
                TextNode(text=", see?", text_type=TextType.TEXT),
            ]

        self.assertEqual(nodes[0], expected[0])
        self.assertEqual(nodes[1], expected[1])
        self.assertEqual(nodes[2], expected[2])
        self.assertEqual(nodes[3], expected[3])
        self.assertEqual(nodes[4], expected[4])

    def test_extract_images(self):
        images = extract_images("Here is ![my dog](https://i.imgur.com/doggo.gif) and here is ![mi gato](https://i.imgur.com/catto.gif)")
        expected = [
                ("my dog", "https://i.imgur.com/doggo.gif"),
                ("mi gato", "https://i.imgur.com/catto.gif")
            ]
        # self.assertCountEqual(text_nodes, expected)
        self.assertEqual(images[0], expected[0])
        self.assertEqual(images[1], expected[1])

    def test_extract_links(self):
        links = extract_links("Here is the link [to my dog profile](https://instagram.dogs/wolfie.com) and here is for [mi gato](https://instagram.cats/pancake.com)")
        expected = [
                ("to my dog profile", "https://instagram.dogs/wolfie.com"),
                ("mi gato", "https://instagram.cats/pancake.com")
            ]
        self.assertEqual(links[0], expected[0])
        self.assertEqual(links[1], expected[1])

    def test_extract_images_will_not_extract_links(self):
        # markdown has links only, no images
        images = extract_images("Here is the link [to my dog profile](https://instagram.dogs/wolfie.com) and here is for [mi gato](https://instagram.cats/pancake.com)")
        expected = []
        self.assertEqual(images, expected)

    def test_extract_links_will_not_extract_images(self):
        # markdown has images only, no links
        links = extract_links("Here is ![my dog](https://i.imgur.com/doggo.gif) and here is ![mi gato](https://i.imgur.com/catto.gif)")
        expected = []
        self.assertEqual(links, expected)

    def test_split_links(self):
        orig_text_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]

        for node in text_nodes:
            self.assertIn(node, expected)

    def test_split_images(self):
        orig_text_node = TextNode("This is text with an ![boot dev mascot image](https://www.boot.dev/mascot-image.png) and also a ![random photo](https://www.boot.dev/random-image-generated.png)", TextType.TEXT)
        text_nodes = split_nodes_image(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("boot dev mascot image", TextType.IMAGE, "https://www.boot.dev/mascot-image.png"),
            TextNode(" and also a ", TextType.TEXT),
            TextNode("random photo", TextType.IMAGE, "https://www.boot.dev/random-image-generated.png")
        ]

        for node in text_nodes:
            self.assertIn(node, expected)

    def test_split_links_with_no_links_returns_original_text_nodes(self):
        orig_text_node = TextNode("This is text with no links", TextType.TEXT)
        text_nodes = split_nodes_link(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no links", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)

    def test_split_nodes_image_with_no_images_returns_original_text_nodes(self):
        orig_text_node = TextNode("This is text with no images", TextType.TEXT)
        text_nodes = split_nodes_image(old_nodes=[orig_text_node])
        expected = [
            TextNode("This is text with no images", TextType.TEXT)
        ]

        self.assertEqual(text_nodes, expected)

    def test_split_links_then_images(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_link(old_nodes=[orig_text_node])
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is **text** with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_links_and_images', nodes)

        for node in nodes:
            self.assertIn(node, expected)

    def test_split_images_then_links(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_image(old_nodes=[orig_text_node])
        nodes = split_nodes_link(old_nodes=nodes)

        expected = [
            TextNode("This is **text** with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_images_then_links', nodes)

        for node in nodes:
            self.assertIn(node, expected)

    def test_split_delimiter_then_images_no_split_link_returns_orig_link_as_text_nodes(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            # TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT),
            # TextNode(" and ", TextType.TEXT),
            # TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_delimiter_then_images', nodes)

        for node in expected:
            self.assertIn(node, nodes)

    def test_split_delimiter_then_link_then_images_returns_proper_text_nodes(self):
        orig_text_node = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and two links: [link 1](https://boot.dev) and [link 2](https://frontendmasters.io)", TextType.TEXT)

        nodes = split_nodes_delimiter(old_nodes=[orig_text_node], delimiter="**", text_type=TextType.BOLD)
        nodes = split_nodes_link(old_nodes=nodes)
        nodes = split_nodes_image(old_nodes=nodes)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an *italic* word and a `code block` and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link 1", TextType.LINK, "https://boot.dev"),
            TextNode(" and two links: ", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("link 2", TextType.LINK, "https://frontendmasters.io"),
        ]

        # print('test_split_delimiter_then_link_then_images', nodes)

        for node in expected:
            self.assertIn(node, nodes)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

