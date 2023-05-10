import unittest
from api_client.input_validation.add_voice_input_validator import AddVoiceInputValidator
from api_client.input_validation.exceptions.empty_name import EmptyName
from api_client.input_validation.exceptions.empty_samples import EmptySamples
from api_client.input_validation.exceptions.missing_description_argument import MissingDescriptionArgument
from api_client.input_validation.exceptions.missing_labels_argument import MissingLabelsArgument
from api_client.input_validation.exceptions.missing_name_argument import MissingNameArgument
from api_client.input_validation.exceptions.missing_samples_argument import MissingSamplesArgument


class TestAddVoiceInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = AddVoiceInputValidator()
        input_validator.validate(name='some name', samples=['some sample'], description='some description',
                                 labels=['some label'])

    def test_validate_raises_no_exception_when_description_and_labels_not_provided(self):
        input_validator = AddVoiceInputValidator()
        input_validator.validate(name='some name', samples=['some sample'], description='', labels=[])

    def test_validate_raises_proper_exception_if_name_not_provided(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(MissingNameArgument):
            input_validator.validate(samples=['some sample'], description='some description', labels=['some label'])

    def test_validate_raises_proper_exception_if_samples_not_provided(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(MissingSamplesArgument):
            input_validator.validate(name='some name', description='some description', labels=['some label'])

    def test_validate_raises_proper_exception_if_description_not_provided(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(MissingDescriptionArgument):
            input_validator.validate(name='some name', samples=['some sample'], labels=['some label'])

    def test_validate_raises_proper_exception_if_labels_not_provided(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(MissingLabelsArgument):
            input_validator.validate(name='some name', samples=['some sample'], description='some description')

    def test_validate_raises_proper_exception_if_name_is_empty(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(EmptyName):
            input_validator.validate(name='', samples=['some sample'], description='some description',
                                     labels=['some label'])

    def test_validate_raises_proper_exception_if_samples_is_empty(self):
        input_validator = AddVoiceInputValidator()
        with self.assertRaises(EmptySamples):
            input_validator.validate(name='some name', samples=[], description='some description',
                                     labels=['some label'])
