from extract_markdown import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from text_node_to_html_node import text_node_to_html_node
from text_to_text_node import text_to_text_node
from htmlnode import ParentNode, LeafNode
def markdown_to_html_node(markdown):
    html_content = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.QUOTE:
                lines = [[text_node_to_html_node(text_node) for text_node in text_to_text_node(line[2:])] for line in block.split("\n")]
                value = None
                if lines[0][0].value.strip()[0] == '"' and lines[0][0].value.strip()[-1] == '"':
                    value = lines[0][0].value
                    lines[0].pop(0)
                quotes = [ParentNode("p", line) for line in lines if len(line) != 0 and len(line[0].value) != 0]
                html_block = ParentNode("blockquote", quotes, value=value)
            case BlockType.CODE:
                html_block = ParentNode("pre", [LeafNode("code", block[3:len(block)-3])])
            case BlockType.HEADING:
                level = len(block) - len(block.lstrip("#"))
                block = "#"*(level -6 ) + block.lstrip("#").strip()
                if level > 6:
                    level = 6
                html_block = ParentNode(f"h{level}", [text_node_to_html_node(text_node) for text_node in text_to_text_node(block)])
            case BlockType.PARAGRAPH:
                html_block = ParentNode("p", [text_node_to_html_node(text_node) for text_node in text_to_text_node(" ".join(block.split("\n")))])
            case BlockType.UNORDERED_LIST:
                li_items = []
                for li_item in block.split("\n"):
                    li_items.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_to_text_node(li_item[2:])]))
                html_block = ParentNode("ul", li_items)
            case BlockType.ORDERED_LIST:
                li_items = []
                for li_item in block.split("\n"):
                    li_items.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_to_text_node(li_item[li_item.index(".")+2:])]))
                html_block = ParentNode("ol", li_items)

        html_content.append(html_block)
    return ParentNode("div", html_content)
