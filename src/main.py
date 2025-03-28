from textnode import *
from htmlnode import *

def main():
    test = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(test)
    test2 = LeafNode("p", "Hello world!")
    print(test2.to_html())

main()
