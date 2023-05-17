from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument
from src.api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId


class DeleteHistoryItemInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'history_item_id': MissingHistoryItemIdArgument}, 'delete history item', **kwargs)
        self._check_if_empty({'history_item_id': EmptyHistoryItemId}, 'delete history item', **kwargs)
