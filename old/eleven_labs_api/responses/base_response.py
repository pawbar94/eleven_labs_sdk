from typing import Any

import requests
from old.eleven_labs_api.responses.response_interface import ResponseInterface


class BaseResponse(ResponseInterface):
    def __init__(self, raw_response: requests.Response):
        self._raw_response: requests.Response = raw_response

    def process(self) -> Any:
        if self.__is_response_invalid():
            raise RuntimeError(self._raw_response.text)

        return self._get_processed_response()

    def __is_response_invalid(self) -> bool:
        return self._raw_response.status_code != 200
