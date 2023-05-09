from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetVoiceRequest(RequestInterface):
    def __init__(self, voice_id: str):
        if not voice_id:
            raise EmptyVoiceId('Voice id cannot be empty!')

        self.__voice_id: str = voice_id

    def uri(self) -> str:
        return f'/v1/voices/{self.__voice_id}'

    def payload(self) -> dict:
        return {}
