import requests
import logging
from typing import Dict
from api_client.request_code import RequestCode

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logger = logging.getLogger('RequestSender')

ELEVEN_LABS_API_URL: str = 'https://api.elevenlabs.io'


class RequestSender:
    @staticmethod
    def send(request_code: RequestCode, api_key: str, uri: str, params: dict, accept_content: str = '') -> requests.Response:
        logger.debug(f'Sending {request_code} request to {RequestSender.__create_url(uri)} with headers '
                     f'{RequestSender.__create_headers(api_key, accept_content)}, params {params} and accept content '
                     f'"{accept_content}"')

        if request_code == RequestCode.GET:
            if params:
                response = requests.get(RequestSender.__create_url(uri),
                                        headers=RequestSender.__create_headers(api_key, accept_content), json=params)
            else:
                response = requests.get(RequestSender.__create_url(uri),
                                        headers=RequestSender.__create_headers(api_key, accept_content))
        elif request_code == RequestCode.POST:
            if params:
                response = requests.post(RequestSender.__create_url(uri),
                                         headers=RequestSender.__create_headers(api_key, accept_content), json=params)
            else:
                response = requests.post(RequestSender.__create_url(uri),
                                         headers=RequestSender.__create_headers(api_key, accept_content))
        elif request_code == RequestCode.DELETE:
            if params:
                response = requests.delete(RequestSender.__create_url(uri),
                                           headers=RequestSender.__create_headers(api_key, accept_content), json=params)
            else:
                response = requests.delete(RequestSender.__create_url(uri),
                                           headers=RequestSender.__create_headers(api_key, accept_content))
        else:
            raise RuntimeError(f'Unknown request code: {request_code}')

        logger.debug(f'Received response: {response.content}')

        return response

    @staticmethod
    def __create_url(uri: str) -> str:
        return ELEVEN_LABS_API_URL + uri

    @staticmethod
    def __create_headers(api_key: str, accept_content: str) -> dict:
        headers: Dict[str, str] = {
            'xi-api-key': api_key,
            'Content-Type': 'application/json'
        }

        if accept_content:
            headers['accept'] = accept_content

        return headers
