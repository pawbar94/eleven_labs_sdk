from abc import abstractmethod


class RequestInterface:
    @abstractmethod
    def uri(self) -> str:
        pass

    @abstractmethod
    def payload(self) -> dict:
        pass
