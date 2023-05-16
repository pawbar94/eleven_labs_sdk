from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId
from src.api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument


class DownloadHistoryItemsInputValidator(BaseInputValidator):
    def __init__(self):
        super().__init__()

    def validate(self, **kwargs) -> None:
        self._check_existence({'history_items_ids': MissingHistoryItemIdArgument}, 'download history items',
                              **kwargs)
        self._check_if_empty({'history_items_ids': EmptyHistoryItemId}, 'download history items',
                             **kwargs)
