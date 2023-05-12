import unittest
from unittest.mock import MagicMock
from api_client.response_handling.text_to_speech_response_handler import TextToSpeechResponseHandler


class TestTextToSpeechResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        response = MagicMock()
        response.status_code = 200
        response.content = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

        response_handler = TextToSpeechResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(processed_response, response.content)
