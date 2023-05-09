import os

from old.cli.commands.text_file_readers.text_file_reader import TextFileReader
from old.cli.commands.base_command import BaseCommand
from old.cli.commands.to_speech_converter.to_speech_converter import ToSpeechConverter
from old.cli.directories import SCRIPT_DIR
from old.cli.user_interface.interface_definition import INPUT_OPTION, NAME_OPTION, OUTPUT_OPTION
from thirdparty.comlint_py import ParsedCommand
from common.voice_properties.voice import Voice
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi

DEFAULT_OUTPUT_FILE_PATH: str = os.path.join(SCRIPT_DIR, )


class ToSpeechCommand(BaseCommand):
    def __init__(self, api: ElevenLabsApi):
        super().__init__(api)

    def _execute(self, command: ParsedCommand) -> None:
        text: str = TextFileReader.read(file_path=command.options[INPUT_OPTION])
        voice: Voice = self._get_voice(voice_name=command.options[NAME_OPTION])
        output_path: str = self.__get_output_path(command, voice.name)

        ToSpeechConverter.download(self._api, text, voice, output_path)

    def __get_output_path(self, command: ParsedCommand, voice_name: str) -> str:
        return os.path.join(SCRIPT_DIR, f'converted_{voice_name.lower()}.mp3') \
                if not command.is_option_used(OUTPUT_OPTION) \
                else command.options[OUTPUT_OPTION]
