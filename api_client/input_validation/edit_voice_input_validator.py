from api_client.input_validation.base_input_validator import BaseInputValidator
from api_client.input_validation.exceptions.empty_voice_id import EmptyVoiceId
from api_client.input_validation.exceptions.missing_description_argument import MissingDescriptionArgument
from api_client.input_validation.exceptions.missing_labels_argument import MissingLabelsArgument
from api_client.input_validation.exceptions.missing_name_argument import MissingNameArgument
from api_client.input_validation.exceptions.missing_samples_argument import MissingSamplesArgument
from api_client.input_validation.exceptions.missing_voice_id_argument import MissingVoiceIdArgument


class EditVoiceInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'voice_id': MissingVoiceIdArgument,
                               'name': MissingNameArgument,
                               'samples': MissingSamplesArgument,
                               'description': MissingDescriptionArgument,
                               'labels': MissingLabelsArgument}, 'edit voice', **kwargs)
        self._check_if_empty({'voice_id': EmptyVoiceId}, 'edit voice', **kwargs)
