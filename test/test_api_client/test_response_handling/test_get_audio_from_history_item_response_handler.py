import unittest
from unittest.mock import MagicMock

from src.api_client.response_handling.get_audio_from_history_item_response_handler import \
    GetAudioFromHistoryItemResponseHandler


class TestGetAudioFromHistoryItemResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        response = MagicMock()
        response.status_code = 200
        response.content = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

        response_handler = GetAudioFromHistoryItemResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(processed_response, response.content)
