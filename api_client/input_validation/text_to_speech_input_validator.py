from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_text import EmptyText
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_latency_argument import MissingLatencyArgument
from api_client.input_validation.exceptions.missing_text_argument import MissingTextArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class TextToSpeechInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'text': MissingTextArgument,
                               'voice_id': MissingVoiceIdArgument,
                               'latency': MissingLatencyArgument}, 'text to speech', **kwargs)
        self._check_if_empty({'text': EmptyText,
                              'voice_id': EmptyVoiceId}, 'text to speech', **kwargs)
