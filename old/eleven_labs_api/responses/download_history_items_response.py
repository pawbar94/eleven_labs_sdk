from typing import List

import requests
from old.eleven_labs_api.responses.base_response import BaseResponse


class DownloadHistoryItemsResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response, history_items_ids: List[str], output_file_path: str):
        super().__init__(raw_response)
        self.__history_items_ids: List[str] = history_items_ids
        self.__output_file_path: str = output_file_path

    def _get_processed_response(self) -> None:
        if len(self.__history_items_ids) > 1:
            dot_index: int = self.__output_file_path.rfind('.')
            self.__output_file_path = self.__output_file_path[:dot_index] + '.zip'

        with open(self.__output_file_path, 'wb') as file:
            file.write(self._raw_response.content)
