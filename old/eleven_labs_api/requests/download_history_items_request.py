from typing import List
from old.eleven_labs_api.requests.exceptions.empty_history_items_ids import EmptyHistoryItemsIds
from old.eleven_labs_api.requests.request_interface import RequestInterface


class DownloadHistoryItemsRequest(RequestInterface):
    def __init__(self, history_items_ids: List[str]):
        if not history_items_ids:
            raise EmptyHistoryItemsIds('History items ids cannot be empty!')

        self.__history_items_ids: List[str] = history_items_ids

    def uri(self) -> str:
        return f'/v1/history/download'

    def payload(self) -> dict:
        return {
            "history_item_ids": self.__history_items_ids
        }
