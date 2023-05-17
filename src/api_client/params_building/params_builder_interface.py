from abc import abstractmethod


class ParamsBuilderInterface:
    @abstractmethod
    def build(self, **kwargs) -> dict:
        pass
