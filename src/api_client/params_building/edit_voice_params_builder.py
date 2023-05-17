from src.api_client.params_building.params_builder_interface import ParamsBuilderInterface


class EditVoiceParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        params: dict = {}

        params['name'] = kwargs['new_name']
        params['files'] = kwargs['new_samples']
        params['description'] = kwargs['new_description']
        params['labels'] = kwargs['new_labels']

        return params
