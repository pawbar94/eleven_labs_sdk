import requests
import json
from common.directories import API_SPEC_FILE_PATH

API_SPEC_URL: str = 'https://api.elevenlabs.io/openapi.json'

api_spec_text: str = requests.get(API_SPEC_URL).text
api_spec = json.loads(api_spec_text)

with open(API_SPEC_FILE_PATH, 'w') as file:
    file.write(json.dumps(api_spec, indent=4))
