from api_client.params_building.params_builder_interface import ParamsBuilderInterface


class TextToSpeechParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        params: dict = {}

        params['text'] = kwargs['text']
        params['model_id'] = kwargs['model_id']
        params['voice_settings'] = {}
        params['voice_settings']['stability'] = kwargs['stability']
        params['voice_settings']['similarity_boost'] = kwargs['similarity_boost']

        return params
