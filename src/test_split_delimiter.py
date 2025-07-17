from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

def test_split_code():
    node = TextNode("Code with `inline` code", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [
        TextNode("Code with ", TextType.TEXT),
        TextNode("inline", TextType.CODE),
        TextNode(" code", TextType.TEXT)
    ]
    assert result == expected

def test_split_bold():
    node = TextNode("Some **bold** text", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected = [
        TextNode("Some ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT)
    ]
    assert result == expected