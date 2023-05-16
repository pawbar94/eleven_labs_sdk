import unittest

from src.api_client.params_building.add_voice_params_builder import AddVoiceParamsBuilder
from src.api_client.params_building.delete_history_item_params_builder import DeleteHistoryItemParamsBuilder
from src.api_client.params_building.delete_sample_params_builder import DeleteSampleParamsBuilder
from src.api_client.params_building.delete_voice_params_builder import DeleteVoiceParamsBuilder
from src.api_client.params_building.download_history_items_params_builder import DownloadHistoryItemsParamsBuilder
from src.api_client.params_building.edit_voice_params_builder import EditVoiceParamsBuilder
from src.api_client.params_building.edit_voice_settings_params_builder import EditVoiceSettingsParamsBuilder
from src.api_client.params_building.get_audio_from_history_item_params_builder import \
    GetAudioFromHistoryItemParamsBuilder
from src.api_client.params_building.get_audio_from_sample_params_builder import GetAudioFromSampleParamsBuilder
from src.api_client.params_building.get_default_voice_settings_params_builder import \
    GetDefaultVoiceSettingsParamsBuilder
from src.api_client.params_building.get_generated_items_params_builder import GetGeneratedItemsParamsBuilder
from src.api_client.params_building.get_history_item_params_builder import GetHistoryItemParamsBuilder
from src.api_client.params_building.get_models_params_builder import GetModelsParamsBuilder
from src.api_client.params_building.get_user_info_params_builder import GetUserInfoParamsBuilder
from src.api_client.params_building.get_user_subscription_info_params_builder import \
    GetUserSubscriptionInfoParamsBuilder
from src.api_client.params_building.get_voice_params_builder import GetVoiceParamsBuilder
from src.api_client.params_building.get_voice_settings_params_builder import GetVoiceSettingsParamsBuilder
from src.api_client.params_building.get_voices_params_builder import GetVoicesParamsBuilder
from src.api_client.params_building.text_to_speech_params_builder import TextToSpeechParamsBuilder


class TestTextToSpeechParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'text': 'some text',
            'model_id': 'some model id',
            'voice_settings': {
                'stability': 0.25,
                'similarity_boost': 0.75
            }
        }
        params_builder = TextToSpeechParamsBuilder()

        params = params_builder.build(text='some text', model_id='some model id', stability=0.25, similarity_boost=0.75)

        self.assertEqual(expected_params, params)


class TestGetModelsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetModelsParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetVoicesParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetVoicesParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetDefaultVoiceSettingsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetDefaultVoiceSettingsParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetVoiceSettingsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetVoiceSettingsParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetVoiceParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetVoiceParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestDeleteVoiceParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = DeleteVoiceParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestEditVoiceSettingsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'stability': 0.25,
            'similarity_boost': 0.75
        }
        params_builder = EditVoiceSettingsParamsBuilder()

        params = params_builder.build(stability=0.25, similarity_boost=0.75)

        self.assertEqual(expected_params, params)


class TestAddVoiceParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'name': 'some name',
            'files': [b'\x00\01\x02', b'\x03\x04\x05'],
            'description': 'some description',
            'labels': '{"key1": "value1", "key2": "value2"}'
        }
        params_builder = AddVoiceParamsBuilder()

        params = params_builder.build(name='some name', files=[b'\x00\01\x02', b'\x03\x04\x05'],
                                      description='some description', labels='{"key1": "value1", "key2": "value2"}')

        self.assertEqual(expected_params, params)


class TestEditVoiceParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'name': 'some name',
            'files': [b'\x00\01\x02', b'\x03\x04\x05'],
            'description': 'some description',
            'labels': '{"key1": "value1", "key2": "value2"}'
        }
        params_builder = EditVoiceParamsBuilder()

        params = params_builder.build(new_name='some name', new_samples=[b'\x00\01\x02', b'\x03\x04\x05'],
                                      new_description='some description',
                                      new_labels='{"key1": "value1", "key2": "value2"}')

        self.assertEqual(expected_params, params)


class TestDeleteSampleParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = DeleteSampleParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetAudioFromSampleParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetAudioFromSampleParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetGeneratedItemsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetGeneratedItemsParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetHistoryItemParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetHistoryItemParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestDeleteHistoryItemParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = DeleteHistoryItemParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetAudioFromHistoryItemParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetAudioFromHistoryItemParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestDownloadHistoryItemsParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'history_items_ids': ['some id', 'some other id']
        }
        params_builder = DownloadHistoryItemsParamsBuilder()

        params = params_builder.build(history_items_ids=['some id', 'some other id'])

        self.assertEqual(expected_params, params)


class TestGetUserSubscriptionInfoParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetUserSubscriptionInfoParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)


class TestGetUserInfoParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {}
        params_builder = GetUserInfoParamsBuilder()

        params = params_builder.build()

        self.assertEqual(expected_params, params)
