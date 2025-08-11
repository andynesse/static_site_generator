from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    template = ""
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    try:
        title = extract_title(markdown)
    except Exception:
        title = "untitled"
    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    with open(dest_path, "w", encoding="utf-8") as file:
        written = file.write(template)
        if written != len(template):
            raise Exception(f"did not write to {dest_path} correctly. Expected written chars: {len(template)}, Actual: {written}")