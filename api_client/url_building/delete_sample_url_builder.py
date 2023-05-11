from api_client.url_building.base_url_builder import BaseUrlBuilder


class DeleteSampleUrlBuilder(BaseUrlBuilder):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs) -> str:
        return self._get_full_url(f'/v1/voices/{kwargs["voice_id"]}/samples/{kwargs["sample_id"]}')
