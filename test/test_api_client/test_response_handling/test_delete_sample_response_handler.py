import unittest
from unittest.mock import MagicMock
from src.api_client.response_handling.delete_sample_response_handler import DeleteSampleResponseHandler


class TestDeleteSampleResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        response = MagicMock()
        response.status_code = 200
        response.text = 'some textual response'

        response_handler = DeleteSampleResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(processed_response, response.text)
