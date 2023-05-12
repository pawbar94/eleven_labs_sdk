from abc import abstractmethod
from typing import Any
from requests import Response


class ResponseHandlerInterface:
    @abstractmethod
    def process(self, response: Response) -> Any:
        pass
