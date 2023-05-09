from abc import abstractmethod
from api_client.request_code import RequestCode


class RequestHandlerInterface:
    @abstractmethod
    def send(self, request_code: RequestCode, url: str, params: dict) -> bytes:
        pass
