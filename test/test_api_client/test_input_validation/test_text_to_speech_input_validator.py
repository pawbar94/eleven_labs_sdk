import unittest

from src.api_client.input_validation.exceptions.empty_model_id import EmptyModelId
from src.api_client.input_validation.exceptions.empty_text import EmptyText
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from src.api_client.input_validation.exceptions.invalid_stability_value import InvalidStabilityValue
from src.api_client.input_validation.exceptions.missing_latency_argument import MissingLatencyArgument
from src.api_client.input_validation.exceptions.missing_model_id_argument import MissingModelIdArgument
from src.api_client.input_validation.exceptions.missing_similarity_boost_argument import MissingSimilarityBoostArgument
from src.api_client.input_validation.exceptions.missing_stability_argument import MissingStabilityArgument
from src.api_client.input_validation.exceptions.missing_text_argument import MissingTextArgument
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from src.api_client.input_validation.text_to_speech_input_validator import TextToSpeechInputValidator


class TestTextToSpeechInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception_for_proper_params(self):
        validator = TextToSpeechInputValidator()
        validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=0.25,
                           similarity_boost=0.75, latency=0)

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingVoiceIdArgument):
            validator.validate(text='test text', model_id='some-model-id', stability=0.25, similarity_boost=0.75,
                               latency=0)

    def test_validate_raise_proper_exception_if_text_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingTextArgument):
            validator.validate(voice_id='test ID', model_id='some-model-id', stability=0.25, similarity_boost=0.75,
                               latency=0)

    def test_validate_raise_proper_exception_if_model_id_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingModelIdArgument):
            validator.validate(voice_id='test ID', text='test text', stability=0.25, similarity_boost=0.75, latency=0)

    def test_validate_raise_proper_exception_if_stability_id_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingStabilityArgument):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', similarity_boost=0.75,
                               latency=0)

    def test_validate_raise_proper_exception_if_similarity_boost_id_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingSimilarityBoostArgument):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=0.25,
                               latency=0)

    def test_validate_raises_proper_exception_if_latency_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingLatencyArgument):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=0.25,
                               similarity_boost=0.75)

    def test_validate_raises_proper_exception_if_provided_voice_id_is_empty(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(EmptyVoiceId):
            validator.validate(voice_id='', text='test text', model_id='some-model-id', stability=0.25,
                               similarity_boost=0.75, latency=0)

    def test_validate_raises_proper_exception_if_provided_text_is_empty(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(EmptyText):
            validator.validate(voice_id='test ID', text='', model_id='some-model-id', stability=0.25,
                               similarity_boost=0.75, latency=0)

    def test_validate_raises_proper_exception_if_provided_model_id_is_empty(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(EmptyModelId):
            validator.validate(voice_id='test ID', text='test text', model_id='', stability=0.25,
                               similarity_boost=0.75, latency=0)

    def test_validate_raises_proper_exception_if_provided_stability_is_out_of_range(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(InvalidStabilityValue):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=-20,
                               similarity_boost=0.75, latency=0)
        with self.assertRaises(InvalidStabilityValue):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=20,
                               similarity_boost=0.75, latency=0)

    def test_validate_raises_proper_exception_if_provided_similarity_boost_is_out_of_range(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(InvalidSimilarityBoostValue):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=0.25,
                               similarity_boost=-20, latency=0)
        with self.assertRaises(InvalidSimilarityBoostValue):
            validator.validate(voice_id='test ID', text='test text', model_id='some-model-id', stability=0.25,
                               similarity_boost=20, latency=0)
