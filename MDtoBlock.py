import re
from htmlnode import ParrentNode
from inlineMD import text_to_textnode
from textnode import text_node_to_html_node
#MD Block types:
block_type_paragraph = "paragraph"  # \n just plain text
block_type_heading = "heading" #starts with 1-6 # ## ### ##### ###### ###### + space
re_heading = r"^(#{1,6})\s"
block_type_code = "code" # ``` ```
block_type_quote = "quote" # every line starts with >
block_type_unordered_list = "unordered_list" # every line starts with * or -
block_type_ordered_list = "ordered_list" # every line starts with a {number}. in an increment of 1. List always starts with 1. 

#Block-level markdown is just the separation of different sections of an entire document. 
#In well-written markdown (which we'll just assume is the only thing going into our generator) blocks are separated by a single blank line. 

def markdown_to_block(text):
    blocks = text.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        new_blocks.append(block)
    return new_blocks

def block_to_blocktype(block):
    lines = block.split("\n")
       
    if re.match(re_heading, block):
        return block_type_heading
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return block_type_code
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

#Now you need to take a block and its "type" and convert it into an HTMLNode (I recommend a separate function for each type of block).

def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParrentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_blocktype(block)
    if block_type == block_type_paragraph:
        return paragraph_to_htmlnode(block)
    if block_type == block_type_heading:
        return heading_to_htmlnode(block)
    if block_type == block_type_code:
        return code_to_htmlnode(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_htmlnode(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_htmlnode(block)
    if block_type == block_type_quote:
        return quote_to_htmlnode(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    children = []
    for text_node in text_nodes:
        HTMLNode = text_node_to_html_node(text_node)
        children.append(HTMLNode)
    return children

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParrentNode("p", children, None)

def unordered_list_to_htmlnode(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParrentNode("li", children))
    return ParrentNode("ul", html_items, None)

def ordered_list_to_htmlnode(block):
    lines = block.split("\n")
    html_items = [] #trzeba obciąć /d+.
    for item in lines:
        text = item.split(". ", 1)[1]
        children = text_to_children(text)
        html_items.append(ParrentNode("li", children))
    return ParrentNode("ol", html_items, None)

def code_to_htmlnode(block):
    # <pre><code>text</code></pre>
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParrentNode("code", children ,None)
    return ParrentNode("pre", [code], None)
        
def quote_to_htmlnode(block):
    #contend of blockquote is just a paragaraph with stripped ">" at the begining
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError ("Invalid line start")    
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParrentNode("blockquote", children, None)

def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParrentNode(f"h{level}", children)
    #print(block)
    #heading_level = len(re.findall(re_heading, block)[0])
    #lines = block.split("\n")
    #new_lines = []
    #for line in lines:
    #    if not line.startswith("#"):
    #        raise ValueError ("Invalid line start")
    #    new_line = line.lstrip("#").strip()
    #    new_lines.append(new_line)
    #content = "".join(new_lines)
    #children = text_to_children(content)
    #return ParrentNode(f"h{heading_level}", children, None)

#print(type(heading_to_htmlnode("## This is a heading")) )
#print(type(ParrentNode("h2", LeafNode(None, "This is a heading", None))))
#print(heading_to_htmlnode("## This is a heading") == ParrentNode("h2", LeafNode(None, "This is a heading", None)))