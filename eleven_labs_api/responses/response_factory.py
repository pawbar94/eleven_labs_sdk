from typing import Type, Dict
from eleven_labs_api.requests.request_id import RequestID
from eleven_labs_api.responses.add_voice_response import AddVoiceResponse
from eleven_labs_api.responses.delete_history_item_response import DeleteHistoryItemResponse
from eleven_labs_api.responses.delete_sample_response import DeleteSampleResponse
from eleven_labs_api.responses.delete_voice_response import DeleteVoiceResponse
from eleven_labs_api.responses.download_history_items_response import DownloadHistoryItemsResponse
from eleven_labs_api.responses.edit_voice_response import EditVoiceResponse
from eleven_labs_api.responses.edit_voice_settings_response import EditVoiceSettingsResponse
from eleven_labs_api.responses.get_audio_from_history_item_response import GetAudioFromHistoryItemResponse
from eleven_labs_api.responses.get_audio_from_sample_response import GetAudioFromSampleResponse
from eleven_labs_api.responses.get_default_voice_settings_response import GetDefaultVoiceSettingsResponse
from eleven_labs_api.responses.get_generated_items_response import GetGeneratedItemsResponse
from eleven_labs_api.responses.get_user_info_response import GetUserInfoResponse
from eleven_labs_api.responses.get_user_subscription_info_response import GetUserSubscriptionInfoResponse
from eleven_labs_api.responses.get_voice_response import GetVoiceResponse
from eleven_labs_api.responses.get_voice_settings_response import GetVoiceSettingsResponse
from eleven_labs_api.responses.get_voices_response import GetVoicesResponse
from eleven_labs_api.responses.response_interface import ResponseInterface
from eleven_labs_api.responses.text_to_speech_audio_response import TextToSpeechAudioResponse
from eleven_labs_api.responses.text_to_speech_stream_response import TextToSpeechStreamResponse

SUPPORTED_RESPONSES: Dict[RequestID, Type[ResponseInterface]] = {
    RequestID.TEXT_TO_SPEECH_AUDIO: TextToSpeechAudioResponse,
    RequestID.TEXT_TO_SPEECH_STREAM: TextToSpeechStreamResponse,
    RequestID.GET_VOICES: GetVoicesResponse,
    RequestID.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsResponse,
    RequestID.GET_VOICE_SETTINGS: GetVoiceSettingsResponse,
    RequestID.GET_VOICE: GetVoiceResponse,
    RequestID.DELETE_VOICE: DeleteVoiceResponse,
    RequestID.EDIT_VOICE_SETTINGS: EditVoiceSettingsResponse,
    RequestID.ADD_VOICE: AddVoiceResponse,
    RequestID.EDIT_VOICE: EditVoiceResponse,
    RequestID.DELETE_SAMPLE: DeleteSampleResponse,
    RequestID.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleResponse,
    RequestID.GET_GENERATED_ITEMS: GetGeneratedItemsResponse,
    RequestID.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemResponse,
    RequestID.DELETE_HISTORY_ITEM: DeleteHistoryItemResponse,
    RequestID.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsResponse,
    RequestID.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoResponse,
    RequestID.GET_USER_INFO: GetUserInfoResponse
}


class ResponseFactory:
    @staticmethod
    def create(request_id: RequestID) -> Type[ResponseInterface]:
        return SUPPORTED_RESPONSES[request_id]
