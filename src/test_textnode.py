import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("Image description", TextType.IMAGE, 'src/image/23.jpg')
        node2 = TextNode("Image description", TextType.IMAGE, 'src/image/23.jpg')
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Some Link", TextType.LINK, 'https://somelink.co')
        node2 = TextNode("Some Link", TextType.LINK, 'https://somelink.co')
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("Some Link", TextType.LINK, 'https://somelink.co')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()