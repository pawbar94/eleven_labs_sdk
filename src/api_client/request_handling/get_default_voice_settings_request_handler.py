from requests import Response
from src.common.enums.request_code import RequestCode
from src.api_client.request_handling.base_request_handler import BaseRequestHandler


class GetDefaultVoiceSettingsRequestHandler(BaseRequestHandler):
    def __init__(self):
        super().__init__()

    def send(self, api_key: str, url: str, params: dict) -> Response:
        return self._execute_request(api_key, RequestCode.GET, url, params)
