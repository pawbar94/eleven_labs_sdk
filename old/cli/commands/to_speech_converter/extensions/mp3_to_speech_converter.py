import os.path
from old.cli.commands.to_speech_converter.to_speech_converter_interface import ToSpeechConverterInterface
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi
from common.voice.voice import Voice
from logging import getLogger

logger = getLogger('Mp3ToSpeechConverter')


class Mp3ToSpeechConverter(ToSpeechConverterInterface):
    def download(self, api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        audio_stream: bytes = api.text_to_speech_stream(text, voice)

        with open(output_path, 'wb') as file:
            file.write(audio_stream)

        logger.info(f'Saved audio to {os.path.abspath(output_path)} file')
