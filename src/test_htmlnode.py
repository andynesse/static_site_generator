import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node

class TestTextNode(unittest.TestCase):

    #HTMLNode:
    def test_eq(self):
        child = HTMLNode("p", "This is a small paragraph!", None, {"id": "info-p"})
        node  = HTMLNode("section", "Value here", [child], {"class": "container blue", "style": "display: block;"})
        node2 = HTMLNode("section", "Value here", [child], {"class": "container blue", "style": "display: block;"})
        self.assertEqual(repr(node), repr(node2))
   
    def test_props_to_html_eq(self):
        child = HTMLNode("p", "This is a small paragraph!", None, {"id": "info-p"})
        node = HTMLNode("section", None, [child], {"class": "container blue", "style": "display: block;"})
        self.assertEqual(node.props_to_html(), ' class="container blue" style="display: block;"')

    def test_value_none_not_eq(self):
        child = HTMLNode("p", "This is a small paragraph!", None, {"id": "info-p"})
        node = HTMLNode("section", None, [child], {"class": "container blue", "style": "display: block;"})
        node2 = HTMLNode("section", "None", [child], {"class": "container blue", "style": "display: block;"})
        self.assertNotEqual(node, node2)


    #LeafNode:
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_prop(self):
        node = LeafNode("a", "Click me!", { "href": "https://www.boot.dev" } )
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("a", "Click me!", { "href": "https://www.boot.dev", "class": "link" } )
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" class="link">Click me!</a>')


    #ParentNode:
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node, grandchild_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><b>grandchild</b></div>",
        )
    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "bold_text"})
        child_node = ParentNode("a", [grandchild_node], {"class": "link", "href": "https://www.boot.dev"})
        parent_node = ParentNode("div", [child_node, grandchild_node], {"id": "grandparent-container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="grandparent-container"><a class="link" href="https://www.boot.dev"><b class="bold_text">grandchild</b></a><b class="bold_text">grandchild</b></div>',
        )

    # text to html:
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italian node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is an italian node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, url="https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_image  (self):
        node = TextNode("This is a image node", TextType.IMAGE, url="https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is a image node"})

if __name__ == "__main__":
    unittest.main()