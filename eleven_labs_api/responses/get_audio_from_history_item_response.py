import requests
from eleven_labs_api.responses.base_response import BaseResponse


class GetAudioFromHistoryItemResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response, output_file_path: str):
        super().__init__(raw_response)
        self.__output_file_path: str = output_file_path

    def _get_processed_response(self) -> None:
        with open(self.__output_file_path, 'wb') as file:
            file.write(self._raw_response.content)
