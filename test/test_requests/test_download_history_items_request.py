import unittest
from typing import List

from eleven_labs_api.requests.download_history_items_request import DownloadHistoryItemsRequest


class TestDownloadHistoryItemsRequest(unittest.TestCase):
    def test_download_history_items_request_constructs_properly(self):
        history_items_ids: List[str] = ['1', '2', '3']
        expected_uri: str = '/v1/history/download'
        expected_payload: dict = {
            "history_item_ids": history_items_ids
        }

        request: DownloadHistoryItemsRequest = DownloadHistoryItemsRequest(history_items_ids)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_download_history_items_request_raises_exception_when_history_items_ids_is_empty(self):
        history_items_ids: List[str] = []

        with self.assertRaises(Exception):
            DownloadHistoryItemsRequest(history_items_ids)
