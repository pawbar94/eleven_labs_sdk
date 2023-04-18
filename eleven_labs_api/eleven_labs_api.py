import traceback
from typing import Any, List
import requests
from eleven_labs_api.requests.request_sender import RequestSender
from eleven_labs_api.requests.request_code import RequestCode
from eleven_labs_api.requests.request_factory import RequestFactory
from eleven_labs_api.requests.request_id import RequestID
from eleven_labs_api.requests.request_interface import RequestInterface
from eleven_labs_api.responses.history_item_model.history_item import HistoryItem
from eleven_labs_api.responses.response_factory import ResponseFactory
from eleven_labs_api.responses.response_interface import ResponseInterface
from eleven_labs_api.responses.user_info_model.user_info import UserInfo
from eleven_labs_api.responses.user_info_model.user_subscription_info import UserSubscriptionInfo
from eleven_labs_api.responses.voice_model.voice import Voice, VoiceID
from eleven_labs_api.responses.voice_model.voice_settings import VoiceSettings
from logging import getLogger

logger = getLogger('ElevenLabsApi')


class ElevenLabsApi:
    def __init__(self, api_key: str):
        self.__api_key: str = api_key

    def text_to_speech_audio(self, text: str, voice: Voice, output_file_path: str) -> None:
        """
        Convert the given text to an audio file using the specified voice and save it to the given file path.

        :param text: The text to convert to speech.
        :param voice: The voice to use for the text-to-speech conversion.
        :param output_file_path: The file path to save the generated audio file to.
        """
        try:
            logger.info(f'Converting text to speech using {voice.name} voice and saving it to {output_file_path} file')
            logger.debug(f'\nVoice to use: {voice}\n'
                         f'Text to convert:{text}\n')

            return self.__handle_request(RequestCode.POST, RequestID.TEXT_TO_SPEECH_AUDIO,
                                         request_params={'voice_id': voice.id, 'text': text,
                                                         'stability': voice.settings.stability,
                                                         'similarity_boost': voice.settings.similarity_boost},
                                         response_params={'output_file_path': output_file_path},
                                         accept_content='audio/mpeg')
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def text_to_speech_stream(self, text: str, voice: Voice) -> bytes:
        """
        Convert the given text to speech using the specified voice and return the resulting audio as a bytes stream.

        :param text: The text to convert to speech.
        :param voice: The voice to use for the text-to-speech conversion.
        :return: A bytes object containing the generated audio.
        """
        try:
            logger.info(f'Converting text to speech stream using {voice.name} voice')
            logger.debug(f'\nVoice to use: {voice}\n'
                         f'Text to convert:{text}\n')

            return self.__handle_request(RequestCode.POST, RequestID.TEXT_TO_SPEECH_AUDIO,
                                         request_params={'voice_id': voice.id, 'text': text,
                                                         'stability': voice.settings.stability,
                                                         'similarity_boost': voice.settings.similarity_boost})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_voices(self) -> List[Voice]:
        """
        Get a list of available voices that can be used for text-to-speech conversion.

        :return: A list of available voices.
        """
        try:
            logger.info('Getting all voices')
            return self.__handle_request(RequestCode.GET, RequestID.GET_VOICES)
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_default_voice_settings(self) -> VoiceSettings:
        """
        Get the default voice settings for text-to-speech conversion.

        :return: The default voice settings.
        """
        try:
            logger.info('Getting default voice settings')
            return self.__handle_request(RequestCode.GET, RequestID.GET_DEFAULT_VOICE_SETTINGS)
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_voice_settings(self, voice: Voice) -> VoiceSettings:
        """
        Get settings for the specified voice for text-to-speech conversion.

        :param voice: The voice to get the settings for.
        :return: The voice settings for the specified voice.
        """
        try:
            logger.info(f'Getting settings for {voice.name} voice')
            return self.__handle_request(RequestCode.GET, RequestID.GET_VOICE_SETTINGS,
                                         request_params={'voice_id': voice.id})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_voice(self, voice_id: str) -> Voice:
        """
        Get the voice with the specified ID for text-to-speech conversion.

        :param voice_id: The ID of the voice to get.
        :return: The voice object with the specified ID.
        """
        try:
            logger.info(f'Getting voice with ID {voice_id}')
            return self.__handle_request(RequestCode.GET, RequestID.GET_VOICE,
                                         request_params={'voice_id': voice_id})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def delete_voice(self, voice: Voice) -> str:
        """
        Delete the specified voice from the account.

        :param voice: The voice to delete.
        :return: A string indicating the result of the deletion.
        """
        try:
            logger.info(f'Deleting {voice.name} voice')
            return self.__handle_request(RequestCode.DELETE, RequestID.DELETE_VOICE,
                                         request_params={'voice_id': voice.id})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def edit_voice_settings(self, voice: Voice, voice_settings: VoiceSettings) -> str:
        """
        Edit settings for the specified voice.

        :param voice: The voice to edit the settings for.
        :param voice_settings: The new voice settings to use for the voice.
        :return: A string indicating the result of the operation.
        """
        try:
            logger.info(f'Editing settings for {voice.name} voice. New settings: {voice_settings}')
            return self.__handle_request(RequestCode.POST, RequestID.EDIT_VOICE_SETTINGS,
                                         request_params={'voice_id': voice.id, 'stability': voice_settings.stability,
                                                         'similarity_boost': voice_settings.similarity_boost})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def add_voice(self, name: str, files: list, description: str, labels: str) -> VoiceID:
        """
        Add a new voice to your account.

        :param name: The name of the new voice.
        :param files: A list of files for the voice's samples.
        :param description: A description of the new voice.
        :param labels: A serialized string with labels for the new voice.
        :return: The ID of the newly added voice.
        """
        try:
            logger.info(f'Adding new voice with name {name}')
            logger.debug(f'\nVoice name: {name}\n'
                         f'Voice files: {files}\n'
                         f'Voice description: {description}\n'
                         f'Voice labels: {labels}\n')

            return self.__handle_request(RequestCode.POST, RequestID.ADD_VOICE,
                                         request_params={'name': name, 'files': files, 'description': description,
                                                         'labels': labels})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def edit_voice(self, voice: Voice, name: str, files: list, description: str, labels: str) -> VoiceID:
        """
        Edit an existing voice.

        :param voice: The voice to edit.
        :param name: The new name for the voice.
        :param files: A list of files for the voice's samples.
        :param description: The new description for the voice.
        :param labels: A serialized string with labels for the new voice.
        :return: The ID of the edited voice.
        """
        try:
            logger.info(f'Editing {voice.name} voice')
            logger.debug(f'\nVoice name: {name}\n'
                         f'Voice files: {files}\n'
                         f'Voice description: {description}\n'
                         f'Voice labels: {labels}\n')

            return self.__handle_request(RequestCode.POST, RequestID.EDIT_VOICE,
                                         request_params={'voice_id': voice.id, 'name': name, 'files': files,
                                                         'description': description, 'labels': labels})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def delete_sample(self, voice: Voice, sample_id: str) -> str:
        """
        Deletes a sample for the given voice from the account.

        :param voice: The voice to which the sample belongs.
        :param sample_id: The ID of the sample to delete.
        :return: A message indicating whether the sample was successfully deleted.
        """
        try:
            logger.info(f'Deleting sample with ID {sample_id} from {voice.name} voice')
            return self.__handle_request(RequestCode.DELETE, RequestID.DELETE_SAMPLE,
                                         request_params={'voice_id': voice.id, 'sample_id': sample_id})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_audio_from_sample(self, voice: Voice, sample_id: str, output_file_path: str) -> None:
        """
        Generates an audio file for the given sample and saves it to the specified output file path.

        :param voice: The voice to which the sample belongs.
        :param sample_id: The ID of the sample to generate audio for.
        :param output_file_path: The path of the output file where the generated audio will be saved.
        """
        try:
            logger.info(f'Getting audio from sample with ID {sample_id} from {voice.name} voice and saving it to '
                        f'{output_file_path} file')
            return self.__handle_request(RequestCode.GET, RequestID.GET_AUDIO_FROM_SAMPLE,
                                         request_params={'voice_id': voice.id, 'sample_id': sample_id},
                                         response_params={'output_file_path': output_file_path},
                                         accept_content=f'audio/{output_file_path.split(".")[-1]}')
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_generated_items(self) -> List[HistoryItem]:
        """
        Returns a list of all history items generated on your account.

        :return: A list of history items.
        """
        try:
            logger.info('Getting generated history items')
            return self.__handle_request(RequestCode.GET, RequestID.GET_GENERATED_ITEMS)
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_audio_from_history_item(self, history_item: HistoryItem, output_file_path: str) -> None:
        """
        Generates an audio file for the given history item and saves it to the specified output file path.

        :param history_item: The history item to generate audio for.
        :param output_file_path: The path of the output file where the generated audio will be saved.
        """
        try:
            logger.info(f'Getting audio from history item with ID {history_item.id} and saving it to '
                        f'{output_file_path} file')
            logger.debug(f'History item: {history_item}')

            return self.__handle_request(RequestCode.GET, RequestID.GET_AUDIO_FROM_HISTORY_ITEM,
                                         request_params={'history_item_id': history_item.id},
                                         response_params={'output_file_path': output_file_path},
                                         accept_content=f'audio/{output_file_path.split(".")[-1]}')
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def delete_history_item(self, history_item: HistoryItem) -> str:
        """
        Deletes the specified history item from the account.

        :param history_item: The history item to delete.
        :return: A message indicating whether the history item was successfully deleted.
        """
        try:
            logger.info(f'Deleting history item with ID {history_item.id}')
            logger.debug(f'History item: {history_item}')

            return self.__handle_request(RequestCode.DELETE, RequestID.DELETE_HISTORY_ITEM,
                                         request_params={'history_item_id': history_item.id})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def download_history_items(self, history_items_ids: List[str], output_file_path: str) -> None:
        """
        Downloads the specified history items to the specified output file path. If there is only one item ID provided,
        there will be a .mpeg audio file generated. If there are multiple item IDs provided, there will be a .zip file
        generated.

        :param history_items_ids: A list of IDs of the history items to download.
        :param output_file_path: The path of the output file where the zip file will be saved.
        """
        try:
            logger.info(f'Downloading history items with IDs {history_items_ids}')
            return self.__handle_request(RequestCode.POST, RequestID.DOWNLOAD_HISTORY_ITEMS,
                                         request_params={'history_items_ids': history_items_ids},
                                         response_params={'history_items_ids': history_items_ids,
                                                          'output_file_path': output_file_path})
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_user_subscription_info(self) -> UserSubscriptionInfo:
        """
        Returns information about the user's subscription.

        :return: An object containing information about the user's subscription.
        """
        try:
            logger.info('Getting user subscription info')
            return self.__handle_request(RequestCode.GET, RequestID.GET_USER_SUBSCRIPTION_INFO)
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def get_user_info(self) -> UserInfo:
        """
        Returns information about the user.

        :return: An object containing information about the user.
        """
        try:
            logger.info('Getting user info')
            return self.__handle_request(RequestCode.GET, RequestID.GET_USER_INFO)
        except Exception as e:
            logger.error(f'{e}\n{traceback.format_exc()}')

    def __handle_request(self, request_code: RequestCode, request_id: RequestID, request_params: dict = None,
                         response_params: dict = None, accept_content: str = '') -> Any:
        if request_params is None:
            request_params = {}
        if response_params is None:
            response_params = {}

        request: RequestInterface = RequestFactory.create(request_id)(**request_params)
        raw_response: requests.Response = RequestSender.send(request_code, self.__api_key, request.uri(),
                                                             request.payload(), accept_content)
        response: ResponseInterface = ResponseFactory.create(request_id)(raw_response, **response_params)

        return response.process()
