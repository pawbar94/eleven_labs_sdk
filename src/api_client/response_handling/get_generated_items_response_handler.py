import json
from typing import Any, List
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler
from src.api_client.response_handling.utils import create_voice_settings, create_feedback
from src.common.history_item.history_item import HistoryItem


class GetGeneratedItemsResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_history_items(data['history'])

    def __create_history_items(self, history_items_properties: list) -> List[HistoryItem]:
        items: List[HistoryItem] = []

        if not history_items_properties:
            return []

        for item_properties in history_items_properties:
            items.append(HistoryItem(id=item_properties['history_item_id'], request_id=item_properties['request_id'],
                                     voice_id=item_properties['voice_id'], voice_name=item_properties['voice_name'],
                                     text=item_properties['text'], date=item_properties['date_unix'],
                                     character_count_change_from=item_properties['character_count_change_from'],
                                     character_count_change_to=item_properties['character_count_change_to'],
                                     content_type=item_properties['content_type'],
                                     state=item_properties['state'],
                                     settings=create_voice_settings(item_properties['settings']),
                                     feedback=create_feedback(item_properties['feedback'])))

        return items
