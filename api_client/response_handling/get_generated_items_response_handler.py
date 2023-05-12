import json
from typing import Any, List
from requests import Response
from api_client.response_handling.base_response_handler import BaseResponseHandler
from api_client.response_handling.utils import create_voice_settings
from common.history_item.feedback import Feedback
from common.history_item.history_item import HistoryItem


class GetGeneratedItemsResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_history_item(data['history'])

    def __create_history_item(self, history_items_properties: list) -> List[HistoryItem]:
        items: List[HistoryItem] = []

        for item_properties in history_items_properties:
            items.append(HistoryItem(id=item_properties['history_item_id'], request_id=item_properties['request_id'],
                                     voice_id=item_properties['voice_id'], voice_name=item_properties['voice_name'],
                                     text=item_properties['text'], date=item_properties['date_unix'],
                                     character_count_change_from=item_properties['character_count_change_from'],
                                     character_count_change_to=item_properties['character_count_change_to'],
                                     content_type=item_properties['content_type'],
                                     state=item_properties['state'],
                                     settings=create_voice_settings(item_properties['settings']),
                                     feedback=self.__create_feedback(item_properties['feedback'])))

        return items

    def __create_feedback(self, feedback_properties: dict) -> Feedback:
        return Feedback(thumbs_up=feedback_properties['thumbs_up'], feedback=feedback_properties['feedback'],
                        emotions=feedback_properties['emotions'],
                        inaccurate_clone=feedback_properties['inaccurate_clone'],
                        glitches=feedback_properties['glitches'], audio_quality=feedback_properties['audio_quality'],
                        other=feedback_properties['other'], review_status=feedback_properties['review_status'])
