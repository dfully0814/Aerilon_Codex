import os
import re
import sys
import markdown
import chardet
import notion_service

CHILD_DIRECTORIES = [
    "Characters",
    "Locations",
    "Lore",
    "NPCs",
    "Organizations",
    "Vessels",
    "Session Recaps"
]

def find_dir_name(file_path):
    head, tail = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(tail)
    return file_name


def build_page_metadata_dict() -> dict:
    """Builds a dictionary of page meatadata to use for generating instance of notion pages"""
    # a collection for adding unique matches in order to create these in the notion database later
    page_names_with_dir = {}

    # Define the regular expression pattern to search for
    pattern = re.compile(r'\[\[.*?\]\]')
    
    for child_dir_name in CHILD_DIRECTORIES:
        child_dir_path = os.path.join("/Users/d.fuller/Library/CloudStorage/OneDrive-Personal/Aerilon_Vault/Codex", child_dir_name)
        for dir_path, directories, file_names in os.walk(child_dir_path):
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                if (os.path.isfile(file_path)):
                    with open(file_path, 'r') as file:
                        page_names_with_dir.update(
                            {
                                file_name: {
                                    "containing_dir": child_dir_name,
                                    "contents": file.read()
                                }
                            }
                        )
                        
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


def to_html(page_text):
    return markdown.markdown(page_text)

pages_dict = build_page_metadata_dict()
print(pages_dict)
