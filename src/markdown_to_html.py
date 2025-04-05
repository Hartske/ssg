import re
from htmlnode import *
from block_type import *
from textnode import *
from split_nodes import *
from markdown_to_blocks import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", [])

    for block in blocks:
        block_type = block_to_block_type(block)
        # Heading
        if block_type is BlockType.HEADING:
            level = heading_level(block)
            text = re.sub(r"^#{1,6}\s+", '', block)
            children = text_to_children(text)
            heading_node = ParentNode(f"h{level}", children)
            parent_node.children.append(heading_node)
        # Paragraph
        elif block_type is BlockType.PARAGRAPH:
            children = text_to_children(block)
            paragraph_node = ParentNode(f"p", children)
            parent_node.children.append(paragraph_node)
        # Code
        elif block_type is BlockType.CODE:
            text = block.strip()
            if text.startswith("```") and text.endswith("```"):
                text = text[3:-3].strip()
            text_node = TextNode(text, TextType.TEXT)
            content = text_node_to_html_node(text_node)
            code_node = ParentNode('code', [content])
            pre_node = ParentNode('pre', [code_node])
            parent_node.children.append(pre_node)
        # Quote
        elif block_type is BlockType.QUOTE:
            text = re.sub(r'^>\s{0,}', '', block, flags=re.MULTILINE)
            children = line_breaks(text)
            quote_node = ParentNode('blockquote', children)
            parent_node.children.append(quote_node)
        # Unordered List
        elif block_type is BlockType.UNORDERED_LIST:
            text = re.sub(r'^-\s{0,}', '', block, flags=re.MULTILINE)
            items = text_to_list_item(text)
            unordered_node = ParentNode('ul', items)
            parent_node.children.append(unordered_node)
        # Ordered List
        elif block_type is BlockType.ORDERED_LIST:
            text = re.sub(r'^\d+.\s{0,}', '', block, flags=re.MULTILINE)
            items = text_to_list_item(text)
            ordered_node = ParentNode('ol', items)
            parent_node.children.append(ordered_node)
    return parent_node

def heading_level(heading):
    return re.search(r'^#{1,6}\s', heading).end() - 1

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def text_to_list_item(text):
    items = text.split('\n')
    list_nodes = []
    for item in items:
        item_nodes = text_to_textnodes(item)
        html_nodes = []
        for node in item_nodes:
            list_node = text_node_to_html_node(node)
            html_nodes.append(list_node)
        list_item = ParentNode('li', html_nodes)
        list_nodes.append(list_item)
    return list_nodes

def line_breaks(text):
    all_children = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_children = text_to_children(line)
        all_children.extend(line_children)
        if i < len(lines) - 1:
            br_node = LeafNode('br', '')
            all_children.append(br_node)
    return all_children