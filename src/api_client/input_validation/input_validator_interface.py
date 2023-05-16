from abc import abstractmethod


class InputValidatorInterface:
    @abstractmethod
    def validate(self, **kwargs) -> None:
        pass
