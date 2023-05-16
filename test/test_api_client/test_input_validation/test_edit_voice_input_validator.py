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
        input_validator.validate(voice_id='some id', name='some name', samples=['some sample'],
                                 description='some description', labels=['some label'])

    def test_validate_raises_no_exception_if_no_new_values_provided(self):
        input_validator = EditVoiceInputValidator()
        input_validator.validate(voice_id='some id', name='', samples=[], description='',
                                 labels=[])

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingVoiceIdArgument):
            input_validator.validate(name='some name', samples=['some sample'], description='some description',
                                     labels=['some label'])

    def test_validate_raises_proper_exception_if_name_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingNameArgument):
            input_validator.validate(voice_id='some id', samples=['some sample'], description='some description',
                                     labels=['some label'])

    def test_validate_raises_proper_exception_if_samples_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingSamplesArgument):
            input_validator.validate(voice_id='some id', name='some name', description='some description',
                                     labels=['some label'])

    def test_validate_raises_proper_exception_if_description_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingDescriptionArgument):
            input_validator.validate(voice_id='some id', name='some name', samples=['some sample'],
                                     labels=['some label'])

    def test_validate_raises_proper_exception_if_labels_not_provided(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(MissingLabelsArgument):
            input_validator.validate(voice_id='some id', name='some name', samples=['some sample'],
                                     description='some description')

    def test_validate_raises_proper_exception_if_voice_id_is_empty(self):
        input_validator = EditVoiceInputValidator()
        with self.assertRaises(EmptyVoiceId):
            input_validator.validate(voice_id='', name='some name', samples=['some sample'],
                                     description='some description',
                                     labels=['some label'])
