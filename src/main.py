from textnode import *

def main():
    test = TextNode('This is some anchor text', TextType(5), 'https://www.boot.dev')
    test_repr = test.__repr__
    print(test_repr)

main()
