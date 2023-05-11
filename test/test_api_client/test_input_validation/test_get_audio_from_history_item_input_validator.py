import unittest

from api_client.input_validation.exceptions.missing_history_item_id_argument import MissingHistoryItemIdArgument
from api_client.input_validation.get_audio_from_history_item_input_validator import GetAudioFromHistoryItemInputValidator
from api_client.input_validation.exceptions.empty_history_item_id import EmptyHistoryItemId


class TestGetAudioFromHistoryItemInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetAudioFromHistoryItemInputValidator()
        input_validator.validate(history_item_id='some id')

    def test_validate_raises_proper_exception_if_history_item_id_not_provided(self):
        input_validator = GetAudioFromHistoryItemInputValidator()
        with self.assertRaises(MissingHistoryItemIdArgument):
            input_validator.validate()

    def test_validate_raises_proper_exception_if_history_item_id_is_empty(self):
        input_validator = GetAudioFromHistoryItemInputValidator()
        with self.assertRaises(EmptyHistoryItemId):
            input_validator.validate(history_item_id='')
