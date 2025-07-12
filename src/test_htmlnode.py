import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", props={"id": "container", "class": "main"})
        self.assertEqual(repr(node), "HTMLNode(tag='div', value='Hello', children=[], props={'id': 'container', 'class': 'main'})")

if __name__ == "__main__":
    unittest.main()