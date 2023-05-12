from typing import Dict
from api_client.command_id import CommandId
from api_client.request_handling.add_voice_request_handler import AddVoiceResponseHandler
from api_client.request_handling.delete_history_item_request_handler import DeleteHistoryItemResponseHandler
from api_client.request_handling.delete_sample_request_handler import DeleteSampleResponseHandler
from api_client.request_handling.delete_voice_request_handler import DeleteVoiceResponseHandler
from api_client.request_handling.download_history_items_request_handler import DownloadHistoryItemsResponseHandler
from api_client.request_handling.edit_voice_request_handler import EditVoiceResponseHandler
from api_client.request_handling.edit_voice_settings_request_handler import EditVoiceSettingsResponseHandler
from api_client.request_handling.get_audio_from_history_item_request_handler import \
    GetAudioFromHistoryItemResponseHandler
from api_client.request_handling.get_audio_from_sample_request_handler import GetAudioFromSampleResponseHandler
from api_client.request_handling.get_default_voice_settings_request_handler import GetDefaultVoiceSettingsResponseHandler
from api_client.request_handling.get_generated_items_request_handler import GetGeneratedItemsResponseHandler
from api_client.request_handling.get_history_item_request_handler import GetHistoryItemResponseHandler
from api_client.request_handling.get_models_request_handler import GetModelsResponseHandler
from api_client.request_handling.get_user_info_request_handler import GetUserInfoResponseHandler
from api_client.request_handling.get_user_subscription_info_request_handler import GetUserSubscriptionInfoResponseHandler
from api_client.request_handling.get_voice_request_handler import GetVoiceResponseHandler
from api_client.request_handling.get_voice_settings_request_handler import GetVoiceSettingsResponseHandler
from api_client.request_handling.get_voices_request_handler import GetVoicesResponseHandler
from api_client.request_handling.request_handler_interface import ResponseHandlerInterface
from api_client.request_handling.text_to_speech_request_handler import TextToSpeechResponseHandler

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
