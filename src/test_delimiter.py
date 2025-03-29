import unittest
from textnode import *
from delimiter import *

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter1(self):
        # Test Case 1
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " word"
        assert new_nodes[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter2(self):
        # Test Case 2
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with an "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "italic"
        assert new_nodes[1].text_type == TextType.ITALIC
        assert new_nodes[2].text == " word"
        assert new_nodes[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter3(self):
        # Test Case 3
        node = TextNode("This is text with **bold** and _italic_ words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " and _italic_ words"
        assert new_nodes[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter4(self):
        # Test Case 4
        node = TextNode("This is text with a `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "code"
        assert new_nodes[1].text_type == TextType.CODE
        assert new_nodes[2].text == " block"
        assert new_nodes[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter5(self):
        # Test Case 5
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with an _italic_ word", TextType.TEXT),
            TextNode("This is text with a **bold** word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
        assert len(new_nodes) == 7
        assert new_nodes[0].text == "This is text with "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " and _italic_ words"
        assert new_nodes[2].text_type == TextType.TEXT
        assert new_nodes[3].text == "This is text with an _italic_ word"
        assert new_nodes[3].text_type == TextType.TEXT
        assert new_nodes[4].text == "This is text with a "
        assert new_nodes[4].text_type == TextType.TEXT
        assert new_nodes[5].text == "bold"
        assert new_nodes[5].text_type == TextType.BOLD
        assert new_nodes[6].text == " word"
        assert new_nodes[6].text_type == TextType.TEXT

if __name__ == "__main__":
    unittest.main()
