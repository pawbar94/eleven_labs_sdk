import unittest

from api_client.input_validation.exceptions.empty_text import EmptyText
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_latency_argument import MissingLatencyArgument
from api_client.input_validation.exceptions.missing_text_argument import MissingTextArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from api_client.input_validation.text_to_speech_input_validator import TextToSpeechInputValidator


class TestTextToSpeechInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception_for_proper_params(self):
        validator = TextToSpeechInputValidator()
        validator.validate(voice_id="test ID", text="test text", model_id='some-model-id', stability=0.25,
                           similarity_boost=0.75, latency=0)

    def test_validate_raise_proper_exception_if_text_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingTextArgument):
            validator.validate(voice_id="test ID", latency=0)

    def test_validate_raises_proper_exception_if_voice_id_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingVoiceIdArgument):
            validator.validate(text="test text", latency=0)

    def test_validate_raises_proper_exception_if_latency_not_provided(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(MissingLatencyArgument):
            validator.validate(text="test text", voice_id="test ID")

    def test_validate_raises_proper_exception_if_provided_text_is_empty(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(EmptyText):
            validator.validate(text="", voice_id="test ID", latency=0)

    def test_validate_raises_proper_exception_if_provided_voice_id_is_empty(self):
        validator = TextToSpeechInputValidator()

        with self.assertRaises(EmptyVoiceId):
            validator.validate(text="test text", voice_id="", latency=0)
