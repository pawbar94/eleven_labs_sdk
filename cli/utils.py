import json
from cli.directories import API_KEY_FILE_PATH


def read_api_key() -> str:
    with open(API_KEY_FILE_PATH, 'r') as file:
        return json.load(file)['key']
