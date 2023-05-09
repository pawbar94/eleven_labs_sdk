from old.eleven_labs_api.requests.exceptions.empty_voice_name import EmptyVoiceName
from old.eleven_labs_api.requests.exceptions.no_sample_files_provided import NoSampleFilesProvided
from old.eleven_labs_api.requests.request_interface import RequestInterface


class AddVoiceRequest(RequestInterface):
    def __init__(self, name: str, files: list, description: str, labels: str):
        if not name:
            raise EmptyVoiceName('Voice name cannot be empty!')
        if not files:
            raise NoSampleFilesProvided('No sample files provided!')

        self.__name: str = name
        self.__files: list = files
        self.__description: str = description
        self.__labels: str = labels

    def uri(self) -> str:
        return f'/v1/voices/add'

    def payload(self) -> dict:
        return {
            "name": self.__name,
            "files": self.__files,
            "description": self.__description,
            "labels": self.__labels
        }
