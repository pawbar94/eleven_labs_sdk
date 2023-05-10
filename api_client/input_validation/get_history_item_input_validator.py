from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument
from api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId


class GetHistoryItemInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'history_item_id': MissingHistoryItemIdArgument}, 'get history item', **kwargs)
        self._check_if_empty({'history_item_id': EmptyHistoryItemId}, 'get history item', **kwargs)
