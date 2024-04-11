import unittest

from textnode import TextNode
from textnode import text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
from inlineMD import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class Testsplit_nodes_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),]
)
        
class Testextract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![image](https://www.boot.dev) word"
        self.assertEqual(extract_markdown_images(text),[("image", "https://www.boot.dev")])
        text2= "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text2),[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_markdown_links(self):
        text1 = "This is text with a [link](https://www.boot.dev) word"
        self.assertEqual(extract_markdown_links(text1),[("link", "https://www.boot.dev")])
        text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text2),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])