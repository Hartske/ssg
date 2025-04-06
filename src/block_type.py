from enum import Enum
import re

class BlockType(Enum): 
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(block):
    if re.search(r'^#{1,6}\s', block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if re.search(r'^>', block, flags=re.MULTILINE):
        return BlockType.QUOTE
    if re.search(r'^-\s', block, flags=re.MULTILINE):
        return BlockType.UNORDERED_LIST
    if re.search(r'^\d+.\s', block, flags=re.MULTILINE):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
