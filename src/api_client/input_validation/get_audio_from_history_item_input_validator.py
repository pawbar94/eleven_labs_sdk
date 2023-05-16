from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId
from src.api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument


class GetAudioFromHistoryItemInputValidator(BaseInputValidator):
    def __init__(self):
        super().__init__()

    def validate(self, **kwargs) -> None:
        self._check_existence({'history_item_id': MissingHistoryItemIdArgument}, 'get audio from history item',
                              **kwargs)
        self._check_if_empty({'history_item_id': EmptyHistoryItemId}, 'get audio from history item',
                             **kwargs)
