from textnode import TextNode


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

#I created variables like text_type_text="text" and text_type_code="code" to represent the various valid TextNode types.
#If an "oldnode" is not a text type TextNode, you should just add it to the new list as-is, we only attempt to split text type TextNode objects.
#If a matching closing delimiter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
#The .split() method was useful to me
#The .extend() method was useful to me

def split_nodes_delimiter(old_nodes : TextNode, delimiter, text_type):

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
                splited_node.append(TextNode(sections[1],text_type_text))
            else:
                splited_node.append(TextNode(sections[i],text_type))
        new_nodes.extend(splited_node)
    return new_nodes



#This is what we want!
node = TextNode("This is text with a `code block` word", text_type_text)
new_nodes = split_nodes_delimiter([node], "`", text_type_code)
print(new_nodes)
#[
#    TextNode("This is text with a ", text_type_text),
#    TextNode("code block", text_type_code),
#    TextNode(" word", text_type_text),
#]