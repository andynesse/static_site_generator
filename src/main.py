import os
import shutil
import sys

from generate_page import generate_pages_recursive
def main():
    basepath = sys.argv[0]
    if basepath == "":
        basepath = "/"
    
    docs_path = "./docs"
    static_path = "./static"
    content_path = "./content"

    clear_content(docs_path)

    print(f"Copying files from '{static_path}' to '{docs_path}':")
    copy_contents(static_path, docs_path)
    print("Copy complete!")
    generate_pages_recursive(content_path, "./template.html", docs_path, basepath)

def clear_content(path):
    print(f"Clearing '{path}' dir:")
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                print("-- Removed", item_path)
            else:
                shutil.rmtree(item_path)
                print("-- Removed", item_path, "and its content")
    else:
        os.mkdir(path)
    print("Directory cleared!\n")

def copy_contents(from_path, to_path):        
    dirlist = os.listdir(from_path)
    for item in dirlist:
        item_path = os.path.join(from_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, to_path)
            print(f"-- Added '{item_path}' to '{to_path}'")
            continue
        os.mkdir(os.path.join(to_path, item))
        print(f"-- Created dir: '{os.path.join(to_path, item)}'")
        copy_contents(item_path, os.path.join(to_path, item))


if __name__ == "__main__":
    main()