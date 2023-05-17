from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.response_handling.add_voice_response_handler import AddVoiceResponseHandler
from src.api_client.response_handling.delete_history_item_response_handler import DeleteHistoryItemResponseHandler
from src.api_client.response_handling.delete_sample_response_handler import DeleteSampleResponseHandler
from src.api_client.response_handling.delete_voice_response_handler import DeleteVoiceResponseHandler
from src.api_client.response_handling.download_history_items_response_handler import DownloadHistoryItemsResponseHandler
from src.api_client.response_handling.edit_voice_response_handler import EditVoiceResponseHandler
from src.api_client.response_handling.edit_voice_settings_response_handler import EditVoiceSettingsResponseHandler
from src.api_client.response_handling.get_audio_from_history_item_response_handler import \
    GetAudioFromHistoryItemResponseHandler
from src.api_client.response_handling.get_audio_from_sample_response_handler import GetAudioFromSampleResponseHandler
from src.api_client.response_handling.get_default_voice_settings_response_handler import \
    GetDefaultVoiceSettingsResponseHandler
from src.api_client.response_handling.get_generated_items_response_handler import GetGeneratedItemsResponseHandler
from src.api_client.response_handling.get_history_item_response_handler import GetHistoryItemResponseHandler
from src.api_client.response_handling.get_models_response_handler import GetModelsResponseHandler
from src.api_client.response_handling.get_user_info_response_handler import GetUserInfoResponseHandler
from src.api_client.response_handling.get_user_subscription_info_response_handler import \
    GetUserSubscriptionInfoResponseHandler
from src.api_client.response_handling.get_voice_response_handler import GetVoiceResponseHandler
from src.api_client.response_handling.get_voice_settings_response_handler import GetVoiceSettingsResponseHandler
from src.api_client.response_handling.get_voices_response_handler import GetVoicesResponseHandler
from src.api_client.response_handling.response_handler_interface import ResponseHandlerInterface
from src.api_client.response_handling.text_to_speech_response_handler import TextToSpeechResponseHandler

COMMAND_RESPONSE_HANDLERS: Dict[CommandId, ResponseHandlerInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechResponseHandler(),
    CommandId.GET_MODELS: GetModelsResponseHandler(),
    CommandId.GET_VOICES: GetVoicesResponseHandler(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsResponseHandler(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsResponseHandler(),
    CommandId.GET_VOICE: GetVoiceResponseHandler(),
    CommandId.DELETE_VOICE: DeleteVoiceResponseHandler(),
    CommandId.EDIT_VOICE_SETTINGS: EditVoiceSettingsResponseHandler(),
    CommandId.ADD_VOICE: AddVoiceResponseHandler(),
    CommandId.EDIT_VOICE: EditVoiceResponseHandler(),
    CommandId.DELETE_SAMPLE: DeleteSampleResponseHandler(),
    CommandId.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleResponseHandler(),
    CommandId.GET_GENERATED_ITEMS: GetGeneratedItemsResponseHandler(),
    CommandId.GET_HISTORY_ITEM_BY_ID: GetHistoryItemResponseHandler(),
    CommandId.DELETE_HISTORY_ITEM: DeleteHistoryItemResponseHandler(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemResponseHandler(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsResponseHandler(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoResponseHandler(),
    CommandId.GET_USER_INFO: GetUserInfoResponseHandler()
}
