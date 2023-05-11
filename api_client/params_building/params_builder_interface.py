from abc import abstractmethod
from api_client.command_id import CommandId


class ParamsBuilderInterface:
    @abstractmethod
    def build(self, **kwargs) -> dict:
        pass
