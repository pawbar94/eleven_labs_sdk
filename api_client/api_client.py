import json
from typing import List, Dict, Any
from requests import Response
from api_client.command_id import CommandId
from api_client.input_validation.input_validator import InputValidator
from api_client.params_building.params_builder import ParamsBuilder
from api_client.request_handling.request_handler import RequestHandler
from api_client.url_building.url_builder import UrlBuilder
from common.history_item.history_item import HistoryItem
from api_client.latency_optimization import LatencyOptimization
from api_client.response_handling.response_handler import ResponseHandler
from common.user_info.user_info import UserInfo
from common.user_info.user_subscription_info import UserSubscriptionInfo
from common.model.model import Model
from logging import getLogger
from common.voice.voice import Voice, VoiceID
from common.voice.voice_settings import VoiceSettings
from common.directories import API_SPEC_FILE_PATH

logger = getLogger('ElevenLabsApi')


class ApiClient:
    def __init__(self, input_validator: InputValidator, url_builder: UrlBuilder, params_builder: ParamsBuilder,
                 request_handler: RequestHandler, response_handler: ResponseHandler):
        self.__input_validator: InputValidator = input_validator
        self.__url_builder: UrlBuilder = url_builder
        self.__params_builder: ParamsBuilder = params_builder
        self.__request_handler: RequestHandler = request_handler
        self.__response_handler: ResponseHandler = response_handler

    def text_to_speech(self, voice_id: str, text: str, model_id: str, stability: float, similarity_boost: float,
                       latency: LatencyOptimization = LatencyOptimization.NONE) -> bytes:
        """
        Converts a given text to speech.

        :param voice_id: ID of the voice to use for the conversion.
        :param text: The text to convert.
        :param model_id: ID of the model to use for the conversion.
        :param stability: The stability parameter value.
        :param similarity_boost: The similarity boost parameter value.
        :param latency: An optional parameter to optimize the streaming latency of the conversion.
        :return: The binary data of the resulting audio file.
        """
        logger.info(f'Converting text to speech using voice with ID {voice_id}')
        logger.debug(f'Model ID: {model_id}')
        logger.debug(f'Stability: {stability}')
        logger.debug(f'Similarity boost: {similarity_boost}')
        logger.debug(f'Streaming latency optimization: {latency}')
        logger.debug(f'Text to convert: {text}')

        return self.__handle_request(CommandId.TEXT_TO_SPEECH, voice_id=voice_id, text=text, model_id=model_id,
                                     stability=stability, similarity_boost=similarity_boost, latency=latency)

    def get_models(self) -> List[Model]:
        """
        Retrieves the available models for speech synthesis.

        :return: A list of available models properties.
        """
        logger.info(f'Getting available models')

        return self.__handle_request(CommandId.GET_MODELS)

    def get_voices(self) -> List[Voice]:
        """
        Retrieves the available voices for speech conversion.

        :return: A list of available voices.
        """
        logger.info(f'Getting available voices')

        return self.__handle_request(CommandId.GET_VOICES)

    def get_voice_settings(self, voice_id: str = '') -> VoiceSettings:
        """
        Retrieves settings for the given voice.

        :param voice_id: An optional parameter to specify the voice id to retrieve the settings for. If not
                         provided, the default voice settings will be returned.
        :return: Settings for the specified voice.
        """
        logger.info(f'Getting {"" if voice_id else "default"} settings'
                    f'{" for voice with ID " + voice_id if voice_id else ""}')

        command_id: CommandId = CommandId.GET_VOICE_SETTINGS if voice_id else CommandId.GET_DEFAULT_VOICE_SETTINGS
        return self.__handle_request(command_id, voice_id=voice_id)

    def get_voice(self, voice_id: str) -> Voice:
        """
        Retrieves voice properties by its ID.

        :param voice_id: The ID of the voice to retrieve.
        :return: The requested voice properties.
        """
        logger.info(f'Getting voice with ID {voice_id}')

        return self.__handle_request(CommandId.GET_VOICE, voice_id=voice_id)

    def delete_voice(self, voice_id: str) -> str:
        """
        Deletes a voice from the account.

        :param voice_id: ID of the voice to delete.
        :return: A message indicating whether the deletion was successful.
        """
        logger.info(f'Deleting voice with ID {voice_id}')

        return self.__handle_request(CommandId.DELETE_VOICE, voice_id=voice_id)

    def edit_voice_settings(self, voice_id: str, settings: VoiceSettings) -> str:
        """
        Edits settings for the given voice.

        :param voice_id: ID of the voice to modify.
        :param settings: The new settings for the voice.
        :return: A message indicating whether the update was successful.
        """
        logger.info(f'Changing settings for voice with ID {voice_id} to {settings}')

        return self.__handle_request(CommandId.EDIT_VOICE_SETTINGS, voice_id=voice_id,
                                     stability=settings.stability, similarity_boost=settings.similarity_boost)

    def add_voice(self, name: str, samples: List[bytes], description: str, labels: Dict[str, str]) -> VoiceID:
        """
        Adds a new voice to the account.

        :param name: Name of the new voice.
        :param samples: A list of binary data containing speech samples for the new voice.
        :param description: A description of the new voice.
        :param labels: Labels to associate with the new voice.
        :return: The ID of the newly created voice.
        """
        logger.info(f'Adding new voice with name {name}')
        logger.debug(f'Num of samples: {len(samples)}, description: {description}, labels: {labels}')

        return self.__handle_request(CommandId.ADD_VOICE, name=name, samples=samples,
                                     description=description, labels=labels)

    def edit_voice(self, voice_id: str, new_name: str, new_samples: List[bytes], new_description: str,
                   new_labels: Dict[str, str]) -> VoiceID:
        """
        Edits an existing voice by updating its name, audio files, description, and labels.

        :param voice_id: ID of the voice to be edited.
        :param new_name: New name of the voice.
        :param new_samples: A list of binary data containing speech samples for the new voice.
        :param new_description: A string containing the new description for the voice.
        :param new_labels: Labels to associate with the new voice.
        :return: A `VoiceID` object representing the ID of the edited voice.
        """
        logger.info(f'Editing voice with ID {voice_id}')
        logger.debug(f'New name: {new_name}, num of samples: {len(new_samples)}, new description: {new_description}, '
                     f'new labels: {new_labels}')

        return self.__handle_request(CommandId.EDIT_VOICE, voice_id=voice_id, name=new_name,
                                     samples=new_samples, description=new_description, labels=new_labels)

    def delete_sample(self, voice_id: str, sample_id: str) -> str:
        """
        Deletes a sample from a voice.

        :param voice_id: ID of the voice the sample belongs to.
        :param sample_id: A string containing the ID of the sample to be deleted.
        :return: A string indicating the status of the operation.
        """
        logger.info(f'Deleting sample with ID {sample_id} from voice with ID {voice_id}')

        return self.__handle_request(CommandId.DELETE_SAMPLE, voice_id=voice_id,
                                     sample_id=sample_id)

    def get_audio_from_sample(self, voice_id: str, sample_id: str) -> bytes:
        """
        Gets the audio data for a sample.

        :param voice_id: ID of the voice the sample belongs to.
        :param sample_id: A string containing the ID of the sample to get the audio data for.
        :return: A bytes object containing the audio data of the sample.
        """
        logger.info(f'Getting audio data for sample with ID {sample_id} from voice with ID {voice_id}')

        return self.__handle_request(CommandId.GET_AUDIO_FROM_SAMPLE, voice_id=voice_id,
                                     sample_id=sample_id)

    def get_generated_items(self) -> List[HistoryItem]:
        """
        Gets a list of generated items.

        :return: A list of `HistoryItem` objects representing the generated items.
        """
        logger.info('Getting generated items')

        return self.__handle_request(CommandId.GET_GENERATED_ITEMS)

    def get_history_item(self, history_item_id: str) -> HistoryItem:
        """
        Gets a history item by ID.

        :param history_item_id: A string containing the ID of the history item to get.
        :return: A `HistoryItem` object representing the history item.
        """
        logger.info(f'Getting history item with ID {history_item_id}')

        return self.__handle_request(CommandId.GET_HISTORY_ITEM_BY_ID, history_item_id=history_item_id)

    def delete_history_item(self, history_item_id: str) -> str:
        """
        Deletes a history item.

        :param history_item_id: ID of the history item to delete.
        :return: A string indicating the status of the operation.
        """
        logger.info(f'Deleting history item with ID {history_item_id}')

        return self.__handle_request(CommandId.DELETE_HISTORY_ITEM, history_item_id=history_item_id)

    def get_audio_from_history_item(self, history_item_id: str) -> bytes:
        """
        Gets the audio data from a history item.

        :param history_item_id: ID of the history item to get the audio data for.
        :return: A bytes object containing the audio data for the history item.
        """
        logger.info(f'Getting audio data from history item with ID {history_item_id}')

        return self.__handle_request(CommandId.GET_AUDIO_FROM_HISTORY_ITEM, history_item_id=history_item_id)

    def download_history_items(self, history_items_ids: List[str]) -> List[bytes]:
        """
        Downloads the audio data for multiple history items.

        :param history_items_ids: A list of strings containing the IDs of the history items to download.
        :return: A list of bytes objects representing the audio data for the history items.
        """
        logger.info(f'Downloading audio data from history items with IDs {history_items_ids}')

        return self.__handle_request(CommandId.DOWNLOAD_HISTORY_ITEMS, history_items_ids=history_items_ids)

    def get_user_subscription_info(self) -> UserSubscriptionInfo:
        """
        Gets the subscription information for the current user.

        :return: A `UserSubscriptionInfo` object representing the user's subscription information.
        """
        logger.info('Getting user subscription info')

        return self.__handle_request(CommandId.GET_USER_SUBSCRIPTION_INFO)

    def get_user_info(self) -> UserInfo:
        """
        Gets the information for the current user.

        :return: A `UserInfo` object representing the user's information.
        """
        logger.info('Getting user info')

        return self.__handle_request(CommandId.GET_USER_INFO)

    def get_api_version(self) -> str:
        """
        Gets the version of the API currently supported by the SDK.

        :return: A string containing the version of the API.
        """
        logger.info(f'Getting supported API version')

        with open(API_SPEC_FILE_PATH) as file:
            return json.loads(file.read())['info']['version']

    def get_openapi_specification(self) -> dict:
        """
        Returns the OpenAPI specification of the API currently supported by the SDK.

        :return: A string containing the OpenAPI specification.
        """
        logger.info(f'Getting OpenAPI specification')

        with open(API_SPEC_FILE_PATH) as file:
            return json.loads(file.read())

    def __handle_request(self, command_id: CommandId, **kwargs) -> Any:
        self.__input_validator.validate(command_id, **kwargs)

        url: str = self.__url_builder.build(command_id, **kwargs)
        params: dict = self.__params_builder.build(command_id, **kwargs)
        response: Response = self.__request_handler.send(command_id, url, params)

        return self.__response_handler.process(command_id, response)
