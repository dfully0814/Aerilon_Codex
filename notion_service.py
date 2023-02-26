import requests
import json
from notion_page import NotionPage

DATABASE_ID = "dc8f63b3bc874a93818676af32fbad0e"
APIKEY = "secret_iYKxuQGT0MZ9Y0XCJPf5GL7NKrb0a0NoewxMkjPUEao"

PAGES_URL = "https://api.notion.com/v1/pages"

def get_page(metadata) -> NotionPage:
    """Gets an instance of a notion page"""
    return NotionPage(metadata, DATABASE_ID)

def get_request_headers():
    return {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
        "Authorization": f"Bearer {APIKEY}"
    }

def get_request_body():
    return {
        "parent": {
            "type": "database_id",
            "database_id": DATABASE_ID,
        },
        "properties": {
            "Name": {
                "type": "title",
                "title": [{
                    "type": "text",
                    "text": {
                        "content": "Tomatoes"
                    }
                }]
            }
        }
    }

# response = requests.post(PAGES_URL, json=get_request_body(), headers=get_request_headers())