from textnode import *
from htmlnode import *
from copystatic import copy_files
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("~ Checking for Public Dir")
    if os.path.exists(dir_path_public):
        print("~ Cleaning Up")
        shutil.rmtree(dir_path_public)
    else:
        print("~ All Clear!")

    print("~ Copying Files to Public...")
    copy_files(dir_path_static, dir_path_public)

main()
