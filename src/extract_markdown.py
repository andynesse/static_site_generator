import re
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown):
    return [block for block in [splitted.strip() for splitted in markdown.split("\n\n")] if block != ""]

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    h1 = None
    for block in blocks:
        if block[0] == "#" and not "\n" in block and len(block) - len(block.lstrip("#")) == 1:
            return block[1:].strip()
        raise Exception("Error: no h1 header found")