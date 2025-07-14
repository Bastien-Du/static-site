import unittest
from htmlnode import HTMLNode, LeafNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_none_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_raises_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("img", "Image", {"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image">Image</img>')



if __name__ == "__main__":
    unittest.main()