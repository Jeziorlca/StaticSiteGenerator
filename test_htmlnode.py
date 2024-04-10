import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        html = HTMLNode(tag="p", value="Hello World!", children=["Hello", "World!"], props={"href": "https://www.google.com"})
        print(html)
    
    def test_props_to_html(self):
        html = HTMLNode(tag="p", value="Hello World!", children=["Hello", "World!"], props={"href": "https://www.google.com"})
        html2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank" })
        html3 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "rel": "noopener noreferrer", "aria-label": "Open in a new tab" })
        self.assertEqual(html.props_to_html(), "href=https://www.google.com")
        self.assertEqual(html2.props_to_html(), "href=https://www.google.com target=_blank")
        self.assertEqual(html3.props_to_html(), "href=https://www.google.com target=_blank rel=noopener noreferrer aria-label=Open in a new tab")

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        html = LeafNode(tag="p", value="This is a paragraph of text.")
        html2 = LeafNode(tag="a",value= "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(html.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(html2.to_html(), "<a href=https://www.google.com>Click me!</a>")