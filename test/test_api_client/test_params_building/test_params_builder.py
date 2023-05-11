import unittest
from unittest.mock import Mock
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.params_building.params_builder import ParamsBuilder
from api_client.params_building.params_builder_interface import ParamsBuilderInterface


def create_mock_command_params_builders():
    return {command_id: Mock(spec=ParamsBuilderInterface) for command_id in CommandId}


def create_params_builder(params_builders):
    return ParamsBuilder(params_builders)


class TestParamsBuilder(unittest.TestCase):
    def test_build_raises_proper_exception_if_invalid_command_id_provided(self):
        params_builder = create_params_builder({})

        with self.assertRaises(UnknownCommandId):
            params_builder.build(command_id=-20, some_arg='some value')

    def test_build_calls_proper_object_for_the_given_command(self):
        mock_command_params_builders = create_mock_command_params_builders()
        params_builder = create_params_builder(mock_command_params_builders)

        for command_id, command_params_builder in mock_command_params_builders.items():
            params_builder.build(command_id, some_arg='some value')
            command_params_builder.build.assert_called_once()
