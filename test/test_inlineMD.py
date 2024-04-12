import unittest

from textnode import TextNode
from textnode import text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
from inlineMD import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

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
    maxDiff = None
    def test_extract_markdown_images(self):
        text = "This is text with a ![image](url) word"
        self.assertEqual(extract_markdown_images(text),[("image", "url")])
        text2= "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text2),[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])       
        text3= "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text3),[("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        text4= "txt ![image](url)txt ![image](url)txt ![image](url)txt ![image](url)"
        self.assertEqual(extract_markdown_images(text4),[("image", "url"),("image", "url"),("image", "url"),("image", "url")])

    def test_extract_markdown_links(self):
        text1 = "This is text with a [link](url) word"
        self.assertEqual(extract_markdown_links(text1),[("link", "url")])
        text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text2),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
    
    def test_split_nodes_image(self):
        #write a test that contains 2 the same images
        text = TextNode("This is text with a ![image](url)", text_type_text,)
        text1= TextNode("Sum text ![image](url) word ![second image](url) dupa", text_type_text,)
        text2= TextNode("Sum text ![image](url) Sum text ![image](url) Sum text ![image](url) Sum text ![image](url) Sum text ![image](url) dupa", text_type_text,)
        node = TextNode("This is text with an ![image](url) and another ![second image](url)", text_type_text,)
        self.assertEqual(split_nodes_image([text]),[TextNode("This is text with a ", text_type_text),TextNode("image", text_type_image, "url")])
        self.assertEqual(split_nodes_image([text1]),[TextNode("Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" word ", text_type_text),TextNode("second image", text_type_image, "url"),TextNode(" dupa", text_type_text)])
        self.assertEqual(split_nodes_image([text2]),[TextNode("Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" Sum text ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" dupa", text_type_text)])
        self.assertEqual(split_nodes_image([node]),[TextNode("This is text with an ", text_type_text),TextNode("image", text_type_image, "url"),TextNode(" and another ", text_type_text),TextNode("second image", text_type_image, "url")])

    def test_split_nodes_link(self):
        text = TextNode("This is text with a [link](url) word", text_type_text,)
        self.assertEqual(split_nodes_link([text]),[TextNode("This is text with a ", text_type_text),TextNode("link", text_type_link, "url"),TextNode(" word", text_type_text)])