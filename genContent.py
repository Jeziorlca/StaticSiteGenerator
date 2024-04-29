import os
from MDtoBlock import markdown_to_html_node

def genPage(from_path, to_path, template_path):
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = grabTitle(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_path = os.path.dirname(to_path)
    if dest_path != "":
        os.makedirs(dest_path, exist_ok=True)
    to_file = open(to_path, "w")
    to_file.write(template)


def grabTitle(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")