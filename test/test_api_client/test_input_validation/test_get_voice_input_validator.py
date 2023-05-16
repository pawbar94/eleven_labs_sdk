import unittest
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from src.api_client.input_validation.get_voice_input_validator import GetVoiceInputValidator


class TestGetVoiceInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetVoiceInputValidator()
        input_validator.validate(voice_id='voice_id')

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        input_validator = GetVoiceInputValidator()

        with self.assertRaises(MissingVoiceIdArgument):
            input_validator.validate()

    def test_validate_raises_proper_exception_if_provided_voice_id_is_empty(self):
        input_validator = GetVoiceInputValidator()

        with self.assertRaises(EmptyVoiceId):
            input_validator.validate(voice_id='')
