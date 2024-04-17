import unittest

from MDtoBlock import *

class test_markdown_to_block(unittest.TestCase):
    maxDiff = None
    def test_markdown_to_block(self):
        MD = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertEqual(len(markdown_to_block(MD)), 3)

    def test_block_to_blocktype(self):
        test1 = "```python\nprint(\"Hello World\")\n```"
        test2 = """> This is a quote
> with some text"""
        test3 = """* This is a list
* with items
* unsorted"""
        test4 = """- This is an unordered list"""
        test5 = """1. This is an ordered list
2. with items"""
        test6 = "# This is a heading"
        test7 = "## This is a sub-heading"
        test8 = "### This is a sub-sub-heading"
        test9 = "#### This is a sub-sub-sub-heading"
        test10 = "##### This is a sub-sub-sub-sub-heading"
        test11 = "###### This is a sub-sub-sub-sub-sub-heading"
        test12 = "####### This is a sub-sub-sub-sub-sub-sub-heading"
        test13 = "######## This is a sub-sub-sub-sub-sub-sub-sub-heading"
        test14 = "1 this is a paragraph"
        test15 = "**This is just plain text**"
        test16 = """1. this is a beniging of a list
10. but it failed"""

        self.assertEqual(block_to_blocktype("paragraph"), "paragraph")
        self.assertEqual(block_to_blocktype("This is just plain text"), "paragraph")
        self.assertEqual(block_to_blocktype(test1), "code")
        self.assertEqual(block_to_blocktype(test2), "quote")
        self.assertEqual(block_to_blocktype(test3), "unordered_list")
        self.assertEqual(block_to_blocktype(test4), "unordered_list")
        self.assertEqual(block_to_blocktype(test5), "ordered_list")
        self.assertEqual(block_to_blocktype(test6), "heading")
        self.assertEqual(block_to_blocktype(test7), "heading")
        self.assertEqual(block_to_blocktype(test8), "heading")
        self.assertEqual(block_to_blocktype(test9), "heading")
        self.assertEqual(block_to_blocktype(test10), "heading")
        self.assertEqual(block_to_blocktype(test11), "heading")
        self.assertEqual(block_to_blocktype(test12), "paragraph")
        self.assertEqual(block_to_blocktype(test13), "paragraph")
        self.assertEqual(block_to_blocktype(test14), "paragraph")
        self.assertEqual(block_to_blocktype(test15), "paragraph")
        self.assertEqual(block_to_blocktype(test16), "paragraph") #this is wrong in context of true MD ordered list, but for now it must suffice

    def test_heading_to_htmlnode(self):
        test1 = "# This is a heading"
        test2 = "## This is a sub-heading"
        test3 = "### This is a sub-sub-heading"
        test4 = "#### This is a sub-sub-sub-heading"
        test5 = "##### This is a sub-sub-sub-sub-heading"
        test6 = "###### This is a sub-sub-sub-sub-sub-heading"
        test7 = "####### This is a sub-sub-sub-sub-sub-sub-heading"
        test8 = "######## This is a sub-sub-sub-sub-sub-sub-sub-heading"

        #self.assertEqual(heading_to_htmlnode(test1), ParrentNode("h1", "<h1><div>This is a heading</div></h1>", None)) 
        pass