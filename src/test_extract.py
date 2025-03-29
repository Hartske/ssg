import unittest
from extract import *

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a link to a [website](https://google.com)"
        )
        self.assertListEqual([("website", "https://google.com")], matches)

if __name__ == "__main__":
    unittest.main()