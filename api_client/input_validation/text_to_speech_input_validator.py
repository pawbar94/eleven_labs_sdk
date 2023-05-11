from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_model_id import EmptyModelId
from api_client.input_validation.exceptions.empty_text import EmptyText
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from api_client.input_validation.exceptions.invalid_stability_value import InvalidStabilityValue
from api_client.input_validation.exceptions.missing_latency_argument import MissingLatencyArgument
from api_client.input_validation.exceptions.missing_model_id_argument import MissingModelIdArgument
from api_client.input_validation.exceptions.missing_similarity_boost_argument import MissingSimilarityBoostArgument
from api_client.input_validation.exceptions.missing_stability_argument import MissingStabilityArgument
from api_client.input_validation.exceptions.missing_text_argument import MissingTextArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class TextToSpeechInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument,
                               'text': MissingTextArgument,
                               'model_id': MissingModelIdArgument,
                               'stability': MissingStabilityArgument,
                               'similarity_boost': MissingSimilarityBoostArgument,
                               'latency': MissingLatencyArgument}, 'text to speech', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId,
                              'text': EmptyText,
                              'model_id': EmptyModelId}, 'text to speech', **kwargs)
        self._check_if_in_range({'stability': InvalidStabilityValue,
                                 'similarity_boost': InvalidSimilarityBoostValue},
                                {'stability': (0, 1),
                                 'similarity_boost': (0, 1)}, 'text to speech', **kwargs)
