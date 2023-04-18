from abc import abstractmethod
from typing import Any


class ResponseInterface:
    @abstractmethod
    def process(self) -> Any:
        pass

    @abstractmethod
    def _get_processed_response(self) -> Any:
        pass
