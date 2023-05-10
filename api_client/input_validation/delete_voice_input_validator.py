from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class DeleteVoiceInputValidator(BaseInputValidator):
    def __init__(self):
        super().__init__()

    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument}, 'delete voice', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId}, 'delete voice', **kwargs)
