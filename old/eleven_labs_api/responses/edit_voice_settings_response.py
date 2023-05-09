import requests
from old.eleven_labs_api.responses.base_response import BaseResponse


class EditVoiceSettingsResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> str:
        return self._raw_response.text
