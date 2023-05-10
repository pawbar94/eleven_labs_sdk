from typing import Dict
from api_client.command_id import CommandId
from api_client.input_validation.delete_voice_input_validator import DeleteVoiceInputValidator
from api_client.input_validation.get_default_voice_settings_input_validator import GetDefaultVoiceSettingsInputValidator
from api_client.input_validation.get_models_input_validator import GetModelsInputValidator
from api_client.input_validation.get_voice_input_validator import GetVoiceInputValidator
from api_client.input_validation.get_voice_settings_input_validator import GetVoiceSettingsInputValidator
from api_client.input_validation.get_voices_input_validator import GetVoicesInputValidator
from api_client.input_validation.input_validator_interface import InputValidatorInterface
from api_client.input_validation.text_to_speech_input_validator import TextToSpeechInputValidator

COMMAND_INPUT_VALIDATORS: Dict[CommandId, InputValidatorInterface] = {
    CommandId.TEXT_TO_SPEECH: TextToSpeechInputValidator(),
    CommandId.GET_MODELS: GetModelsInputValidator(),
    CommandId.GET_VOICES: GetVoicesInputValidator(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: GetDefaultVoiceSettingsInputValidator(),
    CommandId.GET_VOICE_SETTINGS: GetVoiceSettingsInputValidator(),
    CommandId.GET_VOICE: GetVoiceInputValidator(),
    CommandId.DELETE_VOICE: DeleteVoiceInputValidator(),
    CommandId.EDIT_VOICE_SETTINGS: InputValidatorInterface(),
    CommandId.ADD_VOICE: InputValidatorInterface(),
    CommandId.EDIT_VOICE: InputValidatorInterface(),
    CommandId.DELETE_SAMPLE: InputValidatorInterface(),
    CommandId.GET_AUDIO_FROM_SAMPLE: InputValidatorInterface(),
    CommandId.GET_GENERATED_ITEMS: InputValidatorInterface(),
    CommandId.GET_HISTORY_ITEM_BY_ID: InputValidatorInterface(),
    CommandId.DELETE_HISTORY_ITEM: InputValidatorInterface(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: InputValidatorInterface(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: InputValidatorInterface(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: InputValidatorInterface(),
    CommandId.GET_USER_INFO: InputValidatorInterface()
}