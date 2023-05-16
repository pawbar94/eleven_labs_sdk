import unittest
from unittest.mock import Mock
from src.common.enums.command_id import CommandId
from src.api_client.api_client import ApiClient
from src.api_client.input_validation.input_validator import InputValidator
from src.common.enums.latency_optimization import LatencyOptimization
from src.api_client.params_building.params_builder import ParamsBuilder
from src.api_client.request_handling.request_handler import RequestHandler
from src.api_client.response_handling.response_handler import ResponseHandler
from src.api_client.url_building.url_builder import UrlBuilder
from src.common.enums.model_id import ModelId
from src.common.voice.voice_settings import VoiceSettings


def create_mocks():
    return Mock(spec=InputValidator), Mock(spec=UrlBuilder), Mock(spec=ParamsBuilder), Mock(spec=RequestHandler), \
        Mock(spec=ResponseHandler)


def create_eleven_labs_api_client(input_validator: InputValidator, url_builder: UrlBuilder,
                                  params_builder: ParamsBuilder, request_handler: RequestHandler,
                                  response_handler: ResponseHandler):
    return ApiClient(input_validator, url_builder, params_builder, request_handler, response_handler)


class TestElevenLabsApiClient(unittest.TestCase):
    def test_text_to_speech(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        voice_id = 'some_voice_id'
        text = 'Some text to convert to speech'
        model_id = ModelId.MULTILINGUAL
        stability = 0.25
        similarity_boost = 0.75
        latency = LatencyOptimization.MAX_WITH_NO_TEXT_NORMALIZER

        client.text_to_speech(voice_id, text, stability, similarity_boost, model_id, latency)

        input_validator.validate.assert_called_with(CommandId.TEXT_TO_SPEECH, voice_id=voice_id, text=text,
                                                    model_id=model_id.value, stability=stability,
                                                    similarity_boost=similarity_boost, latency=latency.value)
        url_builder.build.assert_called_with(CommandId.TEXT_TO_SPEECH, voice_id=voice_id, text=text,
                                             model_id=model_id.value, stability=stability,
                                             similarity_boost=similarity_boost, latency=latency.value)
        params_builder.build.assert_called_with(CommandId.TEXT_TO_SPEECH, voice_id=voice_id, text=text,
                                                model_id=model_id.value, stability=stability,
                                                similarity_boost=similarity_boost, latency=latency.value)
        request_handler.send.assert_called_with(CommandId.TEXT_TO_SPEECH, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.TEXT_TO_SPEECH, request_handler.send.return_value)

    def test_get_models(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_models()

        input_validator.validate.assert_called_with(CommandId.GET_MODELS)
        url_builder.build.assert_called_with(CommandId.GET_MODELS)
        params_builder.build.assert_called_with(CommandId.GET_MODELS)
        request_handler.send.assert_called_with(CommandId.GET_MODELS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_MODELS, request_handler.send.return_value)

    def test_get_voices(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_voices()

        input_validator.validate.assert_called_with(CommandId.GET_VOICES)
        url_builder.build.assert_called_with(CommandId.GET_VOICES)
        params_builder.build.assert_called_with(CommandId.GET_VOICES)
        request_handler.send.assert_called_with(CommandId.GET_VOICES, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_VOICES, request_handler.send.return_value)

    def test_get_voice_settings_when_voice_id_not_provided(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_voice_settings()

        input_validator.validate.assert_called_with(CommandId.GET_DEFAULT_VOICE_SETTINGS, voice_id='')
        url_builder.build.assert_called_with(CommandId.GET_DEFAULT_VOICE_SETTINGS, voice_id='')
        params_builder.build.assert_called_with(CommandId.GET_DEFAULT_VOICE_SETTINGS, voice_id='')
        request_handler.send.assert_called_with(CommandId.GET_DEFAULT_VOICE_SETTINGS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_DEFAULT_VOICE_SETTINGS,
                                                    request_handler.send.return_value)

    def test_get_voice_settings_when_voice_id_provided(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        voice_id = 'some_voice_id'

        client.get_voice_settings(voice_id)

        input_validator.validate.assert_called_with(CommandId.GET_VOICE_SETTINGS, voice_id=voice_id)
        url_builder.build.assert_called_with(CommandId.GET_VOICE_SETTINGS, voice_id=voice_id)
        params_builder.build.assert_called_with(CommandId.GET_VOICE_SETTINGS, voice_id=voice_id)
        request_handler.send.assert_called_with(CommandId.GET_VOICE_SETTINGS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_VOICE_SETTINGS,
                                                    request_handler.send.return_value)

    def test_get_voice(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        voice_id = 'some_voice_id'

        client.get_voice(voice_id)

        input_validator.validate.assert_called_with(CommandId.GET_VOICE, voice_id=voice_id)
        url_builder.build.assert_called_with(CommandId.GET_VOICE, voice_id=voice_id)
        params_builder.build.assert_called_with(CommandId.GET_VOICE, voice_id=voice_id)
        request_handler.send.assert_called_with(CommandId.GET_VOICE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_VOICE, request_handler.send.return_value)

    def test_delete_voice(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        voice_id = 'some_voice_id'

        client.delete_voice(voice_id)

        input_validator.validate.assert_called_with(CommandId.DELETE_VOICE, voice_id=voice_id)
        url_builder.build.assert_called_with(CommandId.DELETE_VOICE, voice_id=voice_id)
        params_builder.build.assert_called_with(CommandId.DELETE_VOICE, voice_id=voice_id)
        request_handler.send.assert_called_with(CommandId.DELETE_VOICE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.DELETE_VOICE, request_handler.send.return_value)

    def test_edit_voice_settings(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        voice_id = 'some_voice_id'
        voice_settings = VoiceSettings(stability=0.39, similarity_boost=0.72)

        client.edit_voice_settings(voice_id, voice_settings)

        input_validator.validate.assert_called_with(CommandId.EDIT_VOICE_SETTINGS, voice_id=voice_id,
                                                    stability=voice_settings.stability,
                                                    similarity_boost=voice_settings.similarity_boost)
        url_builder.build.assert_called_with(CommandId.EDIT_VOICE_SETTINGS, voice_id=voice_id,
                                             stability=voice_settings.stability,
                                             similarity_boost=voice_settings.similarity_boost)
        params_builder.build.assert_called_with(CommandId.EDIT_VOICE_SETTINGS, voice_id=voice_id,
                                                stability=voice_settings.stability,
                                                similarity_boost=voice_settings.similarity_boost)
        request_handler.send.assert_called_with(CommandId.EDIT_VOICE_SETTINGS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.EDIT_VOICE_SETTINGS,
                                                    request_handler.send.return_value)

    def test_add_voice(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        voice_name = 'some_voice_name'
        samples = [b'\xAA\xBB\xCC\xDD', b'\x11\x22\x33\x44']
        description = 'My new voice'
        lables = {'key1': 'value1', 'key2': 'value2'}

        client.add_voice(voice_name, samples, description, lables)

        input_validator.validate.assert_called_with(CommandId.ADD_VOICE, name=voice_name, samples=samples,
                                                    description=description, labels=lables)
        url_builder.build.assert_called_with(CommandId.ADD_VOICE, name=voice_name, samples=samples,
                                             description=description, labels=lables)
        params_builder.build.assert_called_with(CommandId.ADD_VOICE, name=voice_name, samples=samples,
                                                description=description, labels=lables)
        request_handler.send.assert_called_with(CommandId.ADD_VOICE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.ADD_VOICE,
                                                    request_handler.send.return_value)

    def test_edit_voice(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        voice_id = 'some_voice_id'
        new_voice_name = 'some_voice_name'
        new_samples = [b'\xAA\xBB\xCC\xDD', b'\x11\x22\x33\x44']
        new_description = 'New description'
        new_lables = {'key1': 'value1', 'key2': 'value2'}

        client.edit_voice(voice_id, new_voice_name, new_samples, new_description, new_lables)

        input_validator.validate.assert_called_with(CommandId.EDIT_VOICE, voice_id=voice_id, name=new_voice_name,
                                                    samples=new_samples, description=new_description,
                                                    labels=new_lables)
        url_builder.build.assert_called_with(CommandId.EDIT_VOICE, voice_id=voice_id, name=new_voice_name,
                                             samples=new_samples, description=new_description,
                                             labels=new_lables)
        params_builder.build.assert_called_with(CommandId.EDIT_VOICE, voice_id=voice_id, name=new_voice_name,
                                                samples=new_samples, description=new_description, labels=new_lables)
        request_handler.send.assert_called_with(CommandId.EDIT_VOICE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.EDIT_VOICE,
                                                    request_handler.send.return_value)

    def test_delete_sample(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        voice_id = 'some_voice_id'
        sample_id = 'some_sample_id'

        client.delete_sample(voice_id, sample_id)

        input_validator.validate.assert_called_with(CommandId.DELETE_SAMPLE, voice_id=voice_id, sample_id=sample_id)
        url_builder.build.assert_called_with(CommandId.DELETE_SAMPLE, voice_id=voice_id, sample_id=sample_id)
        params_builder.build.assert_called_with(CommandId.DELETE_SAMPLE, voice_id=voice_id, sample_id=sample_id)
        request_handler.send.assert_called_with(CommandId.DELETE_SAMPLE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.DELETE_SAMPLE,
                                                    request_handler.send.return_value)

    def test_get_audio_from_sample(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        voice_id = 'some_voice_id'
        sample_id = 'some_sample_id'

        client.get_audio_from_sample(voice_id, sample_id)

        input_validator.validate.assert_called_with(CommandId.GET_AUDIO_FROM_SAMPLE, voice_id=voice_id,
                                                    sample_id=sample_id)
        url_builder.build.assert_called_with(CommandId.GET_AUDIO_FROM_SAMPLE, voice_id=voice_id, sample_id=sample_id)
        params_builder.build.assert_called_with(CommandId.GET_AUDIO_FROM_SAMPLE, voice_id=voice_id,
                                                sample_id=sample_id)
        request_handler.send.assert_called_with(CommandId.GET_AUDIO_FROM_SAMPLE, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_AUDIO_FROM_SAMPLE,
                                                    request_handler.send.return_value)

    def test_get_generated_items(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_generated_items()

        input_validator.validate.assert_called_with(CommandId.GET_GENERATED_ITEMS)
        url_builder.build.assert_called_with(CommandId.GET_GENERATED_ITEMS)
        params_builder.build.assert_called_with(CommandId.GET_GENERATED_ITEMS)
        request_handler.send.assert_called_with(CommandId.GET_GENERATED_ITEMS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_GENERATED_ITEMS,
                                                    request_handler.send.return_value)

    def test_get_history_item(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        history_item_id = 'some_history_item_id'

        client.get_history_item(history_item_id)

        input_validator.validate.assert_called_with(CommandId.GET_HISTORY_ITEM_BY_ID, history_item_id=history_item_id)
        url_builder.build.assert_called_with(CommandId.GET_HISTORY_ITEM_BY_ID, history_item_id=history_item_id)
        params_builder.build.assert_called_with(CommandId.GET_HISTORY_ITEM_BY_ID, history_item_id=history_item_id)
        request_handler.send.assert_called_with(CommandId.GET_HISTORY_ITEM_BY_ID, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_HISTORY_ITEM_BY_ID,
                                                    request_handler.send.return_value)

    def test_delete_history_item(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        history_item_id = 'some_history_item_id'

        client.delete_history_item(history_item_id)

        input_validator.validate.assert_called_with(CommandId.DELETE_HISTORY_ITEM, history_item_id=history_item_id)
        url_builder.build.assert_called_with(CommandId.DELETE_HISTORY_ITEM, history_item_id=history_item_id)
        params_builder.build.assert_called_with(CommandId.DELETE_HISTORY_ITEM, history_item_id=history_item_id)
        request_handler.send.assert_called_with(CommandId.DELETE_HISTORY_ITEM, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.DELETE_HISTORY_ITEM,
                                                    request_handler.send.return_value)

    def test_get_audio_from_history_item(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        history_item_id = 'some_history_item_id'

        client.get_audio_from_history_item(history_item_id)

        input_validator.validate.assert_called_with(CommandId.GET_AUDIO_FROM_HISTORY_ITEM,
                                                    history_item_id=history_item_id)
        url_builder.build.assert_called_with(CommandId.GET_AUDIO_FROM_HISTORY_ITEM, history_item_id=history_item_id)
        params_builder.build.assert_called_with(CommandId.GET_AUDIO_FROM_HISTORY_ITEM,
                                                history_item_id=history_item_id)
        request_handler.send.assert_called_with(CommandId.GET_AUDIO_FROM_HISTORY_ITEM, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_AUDIO_FROM_HISTORY_ITEM,
                                                    request_handler.send.return_value)

    def test_download_history_items(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)
        history_items_ids = ['some_history_item_id', 'some_other_history_item_id']

        client.download_history_items(history_items_ids)

        input_validator.validate.assert_called_with(CommandId.DOWNLOAD_HISTORY_ITEMS,
                                                    history_items_ids=history_items_ids)
        url_builder.build.assert_called_with(CommandId.DOWNLOAD_HISTORY_ITEMS, history_items_ids=history_items_ids)
        params_builder.build.assert_called_with(CommandId.DOWNLOAD_HISTORY_ITEMS,
                                                history_items_ids=history_items_ids)
        request_handler.send.assert_called_with(CommandId.DOWNLOAD_HISTORY_ITEMS, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.DOWNLOAD_HISTORY_ITEMS,
                                                    request_handler.send.return_value)

    def test_get_user_subscription_info(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_user_subscription_info()

        input_validator.validate.assert_called_with(CommandId.GET_USER_SUBSCRIPTION_INFO)
        url_builder.build.assert_called_with(CommandId.GET_USER_SUBSCRIPTION_INFO)
        params_builder.build.assert_called_with(CommandId.GET_USER_SUBSCRIPTION_INFO)
        request_handler.send.assert_called_with(CommandId.GET_USER_SUBSCRIPTION_INFO, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_USER_SUBSCRIPTION_INFO,
                                                    request_handler.send.return_value)

    def test_get_user_info(self):
        input_validator, url_builder, params_builder, request_handler, response_handler = create_mocks()
        client = create_eleven_labs_api_client(input_validator, url_builder, params_builder, request_handler,
                                               response_handler)

        client.get_user_info()

        input_validator.validate.assert_called_with(CommandId.GET_USER_INFO)
        url_builder.build.assert_called_with(CommandId.GET_USER_INFO)
        params_builder.build.assert_called_with(CommandId.GET_USER_INFO)
        request_handler.send.assert_called_with(CommandId.GET_USER_INFO, url_builder.build.return_value,
                                                params_builder.build.return_value)
        response_handler.process.assert_called_with(CommandId.GET_USER_INFO,
                                                    request_handler.send.return_value)
