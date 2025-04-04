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

        matches = re.finditer(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)

        last_index = 0
        for match in matches:
            # Add text before the image pattern (if any).
            if last_index < match.start():
                new_nodes.append(TextNode(node.text[last_index:match.start()], TextType.TEXT))
            
            # Add the matched image node.
            image_text = match.group(1)  # The text inside [ ]
            image_url = match.group(2)   # The URL inside ( )
            new_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))
            
            last_index = match.end()
        
        # Add any remaining text after the last match.
        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
                
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

        matches = re.finditer(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)

        last_index = 0
        for match in matches:
            # Add text before the link pattern (if any).
            if last_index < match.start():
                new_nodes.append(TextNode(node.text[last_index:match.start()], TextType.TEXT))
            
            # Add the matched link node.
            link_text = match.group(1)  # The text inside [ ]
            link_url = match.group(2)   # The URL inside ( )
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            last_index = match.end()
        
        # Add any remaining text after the last match.
        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes