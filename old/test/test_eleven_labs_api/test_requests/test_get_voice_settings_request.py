import unittest

from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.get_voice_settings_request import GetVoiceSettingsRequest


class TestGetVoiceSettingsRequest(unittest.TestCase):
    def test_get_voice_settings_request_constructs_properly(self):
        voice_id = '123'
        expected_uri = f'/v1/voices/{voice_id}/settings'
        expected_payload = {}

        request = GetVoiceSettingsRequest(voice_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_get_voice_settings_request_raises_exception_when_voice_id_is_empty(self):
        voice_id = ''

        with self.assertRaises(EmptyVoiceId):
            GetVoiceSettingsRequest(voice_id)
