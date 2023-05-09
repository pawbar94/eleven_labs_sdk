from abc import abstractmethod
from api_client.command_id import CommandId


class UrlBuilderInterface:
    @abstractmethod
    def build(self, command_id: CommandId) -> str:
        pass
