import unittest
from unittest.mock import MagicMock
from api_client.response_handling.edit_voice_settings_response_handler import EditVoiceSettingsResponseHandler


class TestEditVoiceSettingsResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        response = MagicMock()
        response.status_code = 200
        response.text = 'some textual response'

        response_handler = EditVoiceSettingsResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(processed_response, response.text)
