import unittest
from eleven_labs_api.requests.get_generated_items_request import GetGeneratedItemsRequest


class TestGetGeneratedItemsRequest(unittest.TestCase):
    def test_get_generated_items_request_constructs_properly(self):
        expected_uri = '/v1/history'
        expected_payload = {}

        request = GetGeneratedItemsRequest()

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)
