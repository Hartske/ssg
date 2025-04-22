import os
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"  ~ Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, 'r')
    md = from_file.read()
    from_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    # MD to HTML conversion
    nodes = markdown_to_html_node(md)
    html = nodes.to_html()

    # Extract Title
    title = extract_title(md)

    # Replace Template
    page = template.replace('{{ Title }}', title)
    page = template.replace('{{ Content }}', html)

    # Make File
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, mode='w')
    to_file.write(page)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")