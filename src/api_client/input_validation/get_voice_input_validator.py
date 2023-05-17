from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class GetVoiceInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument}, 'get voice', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId}, 'get voice', **kwargs)
