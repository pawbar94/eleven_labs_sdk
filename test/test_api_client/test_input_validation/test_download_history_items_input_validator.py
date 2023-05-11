import unittest

from api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument
from api_client.input_validation.download_history_items_input_validator import DownloadHistoryItemsInputValidator
from api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId


class TestDownloadHistoryItemsInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = DownloadHistoryItemsInputValidator()
        input_validator.validate(history_items_ids='some id')

    def test_validate_raises_proper_exception_if_history_items_ids_not_provided(self):
        input_validator = DownloadHistoryItemsInputValidator()
        with self.assertRaises(MissingHistoryItemIdArgument):
            input_validator.validate()

    def test_validate_raises_proper_exception_if_history_items_ids_is_empty(self):
        input_validator = DownloadHistoryItemsInputValidator()
        with self.assertRaises(EmptyHistoryItemId):
            input_validator.validate(history_items_ids='')
