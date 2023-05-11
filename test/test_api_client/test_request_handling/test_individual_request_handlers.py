import unittest
from unittest.mock import MagicMock, patch
from api_client.request_code import RequestCode
from api_client.request_handling.base_request_handler import BaseRequestHandler
from api_client.request_handling.get_default_voice_settings_request_handler import GetDefaultVoiceSettingsRequestHandler
from api_client.request_handling.get_models_request_handler import GetModelsRequestHandler
from api_client.request_handling.get_voice_settings_request_handler import GetVoiceSettingsRequestHandler
from api_client.request_handling.get_voices_request_handler import GetVoicesRequestHandler
from api_client.request_handling.text_to_speech_request_handler import TextToSpeechRequestHandler


class TestTextToSpeechRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = TextToSpeechRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.POST, 'some url', {'key': 'value'})


class TestGetModelsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetModelsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetVoicesRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetVoicesRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetDefaultVoiceSettingsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetDefaultVoiceSettingsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetVoiceSettingsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetVoiceSettingsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})
