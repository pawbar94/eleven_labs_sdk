import unittest

from eleven_labs_api.requests.add_voice_request import AddVoiceRequest
from eleven_labs_api.requests.delete_history_item_request import DeleteHistoryItemRequest
from eleven_labs_api.requests.delete_sample_request import DeleteSampleRequest
from eleven_labs_api.requests.delete_voice_request import DeleteVoiceRequest
from eleven_labs_api.requests.download_history_items_request import DownloadHistoryItemsRequest
from eleven_labs_api.requests.edit_voice_request import EditVoiceRequest
from eleven_labs_api.requests.edit_voice_settings_request import EditVoiceSettingsRequest
from eleven_labs_api.requests.get_audio_from_history_item_request import GetAudioFromHistoryItemRequest
from eleven_labs_api.requests.get_audio_from_sample_request import GetAudioFromSampleRequest
from eleven_labs_api.requests.get_default_voice_settings_request import GetDefaultVoiceSettingsRequest
from eleven_labs_api.requests.get_generated_items_request import GetGeneratedItemsRequest
from eleven_labs_api.requests.get_user_info_request import GetUserInfoRequest
from eleven_labs_api.requests.get_user_subscription_info_request import GetUserSubscriptionInfoRequest
from eleven_labs_api.requests.get_voice_request import GetVoiceRequest
from eleven_labs_api.requests.get_voice_settings_request import GetVoiceSettingsRequest
from eleven_labs_api.requests.get_voices_request import GetVoicesRequest
from eleven_labs_api.requests.request_factory import RequestFactory
from eleven_labs_api.requests.request_id import RequestID
from eleven_labs_api.requests.text_to_speech_audio_request import TextToSpeechAudioRequest
from eleven_labs_api.requests.text_to_speech_stream_request import TextToSpeechStreamRequest


class TestRequestFactory(unittest.TestCase):
    def test_create(self):
        self.assertEqual(RequestFactory.create(RequestID.TEXT_TO_SPEECH_AUDIO), TextToSpeechAudioRequest)
        self.assertEqual(RequestFactory.create(RequestID.TEXT_TO_SPEECH_STREAM), TextToSpeechStreamRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_VOICES), GetVoicesRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_DEFAULT_VOICE_SETTINGS), GetDefaultVoiceSettingsRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_VOICE_SETTINGS), GetVoiceSettingsRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_VOICE), GetVoiceRequest)
        self.assertEqual(RequestFactory.create(RequestID.DELETE_VOICE), DeleteVoiceRequest)
        self.assertEqual(RequestFactory.create(RequestID.EDIT_VOICE_SETTINGS), EditVoiceSettingsRequest)
        self.assertEqual(RequestFactory.create(RequestID.ADD_VOICE), AddVoiceRequest)
        self.assertEqual(RequestFactory.create(RequestID.EDIT_VOICE), EditVoiceRequest)
        self.assertEqual(RequestFactory.create(RequestID.DELETE_SAMPLE), DeleteSampleRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_AUDIO_FROM_SAMPLE), GetAudioFromSampleRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_GENERATED_ITEMS), GetGeneratedItemsRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_AUDIO_FROM_HISTORY_ITEM), GetAudioFromHistoryItemRequest)
        self.assertEqual(RequestFactory.create(RequestID.DELETE_HISTORY_ITEM), DeleteHistoryItemRequest)
        self.assertEqual(RequestFactory.create(RequestID.DOWNLOAD_HISTORY_ITEMS), DownloadHistoryItemsRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_USER_SUBSCRIPTION_INFO), GetUserSubscriptionInfoRequest)
        self.assertEqual(RequestFactory.create(RequestID.GET_USER_INFO), GetUserInfoRequest)
