import unittest
from old.eleven_labs_api.requests.get_user_subscription_info_request import GetUserSubscriptionInfoRequest


class TestGetUserSubscriptionInfoRequest(unittest.TestCase):
    def test_get_user_subscription_info_request_constructs_properly(self):
        expected_uri: str = '/v1/user/subscription'
        expected_payload: dict = {}

        request = GetUserSubscriptionInfoRequest()

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)
