import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "http://localhost"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="http://localhost"',
        )

if __name__ == "__main__":
    unittest.main()