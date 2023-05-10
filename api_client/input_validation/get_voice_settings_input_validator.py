from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class GetVoiceSettingsInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument}, 'get voice settings', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId}, 'get voice settings', **kwargs)
