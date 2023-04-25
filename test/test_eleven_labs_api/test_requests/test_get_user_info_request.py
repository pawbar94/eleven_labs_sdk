import unittest
from eleven_labs_api.requests.get_user_info_request import GetUserInfoRequest


class TestGetUserInfoRequest(unittest.TestCase):
    def test_get_user_info_request_constructs_properly(self):
        expected_uri: str = '/v1/user'
        expected_payload: dict = {}

        request: GetUserInfoRequest = GetUserInfoRequest()

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)
