import re

def markdown_to_blocks(markdown):
    blocks = list(filter(None, markdown.split("\n\n")))
    clean_blocks = []
    for block in blocks:
        block_prep = re.sub(r'\s{2,}', '\n', block)
        clean_blocks.append(block_prep.strip())
    return clean_blocks
