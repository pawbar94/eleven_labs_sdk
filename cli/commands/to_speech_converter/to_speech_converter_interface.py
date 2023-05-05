from abc import abstractmethod
from eleven_labs_api.eleven_labs_api import ElevenLabsApi
from eleven_labs_api.responses.voice_model.voice import Voice


class ToSpeechConverterInterface:
    @abstractmethod
    def download(self, api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        pass
