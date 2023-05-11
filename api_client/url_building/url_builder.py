from typing import Dict
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.url_building.url_builder_interface import UrlBuilderInterface


class UrlBuilder:
    def __init__(self, command_url_builders: Dict[CommandId, UrlBuilderInterface]):
        self.__command_url_builders: Dict[CommandId, UrlBuilderInterface] = command_url_builders

    def build(self, command_id: CommandId, **kwargs) -> None:
        if command_id not in self.__command_url_builders:
            raise UnknownCommandId(f'Unable to build URL for the given command - unknown command ID: {command_id}')

        self.__command_url_builders[command_id].build(**kwargs)
