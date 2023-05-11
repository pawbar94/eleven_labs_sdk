from api_client.params_building.params_builder_interface import ParamsBuilderInterface


class EditVoiceParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        params: dict = {}

        params['name'] = kwargs['name']
        params['files'] = kwargs['files']
        params['description'] = kwargs['description']
        params['labels'] = kwargs['labels']

        return params
