from typing import Any
from requests import Response
from api_client.response_handling.base_response_handler import BaseResponseHandler


class EditVoiceSettingsResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        return response.text
