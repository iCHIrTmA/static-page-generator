from markdown_blocks import *
from extract_text import *
from generate_page import *
import os
import shutil

def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str):
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # get items in a dir
    for file_name in os.listdir(dir_path_content):
        # print(filename)
        # print (f"generate_pages_recursive; file+name: {filename}")

        file_path = os.path.join(dir_path_content, file_name)
        print (f"file_path: {file_path}")
        if os.path.isfile(file_path):
            # os.remove(file_path)
            dest_path = f"{dest_dir_path}{file_name}"
            dest_path = dest_path.replace("md", "html")
            generate_page(from_path=file_path, template_path=template_path, dest_path=dest_path)
            continue
        if os.path.isdir(file_path):
            dest_path = f"{dest_dir_path}{file_name}/"
            print("destination directory:", dest_path)
            print("does dir exists?", os.path.exists(dest_path))
            if os.path.exists(dest_path) is False:
                os.mkdir(dest_path)
            print("does dir exists?", os.path.exists(dest_path))
            generate_pages_recursive(dir_path_content=file_path, template_path=template_path, dest_dir_path=dest_path)
            continue
        # try:
        #     if os.path.isfile(file_path):
        #         os.remove(file_path)  
        #     elif os.path.isdir(file_path):  
        #         shutil.rmtree(file_path)  
        # except Exception as e:  
        #     print(f"Error deleting {file_path}: {e}")

    # loop over items in a dir 
    # for item in dir_contents:
    #     if item is dir:
    #         generate_pages_recursive()
    #         continue

    #     if item is file:
    #         generate_page()
    #         continue
    
