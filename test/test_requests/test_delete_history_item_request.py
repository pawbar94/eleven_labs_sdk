import unittest
from eleven_labs_api.requests.delete_history_item_request import DeleteHistoryItemRequest
from eleven_labs_api.requests.exceptions.empty_history_item_id import EmptyHistoryItemId


class TestDeleteHistoryItemRequest(unittest.TestCase):
    def test_delete_history_item_request_constructs_properly(self):
        history_item_id = 'some_id'
        expected_uri = f'/v1/history/{history_item_id}'
        expected_payload = {}

        request = DeleteHistoryItemRequest(history_item_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_delete_history_item_request_raises_exception_when_history_item_id_is_empty(self):
        history_item_id = ''

        with self.assertRaises(EmptyHistoryItemId):
            DeleteHistoryItemRequest(history_item_id)
