from abc import abstractmethod
from typing import Any
from requests import Response
from api_client.response_handling.exceptions.response_error import ResponseError
from api_client.response_handling.response_handler_interface import ResponseHandlerInterface

SUCCESSFUL_RESPONSE_CODE: int = 200


class BaseResponseHandler(ResponseHandlerInterface):
    def __init__(self):
        super().__init__()

    def process(self, response: Response) -> Any:
        if response.status_code != SUCCESSFUL_RESPONSE_CODE:
            raise ResponseError(f'Unable to process response - status code: {response.status_code}, content: '
                                f'{response.text}')

        return self._get_processed_response(response)

    @abstractmethod
    def _get_processed_response(self, response: Response) -> Any:
        pass
