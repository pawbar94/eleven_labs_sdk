import unittest
from unittest.mock import Mock
from api_client.command_id import CommandId
from api_client.input_validation.exceptions.unknown_command_id import UnknownCommandId
from api_client.url_building.url_builder import UrlBuilder
from api_client.url_building.url_builder_interface import UrlBuilderInterface


def create_mock_command_url_builders():
    return {command_id: Mock(spec=UrlBuilderInterface) for command_id in CommandId}


def create_url_builder(url_builders):
    return UrlBuilder(url_builders)


class TestUrlBuilder(unittest.TestCase):
    def test_build_raises_proper_exception_if_invalid_command_id_provided(self):
        url_builder = create_url_builder({})

        with self.assertRaises(UnknownCommandId):
            url_builder.build(command_id=-20, some_arg='some value')

    def test_build_calls_proper_object_for_the_given_command(self):
        mock_command_url_builders = create_mock_command_url_builders()
        url_builder = create_url_builder(mock_command_url_builders)

        for command_id, command_url_builder in mock_command_url_builders.items():
            url_builder.build(command_id, some_arg='some value')
            command_url_builder.build.assert_called_once()
