from enum import Enum

class TextType(Enum):
    normal = "normal text"
    bold = "**bold text**"
    italic = "italic text_"
    code = "`code text`"
    link = "link"
    image = "Image"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        pass
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"