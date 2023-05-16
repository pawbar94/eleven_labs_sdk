import json
from typing import Any
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler


class AddVoiceResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return data['voice_id']
