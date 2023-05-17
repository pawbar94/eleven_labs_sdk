from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from src.api_client.input_validation.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from src.api_client.input_validation.exceptions.invalid_stability_value import InvalidStabilityValue
from src.api_client.input_validation.exceptions.missing_similarity_boost_argument import MissingSimilarityBoostArgument
from src.api_client.input_validation.exceptions.missing_stability_argument import MissingStabilityArgument
from src.api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class EditVoiceSettingsInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument,
                               'stability': MissingStabilityArgument,
                               'similarity_boost': MissingSimilarityBoostArgument}, 'edit voice settings', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId}, 'edit voice settings', **kwargs)
        self._check_if_in_range({'stability': InvalidStabilityValue,
                                 'similarity_boost': InvalidSimilarityBoostValue},
                                {'stability': (0, 1),
                                 'similarity_boost': (0, 1)}, 'edit voice settings', **kwargs)
