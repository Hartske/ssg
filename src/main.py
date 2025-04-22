from textnode import *
from htmlnode import *
from copystatic import copy_files
from gencontent import generate_page_recursive
import os
import shutil
import sys

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("~ Cleaning Docs Dir")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("~ Copying Files to Docs...")
    copy_files(dir_path_static, dir_path_docs)

    print('~ Generating pages...')
    generate_page_recursive(
        dir_path_content,
        template_path,
        dir_path_docs,
        basepath
    )

main()
