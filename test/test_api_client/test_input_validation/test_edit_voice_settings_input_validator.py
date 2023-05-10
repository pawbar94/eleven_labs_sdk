import unittest

from api_client.input_validation.edit_voice_settings_input_validator import EditVoiceSettingsInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from api_client.input_validation.exceptions.invalid_stability_value import InvalidStabilityValue
from api_client.input_validation.exceptions.missing_similarity_boost_argument import MissingSimilarityBoostArgument
from api_client.input_validation.exceptions.missing_stability_argument import MissingStabilityArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class TestEditVoiceSettingsInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = EditVoiceSettingsInputValidator()
        input_validator.validate(voice_id='voice_id', stability=0.5, similarity_boost=0.5)

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(MissingVoiceIdArgument):
            input_validator.validate()

    def test_validate_raises_proper_exception_if_stability_not_provided(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(MissingStabilityArgument):
            input_validator.validate(voice_id='voice_id', similarity_boost=0.5)

    def test_validate_raises_proper_exception_if_similarity_boost_not_provided(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(MissingSimilarityBoostArgument):
            input_validator.validate(voice_id='voice_id', stability=0.5)

    def test_validate_raises_proper_exception_if_provided_voice_id_is_empty(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(EmptyVoiceId):
            input_validator.validate(voice_id='', stability=0.5, similarity_boost=0.5)

    def test_validate_raises_proper_exception_if_provided_stability_has_invalid_value(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(InvalidStabilityValue):
            input_validator.validate(voice_id='voice_id', stability=-2, similarity_boost=0.5)
        with self.assertRaises(InvalidStabilityValue):
            input_validator.validate(voice_id='voice_id', stability=2, similarity_boost=0.5)

    def test_validate_raises_proper_exception_if_provided_similarity_boost_has_invalid_value(self):
        input_validator = EditVoiceSettingsInputValidator()

        with self.assertRaises(InvalidSimilarityBoostValue):
            input_validator.validate(voice_id='voice_id', stability=0.5, similarity_boost=-2)
        with self.assertRaises(InvalidSimilarityBoostValue):
            input_validator.validate(voice_id='voice_id', stability=0.5, similarity_boost=2)
