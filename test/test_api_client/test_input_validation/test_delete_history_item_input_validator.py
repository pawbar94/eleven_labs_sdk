import unittest

from api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument
from api_client.input_validation.delete_history_item_input_validator import DeleteHistoryItemInputValidator
from api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId


class TestDeleteHistoryItemInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = DeleteHistoryItemInputValidator()
        input_validator.validate(history_item_id='some id')

    def test_validate_raises_proper_exception_if_history_item_id_not_provided(self):
        input_validator = DeleteHistoryItemInputValidator()
        with self.assertRaises(MissingHistoryItemIdArgument):
            input_validator.validate()

    def test_validate_raises_proper_exception_if_history_item_id_is_empty(self):
        input_validator = DeleteHistoryItemInputValidator()
        with self.assertRaises(EmptyHistoryItemId):
            input_validator.validate(history_item_id='')
