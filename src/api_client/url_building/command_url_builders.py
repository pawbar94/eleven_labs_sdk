from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.url_building.add_voice_url_builder import AddVoiceUrlBuilder
from src.api_client.url_building.delete_history_item_url_builder import DeleteHistoryItemUrlBuilder
from src.api_client.url_building.delete_sample_url_builder import DeleteSampleUrlBuilder
from src.api_client.url_building.delete_voice_url_builder import DeleteVoiceUrlBuilder
from src.api_client.url_building.download_history_items_url_builder import DownloadHistoryItemsUrlBuilder
from src.api_client.url_building.edit_voice_settings_url_builder import EditVoiceSettingsUrlBuilder
from src.api_client.url_building.edit_voice_url_builder import EditVoiceUrlBuilder
from src.api_client.url_building.get_audio_from_history_item_url_builder import GetAudioFromHistoryItemUrlBuilder
from src.api_client.url_building.get_audio_from_sample_url_builder import GetAudioFromSampleUrlBuilder
from src.api_client.url_building.get_default_voice_settings_url_builder import GetDefaultVoiceSettingsUrlBuilder
from src.api_client.url_building.get_generated_items_url_builder import GetGeneratedItemsUrlBuilder
from src.api_client.url_building.get_history_item_url_builder import GetHistoryItemUrlBuilder
from src.api_client.url_building.get_models_url_builder import GetModelsUrlBuilder
from src.api_client.url_building.get_user_info_url_builder import GetUserInfoUrlBuilder
from src.api_client.url_building.get_user_subscription_info_url_builder import GetUserSubscriptionInfoUrlBuilder
from src.api_client.url_building.get_voice_settings_url_builder import GetVoiceSettingsUrlBuilder
from src.api_client.url_building.get_voice_url_builder import GetVoiceUrlBuilder
from src.api_client.url_building.get_voices_url_builder import GetVoicesUrlBuilder
from src.api_client.url_building.text_to_speech_url_builder import TextToSpeechUrlBuilder
from src.api_client.url_building.url_builder_interface import UrlBuilderInterface

COMMAND_URL_BUILDERS: Dict[CommandId, UrlBuilderInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechUrlBuilder(),
    CommandId.GET_MODELS: GetModelsUrlBuilder(),
    CommandId.GET_VOICES: GetVoicesUrlBuilder(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsUrlBuilder(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsUrlBuilder(),
    CommandId.GET_VOICE: GetVoiceUrlBuilder(),
    CommandId.DELETE_VOICE: DeleteVoiceUrlBuilder(),
    CommandId.EDIT_VOICE_SETTINGS: EditVoiceSettingsUrlBuilder(),
    CommandId.ADD_VOICE: AddVoiceUrlBuilder(),
    CommandId.EDIT_VOICE: EditVoiceUrlBuilder(),
    CommandId.DELETE_SAMPLE: DeleteSampleUrlBuilder(),
    CommandId.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleUrlBuilder(),
    CommandId.GET_GENERATED_ITEMS: GetGeneratedItemsUrlBuilder(),
    CommandId.GET_HISTORY_ITEM_BY_ID: GetHistoryItemUrlBuilder(),
    CommandId.DELETE_HISTORY_ITEM: DeleteHistoryItemUrlBuilder(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemUrlBuilder(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsUrlBuilder(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoUrlBuilder(),
    CommandId.GET_USER_INFO: GetUserInfoUrlBuilder()
}
