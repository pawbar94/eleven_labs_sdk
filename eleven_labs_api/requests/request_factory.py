from typing import Dict, Type

from eleven_labs_api.requests.add_voice_request import AddVoiceRequest
from eleven_labs_api.requests.delete_history_item_request import DeleteHistoryItemRequest
from eleven_labs_api.requests.delete_sample_request import DeleteSampleRequest
from eleven_labs_api.requests.delete_voice_request import DeleteVoiceRequest
from eleven_labs_api.requests.download_history_items_request import DownloadHistoryItemsRequest
from eleven_labs_api.requests.edit_voice_request import EditVoiceRequest
from eleven_labs_api.requests.edit_voice_settings_request import EditVoiceSettingsRequest
from eleven_labs_api.requests.get_audio_from_history_item_request import GetAudioFromHistoryItemRequest
from eleven_labs_api.requests.get_audio_from_sample_request import GetAudioFromSampleRequest
from eleven_labs_api.requests.get_default_voice_settings_request import GetDefaultVoiceSettingsRequest
from eleven_labs_api.requests.get_generated_items_request import GetGeneratedItemsRequest
from eleven_labs_api.requests.get_user_info_request import GetUserInfoRequest
from eleven_labs_api.requests.get_user_subscription_info_request import GetUserSubscriptionInfoRequest
from eleven_labs_api.requests.get_voice_request import GetVoiceRequest
from eleven_labs_api.requests.get_voice_settings_request import GetVoiceSettingsRequest
from eleven_labs_api.requests.get_voices_request import GetVoicesRequest
from eleven_labs_api.requests.request_id import RequestID
from eleven_labs_api.requests.request_interface import RequestInterface
from eleven_labs_api.requests.text_to_speech_audio_request import TextToSpeechAudioRequest
from eleven_labs_api.requests.text_to_speech_stream_request import TextToSpeechStreamRequest

SUPPORTED_REQUESTS: Dict[RequestID, Type[RequestInterface]] = {
    RequestID.TEXT_TO_SPEECH_AUDIO: TextToSpeechAudioRequest,
    RequestID.TEXT_TO_SPEECH_STREAM: TextToSpeechStreamRequest,
    RequestID.GET_VOICES: GetVoicesRequest,
    RequestID.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsRequest,
    RequestID.GET_VOICE_SETTINGS: GetVoiceSettingsRequest,
    RequestID.GET_VOICE: GetVoiceRequest,
    RequestID.DELETE_VOICE: DeleteVoiceRequest,
    RequestID.EDIT_VOICE_SETTINGS: EditVoiceSettingsRequest,
    RequestID.ADD_VOICE: AddVoiceRequest,
    RequestID.EDIT_VOICE: EditVoiceRequest,
    RequestID.DELETE_SAMPLE: DeleteSampleRequest,
    RequestID.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleRequest,
    RequestID.GET_GENERATED_ITEMS: GetGeneratedItemsRequest,
    RequestID.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemRequest,
    RequestID.DELETE_HISTORY_ITEM: DeleteHistoryItemRequest,
    RequestID.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsRequest,
    RequestID.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoRequest,
    RequestID.GET_USER_INFO: GetUserInfoRequest
}


class RequestFactory:
    @staticmethod
    def create(request_id: RequestID) -> Type[RequestInterface]:
        return SUPPORTED_REQUESTS[request_id]
