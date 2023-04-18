import requests
import json
from eleven_labs_api.responses.base_response import BaseResponse
from eleven_labs_api.responses.voice_model.voice import Voice
from eleven_labs_api.responses.voice_model.voice_factory import VoiceFactory


class GetVoiceResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> Voice:
        return VoiceFactory.create(json.loads(self._raw_response.text))
