import os.path
from old.cli.commands.to_speech_converter.to_speech_converter_interface import ToSpeechConverterInterface
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi
from common.voice_properties.voice import Voice
from logging import getLogger

logger = getLogger('MpegToSpeechConverter')


class MpegToSpeechConverter(ToSpeechConverterInterface):
    def download(self, api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        api.text_to_speech_audio(text, voice, output_path)

        logger.info(f'Saved audio to {os.path.abspath(output_path)} file')
