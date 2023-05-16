from typing import Dict, Any
from requests import Response
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from src.api_client.response_handling.response_handler_interface import ResponseHandlerInterface


class ResponseHandler:
    def __init__(self, command_response_handlers: Dict[CommandId, ResponseHandlerInterface]):
        self.__command_response_handlers: Dict[CommandId, ResponseHandlerInterface] = command_response_handlers

    def process(self, command_id: CommandId, response: Response) -> Any:
        if command_id not in self.__command_response_handlers:
            raise UnknownCommandId(f'Unable to process response for the given command - unknown command ID: {command_id}')

        return self.__command_response_handlers[command_id].process(response)
