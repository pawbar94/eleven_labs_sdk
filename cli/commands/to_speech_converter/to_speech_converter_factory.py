from typing import Dict
from cli.commands.to_speech_converter.extensions.mp3_to_speech_converter import Mp3ToSpeechConverter
from cli.commands.to_speech_converter.extensions.mpeg_to_speech_converter import MpegToSpeechConverter
from cli.commands.to_speech_converter.to_speech_converter_interface import ToSpeechConverterInterface

SUPPORTED_CONVERTERS: Dict[str, ToSpeechConverterInterface] = {
    'mp3': Mp3ToSpeechConverter(),
    'mpeg': MpegToSpeechConverter()
}


class ToSpeechConverterFactory:
    @staticmethod
    def create(file_extension: str) -> ToSpeechConverterInterface:
        if file_extension not in SUPPORTED_CONVERTERS:
            raise ValueError(f'Unsupported file extension for audio file: {file_extension}! Currently the only '
                             f'supported extensions of audio files are {list(SUPPORTED_CONVERTERS.keys())}.')

        return SUPPORTED_CONVERTERS[file_extension]
