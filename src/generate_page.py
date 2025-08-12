import os
from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
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

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    with open(dest_path, "w", encoding="utf-8") as file:
        written = file.write(template)
        if written != len(template):
            raise Exception(f"did not write to {dest_path} correctly. Expected written chars: {len(template)}, Actual: {written}")
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dirlist = os.listdir(dir_path_content)
    for item in dirlist:
        path = os.path.join(dir_path_content, item)
        if os.path.isfile(path):
            generate_page(path, template_path, os.path.join(dest_dir_path, item.replace(".md", ".html")), basepath)
            continue
        os.mkdir(os.path.join(dest_dir_path, item))
        generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, item), basepath)