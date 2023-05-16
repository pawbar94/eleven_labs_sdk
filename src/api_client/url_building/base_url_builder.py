from src.api_client.url_building.url_builder_interface import UrlBuilderInterface

ELEVEN_LABS_BASE_URL: str = 'https://api.elevenlabs.io'


class BaseUrlBuilder(UrlBuilderInterface):
    def __init__(self):
        super().__init__()

    def _get_full_url(self, sub_url: str) -> str:
        return ELEVEN_LABS_BASE_URL + sub_url
