import unittest

from markdown_to_html_node import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```This is text that _should_ remain
the **same** even with inline stuff
```
"""
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """#heading one with **bold**

### heading _three_ lol

########### heading 6 with extra hash-tags
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>heading one with <b>bold</b></h1><h3> heading <i>three</i> lol</h3><h6>##### heading 6 with extra hash-tags</h6></div>",
        )
    
    def test_ul(self):
        md = """- Hei **på** deg
- Hade på _badet_
- mordi e [mann](https://www.google.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Hei <b>på</b> deg</li><li>Hade på <i>badet</i></li><li>mordi e <a href="https://www.google.com">mann</a></li></ul></div>',
        )

    def test_ol(self):
        md = """1. oner
2. toer
3. treer
4. litt _italics e_ jo fint
5. bhj
6. bruh **mordi e** mann
7. bjbj
8. dette er et ![bilde](url-for-bildet.jpg) :)
9. jdkbjhf
10. sbkd
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>oner</li><li>toer</li><li>treer</li><li>litt <i>italics e</i> jo fint</li><li>bhj</li><li>bruh <b>mordi e</b> mann</li><li>bjbj</li><li>dette er et <img src="url-for-bildet.jpg" alt="bilde"></img> :)</li><li>jdkbjhf</li><li>sbkd</li></ol></div>',
        )

    def test_blockquote(self):
        md = """> og en liten quote
> som går _over_
> flere linjer
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote><p>og en liten quote</p><p>som går <i>over</i></p><p>flere linjer</p></blockquote></div>',
        )

    def test_all_blocks(self):
        md = """
#For **king** and `country`

#####heading nr 

```
> Vi Har laget en block-quote her
Og vi har også **fet** text inni...```

Her er bare noe tilfeldig tekst...
Med et mellomrom, hva vil det gjøre???

- Hei
- Hade
- mordi e mann
- mordi e [mann](https://www.google.com)
- bare så du vett d **solbriller**

1. oner
2. toer
3. treer
4. firer
5. bhj
6. nbk
7. bjbj
8. dette er et ![bilde](url-for-bildet.jpg) :)
9. jdkbjhf
10. sbkd


> og  liten quote
> som går _over_
> flere linjer
> mordi e [mann](https://www.google.com)
> også mordi e mann
"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><h1>For <b>king</b> and <code>country</code></h1><h5>heading nr</h5><pre><code>\n> Vi Har laget en block-quote her\nOg vi har også **fet** text inni...</code></pre><p>Her er bare noe tilfeldig tekst... Med et mellomrom, hva vil det gjøre???</p><ul><li>Hei</li><li>Hade</li><li>mordi e mann</li><li>mordi e <a href="https://www.google.com">mann</a></li><li>bare så du vett d <b>solbriller</b></li></ul><ol><li>oner</li><li>toer</li><li>treer</li><li>firer</li><li>bhj</li><li>nbk</li><li>bjbj</li><li>dette er et <img src="url-for-bildet.jpg" alt="bilde"></img> :)</li><li>jdkbjhf</li><li>sbkd</li></ol><blockquote><p>og  liten quote</p><p>som går <i>over</i></p><p>flere linjer</p><p>mordi e <a href="https://www.google.com">mann</a></p><p>også mordi e mann</p></blockquote></div>""",
        )

if __name__ == "__main__":
    unittest.main()