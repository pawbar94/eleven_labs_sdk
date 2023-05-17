from src.api_client.params_building.params_builder_interface import ParamsBuilderInterface


class GetModelsParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        return {}
