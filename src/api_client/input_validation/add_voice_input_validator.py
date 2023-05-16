from src.api_client.input_validation.base_input_validator import BaseInputValidator
from src.api_client.input_validation.exceptions.empty_name import EmptyName
from src.api_client.input_validation.exceptions.empty_samples import EmptySamples
from src.api_client.input_validation.exceptions.missing_description_argument import MissingDescriptionArgument
from src.api_client.input_validation.exceptions.missing_labels_argument import MissingLabelsArgument
from src.api_client.input_validation.exceptions.missing_name_argument import MissingNameArgument
from src.api_client.input_validation.exceptions.missing_samples_argument import MissingSamplesArgument


class AddVoiceInputValidator(BaseInputValidator):
    def validate(self, **kwargs) -> None:
        self._check_existence({'name': MissingNameArgument,
                               'samples': MissingSamplesArgument,
                               'description': MissingDescriptionArgument,
                               'labels': MissingLabelsArgument}, 'add voice', **kwargs)
        self._check_if_empty({'name': EmptyName,
                              'samples': EmptySamples}, 'add voice', **kwargs)
