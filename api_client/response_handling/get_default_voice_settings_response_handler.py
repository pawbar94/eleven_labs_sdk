import json
from typing import Any
from requests import Response
from api_client.response_handling.base_response_handler import BaseResponseHandler
from api_client.response_handling.utils import create_voice_settings


class GetDefaultVoiceSettingsResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return create_voice_settings(data)
