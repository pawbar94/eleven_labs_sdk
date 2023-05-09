import unittest
from unittest.mock import Mock
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.input_validation.input_validator import InputValidator
from api_client.input_validation.input_validator_interface import InputValidatorInterface


def create_mock_command_input_validators():
    return {command_id: Mock(spec=InputValidatorInterface) for command_id in CommandId}


def create_input_validator(input_validators):
    return InputValidator(input_validators)


class TestInputValidator(unittest.TestCase):
    def test_validate_raises_proper_exception_if_invalid_command_id_provided(self):
        input_validator = create_input_validator({})

        with self.assertRaises(UnknownCommandId):
            input_validator.validate(command_id=-20)

    def test_validate_calls_proper_object_for_the_given_command(self):
        mock_command_input_validators = create_mock_command_input_validators()
        input_validator = create_input_validator(mock_command_input_validators)

        for command_id, command_input_validator in mock_command_input_validators.items():
            input_validator.validate(command_id, some_arg='some_value')
            command_input_validator.validate.assert_called_once_with(some_arg='some_value')
