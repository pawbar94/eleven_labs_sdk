from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_sample_id_argument import MissingSampleIdArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument
from api_client.input_validation.exceptions.empty_sample_id import EmptySampleId


class GetAudioFromSampleInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument,
                               'sample_id': MissingSampleIdArgument}, 'get audio from sample', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId,
                              'sample_id': EmptySampleId}, 'get audio from sample', **kwargs)
