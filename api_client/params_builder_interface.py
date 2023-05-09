from abc import abstractmethod
from api_client.command_id import CommandId


class ParamsBuilderInterface:
    @abstractmethod
    def build(self, command_id: CommandId, **kwargs) -> dict:
        pass
