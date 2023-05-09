from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.request_interface import RequestInterface


class EditVoiceRequest(RequestInterface):
    def __init__(self, voice_id: str, name: str, files: list, description: str, labels: str):
        if not voice_id:
            raise EmptyVoiceId("Voice id cannot be empty")

        self.__voice_id: str = voice_id
        self.__name: str = name
        self.__files: list = files
        self.__description: str = description
        self.__labels: str = labels

    def uri(self) -> str:
        return f'/v1/voices/{self.__voice_id}/edit'

    def payload(self) -> dict:
        return {
            "name": self.__name,
            "files": self.__files,
            "description": self.__description,
            "labels": self.__labels
        }
