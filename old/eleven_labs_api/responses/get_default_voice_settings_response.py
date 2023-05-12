import requests
import json
from old.eleven_labs_api.responses.base_response import BaseResponse
from old.eleven_labs_api.responses.voice_model.voice_factory import VoiceFactory
from common.voice.voice_settings import VoiceSettings


class GetDefaultVoiceSettingsResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> VoiceSettings:
        return VoiceFactory.create_voice_settings(json.loads(self._raw_response.text))
