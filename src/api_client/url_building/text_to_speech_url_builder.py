from src.api_client.url_building.base_url_builder import BaseUrlBuilder


class TextToSpeechUrlBuilder(BaseUrlBuilder):
    def __init__(self):
        super().__init__()

    def build(self, **kwargs) -> str:
        return self._get_full_url(f'/v1/text-to-speech/{kwargs["voice_id"]}/stream')
