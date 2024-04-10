from htmlnode import HTMLNode, ParrentNode, LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self) -> str:
        return "TextNode(" + str(self.text) + ", " + str(self.text_type)  + ", " + str(self.url) + ")"

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

def text_node_to_html_node(text_node):
    #text_type_text: This should become a LeafNode with no tag, just a raw text value.
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text, None)
    #text_type_bold: This should become a LeafNode with a "b" tag and the text
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text, None)
    #text_type_italic: "i" tag, text
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text, None)
    #text_type_code: "code" tag, text
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text, None)
    #text_type_link: "a" tag, anchor text, and "href" prop
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    #text_type_image: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception("Unknown text type: " + text_node.text_type)
    
def split_nodes_delimiter(old_nodes : TextNode, delimiter, text_type):
#I don't want to give you full pseudocode, but here are a few tips:
#I created variables like text_type_text="text" and text_type_code="code" to represent the various valid TextNode types.
#If an "oldnode" is not a text type TextNode, you should just add it to the new list as-is, we only attempt to split text type TextNode objects.
#If a matching closing delimiter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
#The .split() method was useful to me
#The .extend() method was useful to me
    allowed_types = ["text", "bold", "italic", "code", "link", "image"]
    new_nodes = []
    print(type(old_nodes))
    if old_nodes.text_type not in allowed_types:
        raise Exception("Invalid markdown syntax")
    elif old_nodes.text_type == text_type:        
        new_nodes.append(old_nodes.text)
    else:
        new_nodes.extend(old_nodes.text.split(delimiter))
    return new_nodes


node = TextNode("This is text with a `code block` word", text_type_text)
new_nodes = split_nodes_delimiter([node], "`", text_type_code)
#[
#    TextNode("This is text with a ", text_type_text),
#    TextNode("code block", text_type_code),
#    TextNode(" word", text_type_text),
#]