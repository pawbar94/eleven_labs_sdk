from abc import abstractmethod
from typing import Any

from api_client.command_id import CommandId


class ResponseHandlerInterface:
    @abstractmethod
    def process(self, command_id: CommandId, response: bytes) -> Any:
        pass
