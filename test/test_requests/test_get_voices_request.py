import unittest
from eleven_labs_api.requests.get_voices_request import GetVoicesRequest


class TestGetVoicesRequest(unittest.TestCase):
    def test_get_voices_request_constructs_properly(self):
        expected_uri: str = '/v1/voices'
        expected_payload: dict = {}

        request = GetVoicesRequest()

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)
