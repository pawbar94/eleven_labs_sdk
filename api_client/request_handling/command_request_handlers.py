from typing import Dict
from api_client.command_id import CommandId
from api_client.request_handling.add_voice_request_handler import AddVoiceRequestHandler
from api_client.request_handling.delete_history_item_request_handler import DeleteHistoryItemRequestHandler
from api_client.request_handling.delete_sample_request_handler import DeleteSampleRequestHandler
from api_client.request_handling.delete_voice_request_handler import DeleteVoiceRequestHandler
from api_client.request_handling.download_history_items_request_handler import DownloadHistoryItemsRequestHandler
from api_client.request_handling.edit_voice_request_handler import EditVoiceRequestHandler
from api_client.request_handling.edit_voice_settings_request_handler import EditVoiceSettingsRequestHandler
from api_client.request_handling.get_audio_from_history_item_request_handler import \
    GetAudioFromHistoryItemRequestHandler
from api_client.request_handling.get_audio_from_sample_request_handler import GetAudioFromSampleRequestHandler
from api_client.request_handling.get_default_voice_settings_request_handler import GetDefaultVoiceSettingsRequestHandler
from api_client.request_handling.get_generated_items_request_handler import GetGeneratedItemsRequestHandler
from api_client.request_handling.get_history_item_request_handler import GetHistoryItemRequestHandler
from api_client.request_handling.get_models_request_handler import GetModelsRequestHandler
from api_client.request_handling.get_user_info_request_handler import GetUserInfoRequestHandler
from api_client.request_handling.get_user_subscription_info_request_handler import GetUserSubscriptionInfoRequestHandler
from api_client.request_handling.get_voice_request_handler import GetVoiceRequestHandler
from api_client.request_handling.get_voice_settings_request_handler import GetVoiceSettingsRequestHandler
from api_client.request_handling.get_voices_request_handler import GetVoicesRequestHandler
from api_client.request_handling.request_handler_interface import RequestHandlerInterface
from api_client.request_handling.text_to_speech_request_handler import TextToSpeechRequestHandler

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
