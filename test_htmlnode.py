import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        html = HTMLNode(tag="p", value="Hello World!", children=["Hello", "World!"], props={"href": "https://www.google.com"})
        print(html)