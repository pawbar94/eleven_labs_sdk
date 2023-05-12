import json
from typing import Any, List
from requests import Response
from api_client.response_handling.base_response_handler import BaseResponseHandler
from common.model.language import Language
from common.model.model import Model


class GetModelsResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: list = json.loads(response.text)

        return self.__create_models(data)

    def __create_models(self, models_properties: list) -> List[Model]:
        models: List[Model] = []

        for model_properties in models_properties:
            languages: List[Language] = self.__create_languages(model_properties['languages'])
            models.append(Model(model_id=model_properties['model_id'], name=model_properties['name'],
                                can_be_finetuned=model_properties['can_be_finetuned'],
                                can_do_text_to_speech=model_properties['can_do_text_to_speech'],
                                can_do_voice_conversion=model_properties['can_do_voice_conversion'],
                                token_cost_factor=model_properties['token_cost_factor'],
                                description=model_properties['description'], languages=languages))
        return models

    def __create_languages(self, languages_properties: list) -> List[Language]:
        languages: List[Language] = []

        for language_properties in languages_properties:
            languages.append(Language(id=language_properties['language_id'], name=language_properties['name']))

        return languages
