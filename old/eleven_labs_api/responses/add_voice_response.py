import json
import requests
from old.eleven_labs_api.responses.base_response import BaseResponse
from common.voice_properties.voice import VoiceID


class AddVoiceResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> VoiceID:
        return json.loads(self._raw_response.text)['voice_id']
