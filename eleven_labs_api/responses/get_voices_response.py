import requests
import json
from typing import List
from eleven_labs_api.responses.base_response import BaseResponse
from eleven_labs_api.responses.voice_model.voice import Voice
from eleven_labs_api.responses.voice_model.voice_factory import VoiceFactory
from logging import getLogger

logger = getLogger('GetVoicesResponse')


class GetVoicesResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> List[Voice]:
        voices: List[Voice] = []

        for voice_properties in json.loads(self._raw_response.text)['voices']:
            voices.append(VoiceFactory.create(voice_properties))

        logger.debug(f'Received {len(voices)} voices')

        return voices
