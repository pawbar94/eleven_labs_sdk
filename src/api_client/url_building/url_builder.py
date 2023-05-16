from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from src.api_client.url_building.url_builder_interface import UrlBuilderInterface


class UrlBuilder:
    def __init__(self, command_url_builders: Dict[CommandId, UrlBuilderInterface]):
        self.__command_url_builders: Dict[CommandId, UrlBuilderInterface] = command_url_builders

    def build(self, command_id: CommandId, **kwargs) -> str:
        if command_id not in self.__command_url_builders:
            raise UnknownCommandId(f'Unable to build URL for the given command - unknown command ID: {command_id}')

        return self.__command_url_builders[command_id].build(**kwargs)
