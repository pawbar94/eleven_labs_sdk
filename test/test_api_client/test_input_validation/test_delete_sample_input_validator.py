import unittest
from api_client.input_validation.delete_sample_input_validator import DeleteSampleInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_sample_id_argument import MissingSampleIdArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from api_client.input_validation.exceptions.empty_sample_id import EmptySampleId


class TestDeleteSampleInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = DeleteSampleInputValidator()
        input_validator.validate(voice_id='some id', sample_id='some id')

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        input_validator = DeleteSampleInputValidator()
        with self.assertRaises(MissingVoiceIdArgument):
            input_validator.validate(sample_id='some id')

    def test_validate_raises_proper_exception_if_sample_id_not_provided(self):
        input_validator = DeleteSampleInputValidator()
        with self.assertRaises(MissingSampleIdArgument):
            input_validator.validate(voice_id='some id')

    def test_validate_raises_proper_exception_if_voice_id_is_empty(self):
        input_validator = DeleteSampleInputValidator()
        with self.assertRaises(EmptyVoiceId):
            input_validator.validate(voice_id='', sample_id='some id')

    def test_validate_raises_proper_exception_if_sample_id_is_empty(self):
        input_validator = DeleteSampleInputValidator()
        with self.assertRaises(EmptySampleId):
            input_validator.validate(voice_id='some id', sample_id='')
