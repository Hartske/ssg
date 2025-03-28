import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('a', 'Website', [], {'href': 'https://www.google.com', 'target': '_blank'})
        node2 = HTMLNode('a', 'Website', [], {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = HTMLNode('p','This is text in a paragraph.', [], {})
        node2 = HTMLNode('p','This is text in a paragraph.', [], {})
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = HTMLNode('h1','This is a Heading.', [], {})
        node2 = HTMLNode('h1','This is a Heading.', [], {})
        self.assertEqual(node, node2)
    
    def test_eq4(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), "<p>Hello world!</p>")
    
    def test_eq5(self):
        node = LeafNode('a', 'Website', {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.to_html(), '<a>Website</a>')

    def test_eq6(self):
        node = LeafNode('h1','This is a Heading.')
        self.assertEqual(node.to_html(), '<h1>This is a Heading.</h1>')


if __name__ == "__main__":
    unittest.main()