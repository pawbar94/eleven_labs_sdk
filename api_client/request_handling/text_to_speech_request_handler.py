from requests import Response
from api_client.request_code import RequestCode
from api_client.request_handling.base_request_handler import BaseRequestHandler


class TextToSpeechRequestHandler(BaseRequestHandler):
    def __init__(self):
        super().__init__()

    def send(self, api_key: str, url: str, params: dict) -> Response:
        return self._execute_request(api_key, RequestCode.POST, url, params)
