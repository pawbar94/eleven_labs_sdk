import os

SCRIPT_DIR: str = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIR: str = os.path.join(SCRIPT_DIR, '..', 'config')
SPEC_FILE_NAME: str = 'openapi.json'
API_SPEC_FILE_PATH: str = os.path.join(CONFIG_DIR, SPEC_FILE_NAME)
