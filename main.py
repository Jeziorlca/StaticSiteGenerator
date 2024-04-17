from textnode import TextNode
from htmlnode import HTMLNode, ParrentNode, LeafNode
import os
import shutil

def copy_dir(src, dest):
    if os.path.isdir(src):
        if not os.path.exists(dest):
            os.makedirs(dest)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            copy_dir(s, d)
    else:
        shutil.copy2(src, dest)


if os.path.exists("public"):
    shutil.rmtree("public/")

copy_dir("static", "public")

