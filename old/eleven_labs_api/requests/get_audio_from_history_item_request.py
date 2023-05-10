from api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId
from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetAudioFromHistoryItemRequest(RequestInterface):
    def __init__(self, history_item_id: str):
        if not history_item_id:
            raise EmptyHistoryItemId('History item id cannot be empty!')

        self.__history_item_id: str = history_item_id

    def uri(self) -> str:
        return f'/v1/history/{self.__history_item_id}/audio'

    def payload(self) -> dict:
        return {}
