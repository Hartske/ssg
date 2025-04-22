import os
import shutil

def copy_files(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        print(f" ~ {src_path} -> {dst_path}")
        if os.path.isfile(src_path) == True:
            shutil.copy(src_path, dst_path)
        else:
            copy_files(src_path, dst_path)