from typing import Dict, Type, Tuple

from api_client.input_validation.input_validator_interface import InputValidatorInterface


class BaseInputValidator(InputValidatorInterface):
    def __init__(self):
        super().__init__()

    def _check_existence(self, required_args: Dict[str, Type[Exception]], command_name: str, **kwargs) -> None:
        for argument_name, exception in required_args.items():
            if argument_name not in kwargs:
                raise exception(f'Missing {argument_name} argument in the arguments provided for {command_name} '
                                f'command.')

    def _check_if_empty(self, required_args: Dict[str, Type[Exception]], command_name: str, **kwargs) -> None:
        for argument_name, exception in required_args.items():
            if not kwargs[argument_name]:
                raise exception(f'{argument_name} provided for {command_name} command cannot be empty.')

    def _check_if_in_range(self, required_args: Dict[str, Type[Exception]], required_ranges: Dict[str, Tuple[int, int]],
                           command_name: str, **kwargs) -> None:
        for argument_name, exception in required_args.items():
            if kwargs[argument_name] < required_ranges[argument_name][0] or kwargs[argument_name] > required_ranges[argument_name][1]:
                raise exception(f'{argument_name} provided for {command_name} command must be between '
                                f'{required_ranges[argument_name][0]} and {required_ranges[argument_name][1]}.')
