import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if not delimiter in node.text:
            new_nodes.append(node)
            continue
        splitted = node.text.split(delimiter)
        if len(splitted) < 3 or len(splitted) % 2 == 0:
            raise Exception(f'Text node have trailing delimiter or too many delimiters: Expected count of {delimiter} to be 2')
        for i in range(len(splitted) // 2):
            if i == 0:
                converted = [
                    TextNode(splitted[0], TextType.TEXT),
                    TextNode(splitted[1], text_type),
                    TextNode(splitted[2], TextType.TEXT)
                ]
            else:
                converted = [
                    TextNode(splitted[i*3], text_type),
                    TextNode(splitted[i*3+1], TextType.TEXT)
                ]
            new_nodes.extend([text_node for text_node in converted if text_node.text != ""])
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