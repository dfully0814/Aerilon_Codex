import os
import re
import sys
import markdown
import chardet

CHILD_DIRECTORIES = [
    "Characters",
    "Locations",
    "Lore",
    "NPCs",
    "Organizations",
    "Vessels",
    "Session Recaps"
]

pages_dict = {}


def find_dir_name(file_path):
    head, tail = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(tail)
    return file_name


def find_page_names():
    # a collection for adding unique matches in order to create these in the notion database later
    page_names_with_dir = {}

    # Define the regular expression pattern to search for
    # pattern = re.compile(r'\[\[.*?\]\]')
    
    for child_dir_name in CHILD_DIRECTORIES:
        child_dir_path = os.path.join("/Users/d.fuller/Library/CloudStorage/OneDrive-Personal/Aerilon_Vault/Codex", child_dir_name)
        for dir_path, directories, file_names in os.walk(child_dir_path):
            for file_name in file_names:
                page_names_with_dir.update(
                    {
                        file_name: child_dir_name
                    }
                )
                # file_path = os.path.join(dir_path, file_name)
                # if (os.path.isfile(file_path)):
                #     with open(file_path, 'rb') as file:
                #         file_contents_binary = file.read()
                        
                #         file_contents_encoding = chardet.detect(file_contents_binary).get("encoding")
                #         if (file_contents_encoding is None):
                #             file_contents_encoding = "utf-8"
                #         file_contents_decoded = file_contents_binary.decode(
                #             file_contents_encoding
                #         )
                        
                #         for match in re.findall(pattern, file_contents_decoded):
                #             match = match[2:-2]
                #             page_names.add(match)
                            
    return page_names_with_dir


def find_markdown_file(directory, filename):
    """Search for a Markdown file with a specific name in a directory and its sub-directories, and return its contents."""
    for root, dirs, files in os.walk(directory):
        if filename in files:
            # If the file exists in the current directory, open it and read the contents
            try:
                with open(os.path.join(root, filename), 'r') as file:
                    page_text = file.read()
                    return page_text
            except FileNotFoundError:
                print(f"{filename} not found.")


def to_html(page_text):
    return markdown.markdown(page_text)

print(find_page_names())
