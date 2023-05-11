from typing import Dict
from api_client.command_id import CommandId
from api_client.url_building.add_voice_url_builder import AddVoiceUrlBuilder
from api_client.url_building.delete_history_item_url_builder import DeleteHistoryItemUrlBuilder
from api_client.url_building.delete_sample_url_builder import DeleteSampleUrlBuilder
from api_client.url_building.delete_voice_url_builder import DeleteVoiceUrlBuilder
from api_client.url_building.download_history_items_url_builder import DownloadHistoryItemsUrlBuilder
from api_client.url_building.edit_voice_settings_url_builder import EditVoiceSettingsUrlBuilder
from api_client.url_building.edit_voice_url_builder import EditVoiceUrlBuilder
from api_client.url_building.get_audio_from_history_item_url_builder import GetAudioFromHistoryItemUrlBuilder
from api_client.url_building.get_audio_from_sample_url_builder import GetAudioFromSampleUrlBuilder
from api_client.url_building.get_default_voice_settings_url_builder import GetDefaultVoiceSettingsUrlBuilder
from api_client.url_building.get_generated_items_url_builder import GetGeneratedItemsUrlBuilder
from api_client.url_building.get_history_item_url_builder import GetHistoryItemUrlBuilder
from api_client.url_building.get_models_url_builder import GetModelsUrlBuilder
from api_client.url_building.get_user_info_url_builder import GetUserInfoUrlBuilder
from api_client.url_building.get_user_subscription_info_url_builder import GetUserSubscriptionInfoUrlBuilder
from api_client.url_building.get_voice_settings_url_builder import GetVoiceSettingsUrlBuilder
from api_client.url_building.get_voice_url_builder import GetVoiceUrlBuilder
from api_client.url_building.get_voices_url_builder import GetVoicesUrlBuilder
from api_client.url_building.text_to_speech_url_builder import TextToSpeechUrlBuilder
from api_client.url_building.url_builder_interface import UrlBuilderInterface

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
