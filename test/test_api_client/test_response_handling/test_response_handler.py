import unittest
from unittest.mock import Mock
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.response_handling.response_handler import ResponseHandler
from api_client.response_handling.response_handler_interface import ResponseHandlerInterface
from requests import Response


def create_mock_command_response_handlers():
    return {command_id: Mock(spec=ResponseHandlerInterface) for command_id in CommandId}


def create_response_handler(response_handlers):
    return ResponseHandler(response_handlers)


class TestResponseHandler(unittest.TestCase):
    def test_build_raises_proper_exception_if_invalid_command_id_provided(self):
        response_handler = create_response_handler({})

        with self.assertRaises(UnknownCommandId):
            response_handler.process(command_id=-20, response=Response())

    def test_build_calls_proper_object_for_the_given_command(self):
        mock_command_response_handlers = create_mock_command_response_handlers()
        response_handler = create_response_handler(mock_command_response_handlers)
        response = Response()

        for command_id, command_response_handler in mock_command_response_handlers.items():
            response_handler.process(command_id, response=response)
            command_response_handler.process.assert_called_once_with(response)
