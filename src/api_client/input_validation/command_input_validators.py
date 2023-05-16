from typing import Dict
from src.common.enums.command_id import CommandId
from src.api_client.input_validation.add_voice_input_validator import AddVoiceInputValidator
from src.api_client.input_validation.delete_history_item_input_validator import DeleteHistoryItemInputValidator
from src.api_client.input_validation.delete_sample_input_validator import DeleteSampleInputValidator
from src.api_client.input_validation.delete_voice_input_validator import DeleteVoiceInputValidator
from src.api_client.input_validation.download_history_items_input_validator import DownloadHistoryItemsInputValidator
from src.api_client.input_validation.edit_voice_input_validator import EditVoiceInputValidator
from src.api_client.input_validation.edit_voice_settings_input_validator import EditVoiceSettingsInputValidator
from src.api_client.input_validation.get_audio_from_history_item_input_validator import \
    GetAudioFromHistoryItemInputValidator
from src.api_client.input_validation.get_audio_from_sample_input_validator import GetAudioFromSampleInputValidator
from src.api_client.input_validation.get_default_voice_settings_input_validator import GetDefaultVoiceSettingsInputValidator
from src.api_client.input_validation.get_generated_items_input_validator import GetGeneratedItemsInputValidator
from src.api_client.input_validation.get_history_item_input_validator import GetHistoryItemInputValidator
from src.api_client.input_validation.get_models_input_validator import GetModelsInputValidator
from src.api_client.input_validation.get_user_info_input_validator import GetUserInfoInputValidator
from src.api_client.input_validation.get_user_subscription_info_input_validator import GetUserSubscriptionInfoInputValidator
from src.api_client.input_validation.get_voice_input_validator import GetVoiceInputValidator
from src.api_client.input_validation.get_voice_settings_input_validator import GetVoiceSettingsInputValidator
from src.api_client.input_validation.get_voices_input_validator import GetVoicesInputValidator
from src.api_client.input_validation.input_validator_interface import InputValidatorInterface
from src.api_client.input_validation.text_to_speech_input_validator import TextToSpeechInputValidator

COMMAND_INPUT_VALIDATORS: Dict[CommandId, InputValidatorInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechInputValidator(),
    CommandId.GET_MODELS: GetModelsInputValidator(),
    CommandId.GET_VOICES: GetVoicesInputValidator(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsInputValidator(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsInputValidator(),
    CommandId.GET_VOICE: GetVoiceInputValidator(),
    CommandId.DELETE_VOICE: DeleteVoiceInputValidator(),
    CommandId.EDIT_VOICE_SETTINGS: EditVoiceSettingsInputValidator(),
    CommandId.ADD_VOICE: AddVoiceInputValidator(),
    CommandId.EDIT_VOICE: EditVoiceInputValidator(),
    CommandId.DELETE_SAMPLE: DeleteSampleInputValidator(),
    CommandId.GET_AUDIO_FROM_SAMPLE: GetAudioFromSampleInputValidator(),
    CommandId.GET_GENERATED_ITEMS: GetGeneratedItemsInputValidator(),
    CommandId.GET_HISTORY_ITEM_BY_ID: GetHistoryItemInputValidator(),
    CommandId.DELETE_HISTORY_ITEM: DeleteHistoryItemInputValidator(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: GetAudioFromHistoryItemInputValidator(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: DownloadHistoryItemsInputValidator(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: GetUserSubscriptionInfoInputValidator(),
    CommandId.GET_USER_INFO: GetUserInfoInputValidator()
}
