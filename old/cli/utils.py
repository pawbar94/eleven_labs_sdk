import json
import os.path
from old.cli.directories import API_KEY_FILE_PATH


def read_api_key() -> str:
    with open(API_KEY_FILE_PATH, 'r') as file:
        key: str = json.load(file)['key']

    if not key or key == 'YOUR_API_KEY':
        raise ValueError(f'Missing API key! Please add your API key to {os.path.abspath(API_KEY_FILE_PATH)} file.')

    return key


def get_file_extension(file_path: str) -> str:
    if '.' not in file_path:
        raise ValueError(f'Invalid file path: {file_path}! The file path must contain a file extension.')

    return file_path.split('.')[-1]
