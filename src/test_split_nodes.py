import unittest
from textnode import *
from split_nodes import *

class TestDelimiter(unittest.TestCase):
    # Split Nodes Delimiter Tests
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
        
    # Split Nodes Image Tests
    def test_split_images(self):
        # Test Case 1
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

    def test_split_images2(self):
        # Test Case 2
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with an _italic_ word", TextType.TEXT),
            TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
            TextNode("This is text with a **bold** word", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with an _italic_ word", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://google.com"),
                TextNode("This is text with a **bold** word", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_images3(self):
        # Test Case 2
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with a [link](https://google.com)", TextType.LINK),
            TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
            TextNode("This is text with a **bold** word", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with a [link](https://google.com)", TextType.LINK),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://google.com"),
                TextNode("This is text with a **bold** word", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_split_images4(self):
        # Test Case 2
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with a [link](https://google.com)", TextType.LINK),
            TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
            TextNode(" ", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with a [link](https://google.com)", TextType.LINK),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://google.com"),
                TextNode(" ", TextType.TEXT)
            ],
            new_nodes
        )

    # Split Nodes Link Tests
    def test_split_link(self):
        # Test Case 1
        node = TextNode(
        "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link2(self):
        # Test Case 2
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with an _italic_ word", TextType.TEXT),
            TextNode("This is text with an [link](https://google.com)", TextType.TEXT),
            TextNode("This is text with a **bold** word", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with an _italic_ word", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode("This is text with a **bold** word", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_link3(self):
        # Test Case 3
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with a [link](https://google.com)", TextType.TEXT),
            TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
            TextNode("This is text with a **bold** word", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://google.com"),
        ]
        new_nodes = split_nodes_link(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
                TextNode("This is text with a **bold** word", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://google.com"),
            ],
            new_nodes
        )
    
    def test_split_link4(self):
        # Test Case 4
        node = [
            TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
            TextNode("This is text with a [link](https://google.com)", TextType.TEXT),
            TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://google.com"),
        ]
        new_nodes = split_nodes_link(node)
        self.assertListEqual(
            [
                TextNode("This is text with **bold** and _italic_ words", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode("This is text with an ![image](https://google.com)", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://google.com"),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
