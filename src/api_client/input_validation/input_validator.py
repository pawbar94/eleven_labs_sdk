from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from src.api_client.input_validation.input_validator_interface import InputValidatorInterface


class InputValidator:
    def __init__(self, command_input_validators: Dict[CommandId, InputValidatorInterface]):
        self.__command_input_validators: Dict[CommandId, InputValidatorInterface] = command_input_validators

    def validate(self, command_id: CommandId, **kwargs) -> None:
        if command_id not in self.__command_input_validators:
            raise UnknownCommandId(f'Unable to validate input for the given command - unknown command ID: {command_id}')

        self.__command_input_validators[command_id].validate(**kwargs)
