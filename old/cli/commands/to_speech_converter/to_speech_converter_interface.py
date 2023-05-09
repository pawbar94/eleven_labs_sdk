from abc import abstractmethod
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi
from common.voice_properties.voice import Voice


class ToSpeechConverterInterface:
    @abstractmethod
    def download(self, api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        pass
