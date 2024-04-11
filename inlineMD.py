from textnode import TextNode
import re


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

delimiter_dict = {
    "`": text_type_code,
    "**": text_type_bold,
    "*": text_type_italic,
    "[": text_type_link,
    "![": text_type_image
}

#This function needs to extract ony TextNodes from a given line of MD text.
#We assume that the delimiter is not nested in other delimiters
#We assume that we know what the delimiters are
#Text nodes are always on even indexes after splitting on delimiter
#if the code block is at the beginning of the line, the first node will be an empty string hence the if condition

def split_nodes_delimiter(old_nodes : list[TextNode], delimiter, text_type):

    allowed_types = ["text", "bold", "italic", "code", "link", "image"]
    #delimiter_dict ---- exists on top of the file
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        splited_node = []
        sections = node.text.split(delimiter)
        if len(sections) == 2:
            raise ValueError("Markdown section is not closed")
        for i in range(0,len(sections)):
            if sections[i] == "":
                continue
            if i %2 == 0:
                splited_node.append(TextNode(sections[i],text_type_text))
            else:
                splited_node.append(TextNode(sections[i],text_type))
        new_nodes.extend(splited_node)
    return new_nodes



#------------------------------------------------------------------------------
def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links

def split_nodes_image(old_nodes:list[TextNode]):
    pass



def split_nodes_link(old_nodes:list[TextNode]):
    pass