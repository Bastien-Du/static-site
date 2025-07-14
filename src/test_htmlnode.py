import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_with_children(self):
        child1 = LeafNode("p", "First paragraph.")
        child2 = LeafNode("p", "Second paragraph.")
        parent = ParentNode("div", [child1, child2])
        expected = "<div><p>First paragraph.</p><p>Second paragraph.</p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_parent_node_with_props(self):
        child = LeafNode("span", "Some text")
        parent = ParentNode("div", [child], {"class": "container"})
        expected = '<div class="container"><span>Some text</span></div>'
        self.assertEqual(parent.to_html(), expected)

    def test_parent_node_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("p", "Text")])
        self.assertIn("tag", str(context.exception).lower())

    def test_parent_node_missing_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertIn("children", str(context.exception).lower())


if __name__ == "__main__":
    unittest.main()