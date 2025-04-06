import unittest
from markdown_to_html import *

class TestMarkdowntoHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
#### This is a heading Text with a **bold** text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>This is a heading Text with a <b>bold</b> text</h4></div>"
        )

    def test_quote(self):
        md = """
>This is a line in a quote block.
>This is another line in a quote block.
>This is a third line in a quote block.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a line in a quote block.<br></br>This is another line in a quote block.<br></br>This is a third line in a quote block.</blockquote></div>"
        )

    def test_ordered_list(self):
        md = """
1. line one
2. line two
4. line three
4. line four
5. line five
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>line one</li><li>line two</li><li>line three</li><li>line four</li><li>line five</li></ol></div>"
        )

    def test_unordered_list(self):
        md = """
- line one
- line two
- line three
- line four
- line five
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>line one</li><li>line two</li><li>line three</li><li>line four</li><li>line five</li></ul></div>"
        )

    def test_unordered_list_2(self):
        md = """
- line **one**
- line `two`
- line _three_
- line [four](https://some.link)
- line five
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>line <b>one</b></li><li>line <code>two</code></li><li>line <i>three</i></li><li>line <a href="https://some.link">four</a></li><li>line five</li></ul></div>'
        )

if __name__ == "__main__":
    unittest.main()