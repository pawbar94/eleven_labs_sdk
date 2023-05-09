from typing import List
import requests
import json
from old.eleven_labs_api.responses.base_response import BaseResponse
from common.history_item_properties.history_item import HistoryItem
from old.eleven_labs_api.responses.history_item_model.history_item_factory import HistoryItemFactory
from logging import getLogger

logger = getLogger('GetGeneratedItemsResponse')


class GetGeneratedItemsResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> List[HistoryItem]:
        items: List[HistoryItem] = []

        for item_properties in json.loads(self._raw_response.text)['history']:
            items.append(HistoryItemFactory.create(item_properties))

        logger.debug(f'Received {len(items)} generated items')

        return items
