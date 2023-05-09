import unittest
from old.eleven_labs_api.requests.get_default_voice_settings_request import GetDefaultVoiceSettingsRequest


class TestGetDefaultVoiceSettingsRequest(unittest.TestCase):
    def test_get_default_voice_settings_request_constructs_properly(self):
        expected_uri: str = '/v1/voices/settings/default'
        expected_payload: dict = {}

        request = GetDefaultVoiceSettingsRequest()

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)
