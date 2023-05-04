import os

SCRIPT_DIR: str = os.path.dirname(os.path.realpath(__file__))
CLI_CONFIG_DIR: str = os.path.join(SCRIPT_DIR, 'config')
API_KEY_FILE_PATH: str = os.path.join(CLI_CONFIG_DIR, 'api_key.json')
