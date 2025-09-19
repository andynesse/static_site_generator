import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
        splitted = node.text.split(delimiter)
        # If delimiters are not paired, treat as plain text
        if len(splitted) % 2 == 0:
            # Even number of splits means trailing delimiter or unbalanced
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        for i, part in enumerate(splitted):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        splitted = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        converted = [TextNode(splitted.pop(0), TextType.TEXT)]
        for i in range(len(images)):
            converted.extend([
                TextNode(splitted[i*3], TextType.IMAGE, splitted[i*3+1]), 
                TextNode(splitted[i*3+2], TextType.TEXT)
            ])
        new_nodes.extend([text_node for text_node in converted if text_node.text != "" or text_node.text_type != TextType.TEXT])
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        splitted = re.split(r"(?<!!)\[(.*?)\]\((.*?)\)", node.text)
        converted = [TextNode(splitted.pop(0), TextType.TEXT)]
        for i in range(len(links)):
            converted.extend([
                TextNode(splitted[i*3], TextType.LINK, splitted[i*3+1]), 
                TextNode(splitted[i*3+2], TextType.TEXT)
            ])
        new_nodes.extend([text_node for text_node in converted if text_node.text != "" or text_node.text_type != TextType.TEXT])
    return new_nodes