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
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Website</a>')

    def test_eq6(self):
        node = LeafNode('h1','This is a Heading.')
        self.assertEqual(node.to_html(), '<h1>This is a Heading.</h1>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_multi_nest(self):
        child1 = LeafNode("b", "Some bolded text")
        child2 = LeafNode("a", "website", {"href": "https://google.com", "target": "_blank"})
        parent1 = ParentNode("p", [child1, child2])
        child3 = LeafNode("h1", "Some Heading")
        parent2 = ParentNode("div", [child3, parent1])
        self.assertEqual(
            parent2.to_html(),
            '<div><h1>Some Heading</h1><p><b>Some bolded text</b><a href="https://google.com" target="_blank">website</a></p></div>',
        )

    def test_parent_empty_child(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_deep_nest(self):
        child1 = LeafNode("b", "Some bolded text")
        child2 = LeafNode("a", "website", {"href": "https://google.com", "target": "_blank"})
        parent1 = ParentNode("p", [child1, child2])
        child3 = LeafNode("h1", "Some Heading")
        parent2 = ParentNode("div", [child3, parent1])
        parent3 = ParentNode("div", [parent2])
        child4 = LeafNode("b", "Some bolded text")
        parent4 = ParentNode("h1", [child4, parent3])
        parent5 = ParentNode("div", [parent4])
        self.assertEqual(
            parent5.to_html(),
            '<div><h1><b>Some bolded text</b><div><div><h1>Some Heading</h1><p><b>Some bolded text</b><a href="https://google.com" target="_blank">website</a></p></div></div></h1></div>',
        )


if __name__ == "__main__":
    unittest.main()