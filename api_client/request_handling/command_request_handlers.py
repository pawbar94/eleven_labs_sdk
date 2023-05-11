from typing import Dict
from api_client.command_id import CommandId
from api_client.request_handling.request_handler_interface import RequestHandlerInterface

COMMAND_REQUEST_HANDLERS: Dict[CommandId, RequestHandlerInterface] = {
    CommandId.TEXT_TO_SPEECH: RequestHandlerInterface(),
    CommandId.GET_MODELS: RequestHandlerInterface(),
    CommandId.GET_VOICES: RequestHandlerInterface(),
    CommandId.GET_DEFAULT_VOICE_SETTINGS: RequestHandlerInterface(),
    CommandId.GET_VOICE_SETTINGS: RequestHandlerInterface(),
    CommandId.GET_VOICE: RequestHandlerInterface(),
    CommandId.DELETE_VOICE: RequestHandlerInterface(),
    CommandId.EDIT_VOICE_SETTINGS: RequestHandlerInterface(),
    CommandId.ADD_VOICE: RequestHandlerInterface(),
    CommandId.EDIT_VOICE: RequestHandlerInterface(),
    CommandId.DELETE_SAMPLE: RequestHandlerInterface(),
    CommandId.GET_AUDIO_FROM_SAMPLE: RequestHandlerInterface(),
    CommandId.GET_GENERATED_ITEMS: RequestHandlerInterface(),
    CommandId.GET_HISTORY_ITEM_BY_ID: RequestHandlerInterface(),
    CommandId.DELETE_HISTORY_ITEM: RequestHandlerInterface(),
    CommandId.GET_AUDIO_FROM_HISTORY_ITEM: RequestHandlerInterface(),
    CommandId.DOWNLOAD_HISTORY_ITEMS: RequestHandlerInterface(),
    CommandId.GET_USER_SUBSCRIPTION_INFO: RequestHandlerInterface(),
    CommandId.GET_USER_INFO: RequestHandlerInterface()
}
