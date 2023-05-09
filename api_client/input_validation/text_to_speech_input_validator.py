from api_client.input_validation.exceptions.empty_text import EmptyText
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_latency_argument import MissingLatencyArgument
from api_client.input_validation.exceptions.missing_text_argument import MissingTextArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from api_client.input_validation.input_validator_interface import InputValidatorInterface


class TextToSpeechInputValidator(InputValidatorInterface):
    def validate(self, **kwargs) -> None:
        if 'text' not in kwargs:
            raise MissingTextArgument(f'Missing text argument in the arguments provided for text to speech command.')
        if 'voice_id' not in kwargs:
            raise MissingVoiceIdArgument(f'Missing voice_id argument in the arguments provided for text to speech '
                                         f'command.')
        if 'latency' not in kwargs:
            raise MissingLatencyArgument(f'Missing latency argument in the arguments provided for text to speech '
                                         f'command.')

        if not kwargs['text']:
            raise EmptyText(f'Text provided for text-to-speech conversion cannot be empty.')
        if not kwargs['voice_id']:
            raise EmptyVoiceId(f'Voice ID provided for text-to-speech conversion cannot be empty.')
