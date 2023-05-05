import os.path
from cli.commands.to_speech_converter.to_speech_converter_interface import ToSpeechConverterInterface
from eleven_labs_api.eleven_labs_api import ElevenLabsApi
from eleven_labs_api.responses.voice_model.voice import Voice
from logging import getLogger

logger = getLogger('MpegToSpeechConverter')


class MpegToSpeechConverter(ToSpeechConverterInterface):
    def download(self, api: ElevenLabsApi, text: str, voice: Voice, output_path: str) -> None:
        api.text_to_speech_audio(text, voice, output_path)

        logger.info(f'Saved audio to {os.path.abspath(output_path)} file')
