import unittest
import json
from unittest.mock import MagicMock

from src.api_client.response_handling.get_default_voice_settings_response_handler import \
    GetDefaultVoiceSettingsResponseHandler
from src.common.voice.voice_settings import VoiceSettings


class TestGetDefaultVoiceSettingsResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
            'stability': 0.1,
            'similarity_boost': 0.2
        }
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = VoiceSettings(stability=0.1, similarity_boost=0.2)

        response_handler = GetDefaultVoiceSettingsResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
