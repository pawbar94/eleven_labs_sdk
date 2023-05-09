from typing import Type, Dict
from api_client.command_id import RequestID
from old.eleven_labs_api.responses.add_voice_response import AddVoiceResponse
from old.eleven_labs_api.responses.delete_history_item_response import DeleteHistoryItemResponse
from old.eleven_labs_api.responses.delete_sample_response import DeleteSampleResponse
from old.eleven_labs_api.responses.delete_voice_response import DeleteVoiceResponse
from old.eleven_labs_api.responses.download_history_items_response import DownloadHistoryItemsResponse
from old.eleven_labs_api.responses.edit_voice_response import EditVoiceResponse
from old.eleven_labs_api.responses.edit_voice_settings_response import EditVoiceSettingsResponse
from old.eleven_labs_api.responses.get_audio_from_history_item_response import GetAudioFromHistoryItemResponse
from old.eleven_labs_api.responses.get_audio_from_sample_response import GetAudioFromSampleResponse
from old.eleven_labs_api.responses.get_default_voice_settings_response import GetDefaultVoiceSettingsResponse
from old.eleven_labs_api.responses.get_generated_items_response import GetGeneratedItemsResponse
from old.eleven_labs_api.responses.get_user_info_response import GetUserInfoResponse
from old.eleven_labs_api.responses.get_user_subscription_info_response import GetUserSubscriptionInfoResponse
from old.eleven_labs_api.responses.get_voice_response import GetVoiceResponse
from old.eleven_labs_api.responses.get_voice_settings_response import GetVoiceSettingsResponse
from old.eleven_labs_api.responses.get_voices_response import GetVoicesResponse
from old.eleven_labs_api.responses.response_interface import ResponseInterface
from old.eleven_labs_api.responses.text_to_speech_audio_response import TextToSpeechAudioResponse
from old.eleven_labs_api.responses.text_to_speech_stream_response import TextToSpeechStreamResponse

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
