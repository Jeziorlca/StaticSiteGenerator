import unittest

from textnode import TextNode
from textnode import text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        
        self.assertEqual(node, node2)
        self.assertNotEqual(node, TextNode("This is a text node", "bold", "https://www.boot.dev"))
        self.assertNotEqual(node, TextNode("This is a text node", "italic", "https://www.boot.dev"))
        self.assertNotEqual(node, TextNode("This is a text node", "bold", "https://www.google.com"))
        self.assertNotEqual(node, TextNode("This is a text nod", "bold", "https://www.boot.dev"))
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.boot.dev)")

class Testsplit_nodes_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text node", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),]
)

if __name__ == "__main__":
    unittest.main()
