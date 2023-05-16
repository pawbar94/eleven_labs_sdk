from src.api_client.url_building.base_url_builder import BaseUrlBuilder


class GetHistoryItemUrlBuilder(BaseUrlBuilder):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs) -> str:
        return self._get_full_url(f'/v1/history/{kwargs["history_item_id"]}')
