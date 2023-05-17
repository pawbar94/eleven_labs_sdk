from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.missing_sample_id_argument import MissingSampleIdArgument
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from src.api_client.input_validation.exceptions.empty_sample_id import EmptySampleId


class DeleteSampleInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument,
                               'sample_id': MissingSampleIdArgument}, 'delete sample', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId,
                              'sample_id': EmptySampleId}, 'delete sample', **kwargs)
