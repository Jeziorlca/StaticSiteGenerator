import os
import shutil
from genContent import genPage

dir_path_static = r"C:\Users\jezio\Code\BootDev\StaticSiteGenerator\static"
dir_path_public = r"C:\Users\jezio\Code\BootDev\StaticSiteGenerator\public"
dir_path_content = r"C:\Users\jezio\Code\BootDev\StaticSiteGenerator\content"
template_path = r"C:\Users\jezio\Code\BootDev\StaticSiteGenerator\template.html"

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
    genPage(
        os.path.join(dir_path_content, "index.md"),
        os.path.join(dir_path_public, "index.html"),
        template_path,
    )

main()