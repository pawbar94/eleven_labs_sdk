import unittest
from unittest.mock import MagicMock
from api_client.response_handling.base_response_handler import BaseResponseHandler
from api_client.response_handling.exceptions.response_error import ResponseError


class TestBaseResponseHandler(unittest.TestCase):
    def test_process_raises_proper_error_if_status_code_not_successful(self):
        test_response = MagicMock()
        test_response.status_code = 404

        base_response_handler = BaseResponseHandler()

        with self.assertRaises(ResponseError):
            base_response_handler.process(test_response)
