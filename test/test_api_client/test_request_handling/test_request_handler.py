import unittest
from unittest.mock import Mock
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from src.api_client.request_handling.request_handler import RequestHandler
from src.api_client.request_handling.request_handler_interface import RequestHandlerInterface

API_KEY = '123'


def create_mock_command_request_handlers():
    return {command_id: Mock(spec=RequestHandlerInterface) for command_id in CommandId}


def create_request_handler(request_handlers):
    return RequestHandler(API_KEY, request_handlers)


class TestRequestHandler(unittest.TestCase):
    def test_build_raises_proper_exception_if_invalid_command_id_provided(self):
        request_handler = create_request_handler({})

        with self.assertRaises(UnknownCommandId):
            request_handler.send(command_id=-20, url='some url', params={'some param': 'some value'})

    def test_build_calls_proper_object_for_the_given_command(self):
        mock_command_request_handlers = create_mock_command_request_handlers()
        request_handler = create_request_handler(mock_command_request_handlers)

        for command_id, command_request_handler in mock_command_request_handlers.items():
            request_handler.send(command_id, url='some url', params={'some param': 'some value'})
            command_request_handler.send.assert_called_once_with(API_KEY, 'some url', {'some param': 'some value'})
