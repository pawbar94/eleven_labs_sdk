from typing import Dict
from requests import Response
import requests
from api_client.request_code import RequestCode
from api_client.request_handling.exceptions.unknown_request_code import UnknownRequestCode
from api_client.request_handling.request_handler_interface import RequestHandlerInterface


class BaseRequestHandler(RequestHandlerInterface):
    def __init__(self):
        super().__init__()

    def _execute_request(self, api_key: str, request_code: RequestCode, url: str, params: dict) -> Response:
        args: dict = {
            'headers': self.__create_headers(api_key),
        }

        if params:
            args['json'] = params

        if request_code == RequestCode.GET:
            response: Response = requests.get(url, **args)
        elif request_code == RequestCode.POST:
            response: Response = requests.post(url, **args)
        elif request_code == RequestCode.DELETE:
            response: Response = requests.delete(url, **args)
        else:
            raise UnknownRequestCode(f'Unknown request code: {request_code}')

        return response

    def __create_headers(self, api_key: str) -> dict:
        headers: Dict[str, str] = {
            'xi-api-key': api_key,
            'Content-Type': 'application/json'
        }

        return headers
