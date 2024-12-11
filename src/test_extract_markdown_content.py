import unittest

from extract_markdown_content import *


class TestExtractMarkdownContent(unittest.TestCase):
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
