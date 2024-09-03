import os
import shutil
from genContent import genPage, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

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

def main():
    print(os.getcwd())

    print("Removing public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public/")

    print("Copying static directory to public...") 
    copy_dir("static", "public")

    #Generating page
    #genPage(
    #    os.path.join(dir_path_content, "index.md"),
    #    os.path.join(dir_path_public, "index.html"),
    #    template_path,
    #)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
main()