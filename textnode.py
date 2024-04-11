from htmlnode import HTMLNode, ParrentNode, LeafNode

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
    