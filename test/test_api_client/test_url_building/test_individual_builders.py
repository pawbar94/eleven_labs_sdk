import unittest

from src.api_client.url_building.add_voice_url_builder import AddVoiceUrlBuilder
from src.api_client.url_building.delete_history_item_url_builder import DeleteHistoryItemUrlBuilder
from src.api_client.url_building.delete_sample_url_builder import DeleteSampleUrlBuilder
from src.api_client.url_building.delete_voice_url_builder import DeleteVoiceUrlBuilder
from src.api_client.url_building.download_history_items_url_builder import DownloadHistoryItemsUrlBuilder
from src.api_client.url_building.edit_voice_settings_url_builder import EditVoiceSettingsUrlBuilder
from src.api_client.url_building.edit_voice_url_builder import EditVoiceUrlBuilder
from src.api_client.url_building.get_audio_from_history_item_url_builder import GetAudioFromHistoryItemUrlBuilder
from src.api_client.url_building.get_audio_from_sample_url_builder import GetAudioFromSampleUrlBuilder
from src.api_client.url_building.get_default_voice_settings_url_builder import GetDefaultVoiceSettingsUrlBuilder
from src.api_client.url_building.get_generated_items_url_builder import GetGeneratedItemsUrlBuilder
from src.api_client.url_building.get_history_item_url_builder import GetHistoryItemUrlBuilder
from src.api_client.url_building.get_user_info_url_builder import GetUserInfoUrlBuilder
from src.api_client.url_building.get_user_subscription_info_url_builder import GetUserSubscriptionInfoUrlBuilder
from src.api_client.url_building.get_voice_settings_url_builder import GetVoiceSettingsUrlBuilder
from src.api_client.url_building.get_voice_url_builder import GetVoiceUrlBuilder
from src.api_client.url_building.get_voices_url_builder import GetVoicesUrlBuilder
from src.api_client.url_building.text_to_speech_url_builder import TextToSpeechUrlBuilder
from src.api_client.url_building.get_models_url_builder import GetModelsUrlBuilder


class TestTextToSpeechUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/text-to-speech/some-voice-id/stream'
        url_builder = TextToSpeechUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TestGetModelsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/models'
        url_builder = GetModelsUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TestGetVoicesUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices'
        url_builder = GetVoicesUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TestGetDefaultVoiceSettingsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/settings/default'
        url_builder = GetDefaultVoiceSettingsUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TestGetVoiceSettingsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id/settings'
        url_builder = GetVoiceSettingsUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TestGetVoiceUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id'
        url_builder = GetVoiceUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TestDeleteVoiceUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id'
        url_builder = DeleteVoiceUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TestEditVoiceSettingsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id/settings/edit'
        url_builder = EditVoiceSettingsUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TesAddVoiceUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/add'
        url_builder = AddVoiceUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TesEditVoiceUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id/edit'
        url_builder = EditVoiceUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id')

        self.assertEqual(url, expected_url)


class TesDeleteSampleUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id/samples/some-sample-id'
        url_builder = DeleteSampleUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id', sample_id='some-sample-id')

        self.assertEqual(url, expected_url)


class TesGetAudioFromSampleUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/voices/some-voice-id/samples/some-sample-id/audio'
        url_builder = GetAudioFromSampleUrlBuilder()

        url = url_builder.build(voice_id='some-voice-id', sample_id='some-sample-id')

        self.assertEqual(url, expected_url)


class TesGetGeneratedItemsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/history'
        url_builder = GetGeneratedItemsUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TesGetHistoryItemUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/history/some-id'
        url_builder = GetHistoryItemUrlBuilder()

        url = url_builder.build(history_item_id='some-id')

        self.assertEqual(url, expected_url)


class TesDeleteHistoryItemUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/history/some-id'
        url_builder = DeleteHistoryItemUrlBuilder()

        url = url_builder.build(history_item_id='some-id')

        self.assertEqual(url, expected_url)


class TesGetAudioFromHistoryItemUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/history/some-id/audio'
        url_builder = GetAudioFromHistoryItemUrlBuilder()

        url = url_builder.build(history_item_id='some-id')

        self.assertEqual(url, expected_url)


class TestDownloadHistoryItemsUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/history/download'
        url_builder = DownloadHistoryItemsUrlBuilder()

        url = url_builder.build(history_items_ids=['some-id-1', 'some-id-2'])

        self.assertEqual(url, expected_url)


class TestGetUserSubscriptionInfoUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/user/subscription'
        url_builder = GetUserSubscriptionInfoUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)


class TestGetUserInfoUrlBuilder(unittest.TestCase):
    def test_build_returns_proper_url(self):
        expected_url = 'https://api.elevenlabs.io/v1/user'
        url_builder = GetUserInfoUrlBuilder()

        url = url_builder.build()

        self.assertEqual(url, expected_url)
