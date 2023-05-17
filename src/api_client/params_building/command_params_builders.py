from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.params_building.add_voice_params_builder import AddVoiceParamsBuilder
from src.api_client.params_building.delete_history_item_params_builder import DeleteHistoryItemParamsBuilder
from src.api_client.params_building.delete_sample_params_builder import DeleteSampleParamsBuilder
from src.api_client.params_building.delete_voice_params_builder import DeleteVoiceParamsBuilder
from src.api_client.params_building.download_history_items_params_builder import DownloadHistoryItemsParamsBuilder
from src.api_client.params_building.edit_voice_params_builder import EditVoiceParamsBuilder
from src.api_client.params_building.edit_voice_settings_params_builder import EditVoiceSettingsParamsBuilder
from src.api_client.params_building.get_audio_from_history_item_params_builder import GetAudioFromHistoryItemParamsBuilder
from src.api_client.params_building.get_audio_from_sample_params_builder import GetAudioFromSampleParamsBuilder
from src.api_client.params_building.get_default_voice_settings_params_builder import GetDefaultVoiceSettingsParamsBuilder
from src.api_client.params_building.get_generated_items_params_builder import GetGeneratedItemsParamsBuilder
from src.api_client.params_building.get_history_item_params_builder import GetHistoryItemParamsBuilder
from src.api_client.params_building.get_models_params_builder import GetModelsParamsBuilder
from src.api_client.params_building.get_user_info_params_builder import GetUserInfoParamsBuilder
from src.api_client.params_building.get_user_subscription_info_params_builder import GetUserSubscriptionInfoParamsBuilder
from src.api_client.params_building.get_voice_params_builder import GetVoiceParamsBuilder
from src.api_client.params_building.get_voice_settings_params_builder import GetVoiceSettingsParamsBuilder
from src.api_client.params_building.get_voices_params_builder import GetVoicesParamsBuilder
from src.api_client.params_building.params_builder_interface import ParamsBuilderInterface
from src.api_client.params_building.text_to_speech_params_builder import TextToSpeechParamsBuilder

COMMAND_PARAMS_BUILDERS: Dict[CommandId, ParamsBuilderInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechParamsBuilder(),
    CommandId.GET_MODELS: GetModelsParamsBuilder(),
    CommandId.GET_VOICES: GetVoicesParamsBuilder(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsParamsBuilder(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsParamsBuilder(),
    CommandId.GET_VOICE: GetVoiceParamsBuilder(),
    CommandId.DELETE_VOICE: DeleteVoiceParamsBuilder(),
    CommandId.EDIT_VOICE_SETTINGS: EditVoiceSettingsParamsBuilder(),
    CommandId.ADD_VOICE: AddVoiceParamsBuilder(),
    CommandId.EDIT_VOICE: EditVoiceParamsBuilder(),
    CommandId.DELETE_SAMPLE: DeleteSampleParamsBuilder(),
    CommandId.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleParamsBuilder(),
    CommandId.GET_GENERATED_ITEMS: GetGeneratedItemsParamsBuilder(),
    CommandId.GET_HISTORY_ITEM_BY_ID: GetHistoryItemParamsBuilder(),
    CommandId.DELETE_HISTORY_ITEM: DeleteHistoryItemParamsBuilder(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemParamsBuilder(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsParamsBuilder(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoParamsBuilder(),
    CommandId.GET_USER_INFO: GetUserInfoParamsBuilder()
}
