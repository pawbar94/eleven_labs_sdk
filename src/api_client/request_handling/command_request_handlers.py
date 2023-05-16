from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.request_handling.add_voice_request_handler import AddVoiceRequestHandler
from src.api_client.request_handling.delete_history_item_request_handler import DeleteHistoryItemRequestHandler
from src.api_client.request_handling.delete_sample_request_handler import DeleteSampleRequestHandler
from src.api_client.request_handling.delete_voice_request_handler import DeleteVoiceRequestHandler
from src.api_client.request_handling.download_history_items_request_handler import DownloadHistoryItemsRequestHandler
from src.api_client.request_handling.edit_voice_request_handler import EditVoiceRequestHandler
from src.api_client.request_handling.edit_voice_settings_request_handler import EditVoiceSettingsRequestHandler
from src.api_client.request_handling.get_audio_from_history_item_request_handler import \
    GetAudioFromHistoryItemRequestHandler
from src.api_client.request_handling.get_audio_from_sample_request_handler import GetAudioFromSampleRequestHandler
from src.api_client.request_handling.get_default_voice_settings_request_handler import GetDefaultVoiceSettingsRequestHandler
from src.api_client.request_handling.get_generated_items_request_handler import GetGeneratedItemsRequestHandler
from src.api_client.request_handling.get_history_item_request_handler import GetHistoryItemRequestHandler
from src.api_client.request_handling.get_models_request_handler import GetModelsRequestHandler
from src.api_client.request_handling.get_user_info_request_handler import GetUserInfoRequestHandler
from src.api_client.request_handling.get_user_subscription_info_request_handler import GetUserSubscriptionInfoRequestHandler
from src.api_client.request_handling.get_voice_request_handler import GetVoiceRequestHandler
from src.api_client.request_handling.get_voice_settings_request_handler import GetVoiceSettingsRequestHandler
from src.api_client.request_handling.get_voices_request_handler import GetVoicesRequestHandler
from src.api_client.request_handling.request_handler_interface import RequestHandlerInterface
from src.api_client.request_handling.text_to_speech_request_handler import TextToSpeechRequestHandler

COMMAND_REQUEST_HANDLERS: Dict[CommandId, RequestHandlerInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechRequestHandler(),
    CommandId.GET_MODELS: GetModelsRequestHandler(),
    CommandId.GET_VOICES: GetVoicesRequestHandler(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsRequestHandler(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsRequestHandler(),
    CommandId.GET_VOICE: GetVoiceRequestHandler(),
    CommandId.DELETE_VOICE: DeleteVoiceRequestHandler(),
    CommandId.EDIT_VOICE_SETTINGS: EditVoiceSettingsRequestHandler(),
    CommandId.ADD_VOICE: AddVoiceRequestHandler(),
    CommandId.EDIT_VOICE: EditVoiceRequestHandler(),
    CommandId.DELETE_SAMPLE: DeleteSampleRequestHandler(),
    CommandId.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleRequestHandler(),
    CommandId.GET_GENERATED_ITEMS: GetGeneratedItemsRequestHandler(),
    CommandId.GET_HISTORY_ITEM_BY_ID: GetHistoryItemRequestHandler(),
    CommandId.DELETE_HISTORY_ITEM: DeleteHistoryItemRequestHandler(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemRequestHandler(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsRequestHandler(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoRequestHandler(),
    CommandId.GET_USER_INFO: GetUserInfoRequestHandler()
}
