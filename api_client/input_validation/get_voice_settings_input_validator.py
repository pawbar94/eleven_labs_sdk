from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from api_client.input_validation.input_validator_interface import InputValidatorInterface


class GetVoiceSettingsInputValidator(InputValidatorInterface):
    def validate(self, **kwargs) -> None:
        if 'voice_id' not in kwargs:
            raise MissingVoiceIdArgument(f'Missing voice_id argument in the arguments provided for text to speech '
                                         f'command.')
        if not kwargs['voice_id']:
            raise EmptyVoiceId(f'Voice ID provided for text-to-speech conversion cannot be empty.')
