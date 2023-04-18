import unittest

from eleven_labs_api.requests.exceptions.empty_history_item_id import EmptyHistoryItemId
from eleven_labs_api.requests.get_audio_from_history_item_request import GetAudioFromHistoryItemRequest


class TestGetAudioFromHistoryItemRequest(unittest.TestCase):
    def test_get_audio_from_history_item_request_constructs_properly(self):
        history_item_id = '1234'
        expected_uri = f'/v1/history/{history_item_id}/audio'
        expected_payload = {}

        request = GetAudioFromHistoryItemRequest(history_item_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_get_audio_from_history_item_request_raises_exception_when_history_item_id_is_empty(self):
        history_item_id = ''

        with self.assertRaises(EmptyHistoryItemId):
            GetAudioFromHistoryItemRequest(history_item_id)
