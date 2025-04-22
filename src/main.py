from textnode import *
from htmlnode import *
from copystatic import copy_files
from gencontent import generate_page_recursive
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("~ Cleaning Public Dir")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("~ Copying Files to Public...")
    copy_files(dir_path_static, dir_path_public)

    print('~ Generating pages...')
    generate_page_recursive(
        dir_path_content,
        template_path,
        dir_path_public
    )

main()
