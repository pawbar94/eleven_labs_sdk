from abc import abstractmethod


class UrlBuilderInterface:
    @abstractmethod
    def build(self, **kwargs) -> str:
        pass
