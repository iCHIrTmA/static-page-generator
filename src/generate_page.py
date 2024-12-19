from markdown_blocks import *
from extract_text import *

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, 'r', encoding="utf-8")
    markdown = from_file.read()
    # print(markdown)

    template_file = open(template_path, 'r', encoding="utf-8")
    template = template_file.read()
    # print(template)

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    # print(title)
    # print(content)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", content)

    # print(page)
    with open(dest_path, 'w') as file:
        file.write(page)

