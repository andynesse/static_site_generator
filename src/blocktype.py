from extract_markdown import markdown_to_blocks
from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block[0] == "#" and not "\n" in block:
        return BlockType.HEADING
    if block[:3] == "```" and block[len(block)-3:] == "```" and len(block) >= 6:
        return BlockType.CODE
    if len(block.split("\n")) == len([qline for qline in block.split("\n") if qline[0] == ">"]):
        return BlockType.QUOTE
    if len(block.split("\n")) == len([ulline for ulline in block.split("\n") if ulline[:2] == "- "]):
        return BlockType.UNORDERED_LIST
    ol = True
    for i in range(len(block.split("\n"))):
        split_line = block.split("\n")[i].split(". ")
        if len(split_line) > 1 and split_line[0].isnumeric() and split_line[0] == str(i+1):
            continue
        ol = False
        break
    if ol:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

