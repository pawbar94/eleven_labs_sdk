from src.api_client.params_building.params_builder_interface import ParamsBuilderInterface


class DownloadHistoryItemsParamsBuilder(ParamsBuilderInterface):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs):
        params: dict = {}

        params['history_items_ids'] = kwargs['history_items_ids']

        return params
