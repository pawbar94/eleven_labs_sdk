import json
from typing import Any
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler
from src.api_client.response_handling.utils import create_voice_settings, create_feedback
from src.common.history_item.history_item import HistoryItem


class GetHistoryItemResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_history_item(data)

    def __create_history_item(self, history_item_properties: dict) -> HistoryItem:
        return HistoryItem(id=history_item_properties['history_item_id'],
                           request_id=history_item_properties['request_id'],
                           voice_id=history_item_properties['voice_id'],
                           voice_name=history_item_properties['voice_name'],
                           text=history_item_properties['text'], date=history_item_properties['date_unix'],
                           character_count_change_from=history_item_properties['character_count_change_from'],
                           character_count_change_to=history_item_properties['character_count_change_to'],
                           content_type=history_item_properties['content_type'],
                           state=history_item_properties['state'],
                           settings=create_voice_settings(history_item_properties['settings']),
                           feedback=create_feedback(history_item_properties['feedback']))
