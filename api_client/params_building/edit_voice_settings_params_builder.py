from api_client.params_building.params_builder_interface import ParamsBuilderInterface


class EditVoiceSettingsParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        params: dict = {}

        params['stability'] = kwargs['stability']
        params['similarity_boost'] = kwargs['similarity_boost']

        return params
