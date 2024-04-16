import re
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
        block.strip()
        new_blocks.append(block)
    return new_blocks

def block_to_blocktype(block):
    if re.match(re_heading, block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        return block_type_unordered_list
    if re.match(r"^\d+\.", block):
        return block_type_ordered_list
    return block_type_paragraph