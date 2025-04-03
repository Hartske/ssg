import re
from textnode import *
from extract import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) < 2:
            new_nodes.append(node)
            continue

        text_split = node.text.split(delimiter)

        if len(text_split) % 2 == 0:
            raise ValueError(f"Invalid markdown: Odd number of '{delimiter}' delimiters")

        for i in range(len(text_split)):
            text_chunk = text_split[i]
            current_type = TextType.TEXT if i % 2 == 0 else text_type
            new_nodes.append(TextNode(text_chunk, current_type))
            
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text) is None:
            new_nodes.append(node)
            continue

        text_split = list(filter(None, re.split(r"\!\[|\)", node.text)))

        for i in range(len(text_split)):
            image_chunk = text_split[i]
            if i % 2 == 0:
                new_nodes.append(TextNode(image_chunk, TextType.TEXT))
            else:
                image_split = re.split(r"\]\(", image_chunk)
                new_nodes.append(TextNode(image_split[0], TextType.IMAGE, image_split[1]))
                
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if re.search(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text) is None:
            new_nodes.append(node)
            continue

        text_split = list(filter(None, re.split(r"\[|\)", node.text)))

        for i in range(len(text_split)):
            link_chunk = text_split[i]
            if i % 2 == 0:
                new_nodes.append(TextNode(link_chunk, TextType.TEXT))
            else:
                link_split = re.split(r"\]\(", link_chunk)
                new_nodes.append(TextNode(link_split[0], TextType.LINK, link_split[1]))
    return new_nodes
