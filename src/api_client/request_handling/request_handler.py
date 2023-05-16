from typing import Dict
from requests import Response
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from src.api_client.request_handling.request_handler_interface import RequestHandlerInterface


class RequestHandler:
    def __init__(self, api_key: str, command_request_handlers: Dict[CommandId, RequestHandlerInterface]):
        self.__api_key: str = api_key
        self.__command_request_handlers: Dict[CommandId, RequestHandlerInterface] = command_request_handlers

    def send(self, command_id: CommandId, url: str, params: dict) -> Response:
        if command_id not in self.__command_request_handlers:
            raise UnknownCommandId(f'Unable to send request for the given command - unknown command ID: {command_id}')

        return self.__command_request_handlers[command_id].send(self.__api_key, url, params)
