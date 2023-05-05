from cli.commands.to_speech_converter.to_speech_converter_factory import ToSpeechConverterFactory
from cli.commands.to_speech_converter.to_speech_converter_interface import ToSpeechConverterInterface
from cli.utils import get_file_extension
from eleven_labs_api.eleven_labs_api import ElevenLabsApi
from eleven_labs_api.responses.voice_model.voice import Voice


class ToSpeechConverter:
    @staticmethod
    def download(api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        downloader: ToSpeechConverterInterface = ToSpeechConverterFactory.create(file_extension=get_file_extension(output_path))

        return downloader.download(api, text, voice, output_path)
