import unittest
from src.api_client.input_validation.edit_voice_input_validator import EditVoiceInputValidator
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.missing_description_argument import MissingDescriptionArgument
from src.api_client.input_validation.exceptions.missing_labels_argument import MissingLabelsArgument
from src.api_client.input_validation.exceptions.missing_name_argument import MissingNameArgument
from src.api_client.input_validation.exceptions.missing_samples_argument import MissingSamplesArgument
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class TestEditVoiceInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = EditVoiceInputValidator()
        input_validator.validate(voice_id='some id', new_name='some name', new_samples=['some sample'],
                                 new_description='some description', new_labels=['some label'])

    def test_validate_raises_no_exception_if_no_new_values_provided(self):
        input_validator = EditVoiceInputValidator()
        input_validator.validate(voice_id='some id', new_name='', new_samples=[], new_description='',
                                 new_labels=[])

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingVoiceIdArgument):
            input_validator.validate(name='some name', new_samples=['some sample'], new_description='some description',
                                     new_labels=['some label'])

    def test_validate_raises_proper_exception_if_name_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingNameArgument):
            input_validator.validate(voice_id='some id', new_samples=['some sample'], new_description='some description',
                                     new_labels=['some label'])

    def test_validate_raises_proper_exception_if_samples_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingSamplesArgument):
            input_validator.validate(voice_id='some id', new_name='some name', new_description='some description',
                                     new_labels=['some label'])

    def test_validate_raises_proper_exception_if_description_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingDescriptionArgument):
            input_validator.validate(voice_id='some id', new_name='some name', new_samples=['some sample'],
                                     new_labels=['some label'])

    def test_validate_raises_proper_exception_if_labels_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingLabelsArgument):
            input_validator.validate(voice_id='some id', new_name='some name', new_samples=['some sample'],
                                     new_description='some description')

    def test_validate_raises_proper_exception_if_voice_id_is_empty(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(EmptyVoiceId):
            input_validator.validate(voice_id='', new_name='some name', new_samples=['some sample'],
                                     new_description='some description',
                                     new_labels=['some label'])
