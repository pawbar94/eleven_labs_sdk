from typing import Dict
from api_client.command_id import CommandId
from api_client.params_building.params_builder_interface import ParamsBuilderInterface

COMMAND_PARAMS_BUILDERS: Dict[CommandId, ParamsBuilderInterface] = {
    CommandId.TEXT_TO_SPEECH: ParamsBuilderInterface(),
    CommandId.GET_MODELS: ParamsBuilderInterface(),
    CommandId.GET_VOICES: ParamsBuilderInterface(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: ParamsBuilderInterface(),
    CommandId.GET_VOICE_SETTINGS: ParamsBuilderInterface(),
    CommandId.GET_VOICE: ParamsBuilderInterface(),
    CommandId.DELETE_VOICE: ParamsBuilderInterface(),
    CommandId.EDIT_VOICE_SETTINGS: ParamsBuilderInterface(),
    CommandId.ADD_VOICE: ParamsBuilderInterface(),
    CommandId.EDIT_VOICE: ParamsBuilderInterface(),
    CommandId.DELETE_SAMPLE: ParamsBuilderInterface(),
    CommandId.GET_AUDIO_FROM_SAMPLE: ParamsBuilderInterface(),
    CommandId.GET_GENERATED_ITEMS: ParamsBuilderInterface(),
    CommandId.GET_HISTORY_ITEM_BY_ID: ParamsBuilderInterface(),
    CommandId.DELETE_HISTORY_ITEM: ParamsBuilderInterface(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: ParamsBuilderInterface(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: ParamsBuilderInterface(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: ParamsBuilderInterface(),
    CommandId.GET_USER_INFO: ParamsBuilderInterface()
}
