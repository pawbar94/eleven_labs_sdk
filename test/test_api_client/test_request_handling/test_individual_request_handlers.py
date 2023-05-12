import unittest
from unittest.mock import MagicMock, patch
from api_client.request_code import RequestCode
from api_client.request_handling.add_voice_request_handler import AddVoiceRequestHandler
from api_client.request_handling.base_request_handler import BaseRequestHandler
from api_client.request_handling.delete_history_item_request_handler import DeleteHistoryItemRequestHandler
from api_client.request_handling.delete_sample_request_handler import DeleteSampleRequestHandler
from api_client.request_handling.delete_voice_request_handler import DeleteVoiceRequestHandler
from api_client.request_handling.download_history_items_request_handler import DownloadHistoryItemsRequestHandler
from api_client.request_handling.edit_voice_request_handler import EditVoiceRequestHandler
from api_client.request_handling.edit_voice_settings_request_handler import EditVoiceSettingsRequestHandler
from api_client.request_handling.get_audio_from_history_item_request_handler import \
    GetAudioFromHistoryItemRequestHandler
from api_client.request_handling.get_audio_from_sample_request_handler import GetAudioFromSampleRequestHandler
from api_client.request_handling.get_default_voice_settings_request_handler import GetDefaultVoiceSettingsRequestHandler
from api_client.request_handling.get_generated_items_request_handler import GetGeneratedItemsRequestHandler
from api_client.request_handling.get_history_item_request_handler import GetHistoryItemRequestHandler
from api_client.request_handling.get_models_request_handler import GetModelsRequestHandler
from api_client.request_handling.get_user_info_request_handler import GetUserInfoRequestHandler
from api_client.request_handling.get_user_subscription_info_request_handler import GetUserSubscriptionInfoRequestHandler
from api_client.request_handling.get_voice_request_handler import GetVoiceRequestHandler
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


class TestGetVoiceRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetVoiceRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestDeleteVoiceRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = DeleteVoiceRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.DELETE, 'some url',
                                                         {'key': 'value'})


class TestEditVoiceSettingsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = EditVoiceSettingsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.POST, 'some url', {'key': 'value'})


class TestAddVoiceRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = AddVoiceRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.POST, 'some url', {'key': 'value'})


class TestEditVoiceRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = EditVoiceRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.POST, 'some url', {'key': 'value'})


class TestDeleteSampleRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = DeleteSampleRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.DELETE, 'some url',
                                                         {'key': 'value'})


class TestGetAudioFromSampleRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetAudioFromSampleRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetGeneratedItemsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetGeneratedItemsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetHistoryItemRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetHistoryItemRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestDeleteHistoryItemRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = DeleteHistoryItemRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.DELETE, 'some url',
                                                         {'key': 'value'})


class TestGetAudioFromHistoryItemRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetAudioFromHistoryItemRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestDownloadHistoryItemsRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = DownloadHistoryItemsRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.POST, 'some url', {'key': 'value'})


class TestGetUserSubscriptionInfoRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetUserSubscriptionInfoRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})


class TestGetUserInfoRequestHandler(unittest.TestCase):
    def test_send_calls_execute_with_proper_request_code(self):
        execute_request_mock = MagicMock()

        with patch.object(BaseRequestHandler, '_execute_request', execute_request_mock):
            request_handler = GetUserInfoRequestHandler()
            request_handler.send('some api key', 'some url', {'key': 'value'})
            execute_request_mock.assert_called_once_with('some api key', RequestCode.GET, 'some url', {'key': 'value'})
