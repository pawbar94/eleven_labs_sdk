from typing import Dict
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.params_building.params_builder_interface import ParamsBuilderInterface


class ParamsBuilder:
    def __init__(self, command_params_builders: Dict[CommandId, ParamsBuilderInterface]):
        self.__command_params_builders: Dict[CommandId, ParamsBuilderInterface] = command_params_builders

    def build(self, command_id: CommandId, **kwargs) -> None:
        if command_id not in self.__command_params_builders:
            raise UnknownCommandId(f'Unable to build params for the given command - unknown command ID: {command_id}')

        self.__command_params_builders[command_id].build(**kwargs)
