from abc import abstractmethod
from requests import Response


class RequestHandlerInterface:
    @abstractmethod
    def send(self, api_key: str, url: str, params: dict) -> Response:
        pass
