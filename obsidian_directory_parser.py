import os
import re
import sys
import markdown

CHILD_DIRECTORIES = [
    "Characters",
    "Locations",
    "Lore",
    "NPCs",
    "Organizations",
    "Vessels",
    "Session Recaps",
    "Uncharted North"
]


def find_dir_name(file_path):
    head, tail = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(tail)
    return file_name


def find_page_names(parent_directory, directories):
    # Collection for adding unique matches in order to create these in the notion database later
    page_names = set()

    pages = {}

    # Define the regular expression pattern to search for
    pattern = re.compile(r'\[\[(?!.*\.(?:jpg|png|webp|bmp|jpeg)).*?\]\]')

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Error: missing parent directory path argument.")
            print("Usage: python script.py <parent_directory_path>")
            sys.exit(1)

    for dir_name in directories:
        dir_path = os.path.join(parent_directory, dir_name)
        for dir_path, dir_names, file_names in os.walk(dir_path):
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                if (os.path.isfile(file_path)):
                    with open(file_path, 'r', encoding="utf-8") as file:
                        for line in file:
                            for match in re.findall(pattern, line):
                                page_name = match[2:-2]
                                pages.update(
                                    {
                                        page_name: find_markdown_file(parent_directory, page_name)
                                    }
                                )
    print(pages.get('Thryn'))


def find_markdown_file(directory, filename):
    """Search for a Markdown file with a specific name in a directory and its sub-directories, and return its contents."""
    for root, dirs, files in os.walk(directory):
        if filename in files:
            # If the file exists in the current directory, open it and read the contents
            try:
                with open(os.path.join(root, filename), 'r') as file:
                    page_text = file.read()
            except FileNotFoundError:
                print(f"{filename} not found.")
            
            return markdown.markdown(page_text)

    # If the file is not found, return None
    return None


def to_html(page_text):
    return markdown.markdown(page_text)


PARENT_DIRECTORY = sys.argv[1]
find_page_names(PARENT_DIRECTORY, CHILD_DIRECTORIES)
