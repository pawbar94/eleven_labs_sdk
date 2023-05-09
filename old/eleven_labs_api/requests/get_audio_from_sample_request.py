from old.eleven_labs_api.requests.exceptions.empty_sample_id import EmptySampleId
from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetAudioFromSampleRequest(RequestInterface):
    def __init__(self, voice_id: str, sample_id: str):
        if not voice_id:
            raise EmptyVoiceId('Voice ID cannot be empty!')
        if not sample_id:
            raise EmptySampleId('Sample ID cannot be empty!')

        self.__voice_id: str = voice_id
        self.__sample_id: str = sample_id

    def uri(self) -> str:
        return f'/v1/voices/{self.__voice_id}/samples/{self.__sample_id}/audio'

    def payload(self) -> dict:
        return {}
