import unittest
import json
from unittest.mock import MagicMock
from src.api_client.response_handling.add_voice_response_handler import AddVoiceResponseHandler


class TestAddVoiceResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
            'voice_id': 'some voice ID'
        }
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = 'some voice ID'

        response_handler = AddVoiceResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
