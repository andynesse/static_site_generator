import os
import shutil
from generate_page import generate_pages_recursive
def main():
    public_path = "./public"
    static_path = "./static"

    clear_content(public_path)

    print(f"Copying files from '{static_path}' to '{public_path}':")
    copy_contents(static_path, public_path)
    print("Copy complete!")
    generate_pages_recursive("./content", "./template.html", "./public")

def clear_content(path):
    print(f"Clearing '{path}' dir:")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
            print("-- Removed", item_path)
        else:
            shutil.rmtree(item_path)
            print("-- Removed", item_path, "and its content")
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