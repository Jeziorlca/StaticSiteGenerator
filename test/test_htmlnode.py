import unittest

from htmlnode import HTMLNode, LeafNode, ParrentNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        html = HTMLNode("p", "Hello World!", ["Hello", "World!"], {"href": "https://www.google.com"})
        print(html)
    
    def test_props_to_html(self):
        html = HTMLNode("p", "Hello World!", ["Hello", "World!"], {"href": "https://www.google.com"})
        html2 = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank" })
        html3 = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank", "rel": "noopener noreferrer", "aria-label": "Open in a new tab" })
        node = HTMLNode("div","Hello, world!",None,{"class": "greeting", "href": "https://boot.dev"},)
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://boot.dev"',)
        self.assertEqual(html.props_to_html(), ' href="https://www.google.com"')
        self.assertEqual(html2.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(html3.props_to_html(), ' href="https://www.google.com" target="_blank" rel="noopener noreferrer" aria-label="Open in a new tab"')

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        html = LeafNode("p", "This is a paragraph of text.")
        html2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        self.assertEqual(html.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(html2.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        #html = ParrentNode("p", "Hello World!", ["Hello", "World!"], {"href": "https://www.google.com"})
        node = ParrentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        #self.assertEqual(html.to_html(), "<p><b>Bold text</b><i>italic text</i><b>Normal text</b><i>Normal text</i></p>")
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")