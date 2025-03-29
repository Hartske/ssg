from textnode import *

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
