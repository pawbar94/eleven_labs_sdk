import logging
from abc import abstractmethod
from typing import List
from old.cli.user_interface.interface_definition import LOG_LEVEL_OPTION, DEFAULT_LOGGING_LEVEL
from thirdparty.comlint_py import CommandHandlerInterface, ParsedCommand
from common.voice_properties.voice import Voice
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi


class BaseCommand(CommandHandlerInterface):
    def __init__(self, api: ElevenLabsApi):
        super().__init__()

        self._api: ElevenLabsApi = api

    def run(self, command: ParsedCommand) -> None:
        self.__configure_logger(command)
        self._execute(command)

    @abstractmethod
    def _execute(self, command: ParsedCommand) -> None:
        pass

    def _get_voice(self, voice_name: str) -> Voice:
        voices: List[Voice] = self._api.get_voices()

        return self._find_voice(voices, voice_name)

    def _find_voice(self, voices: List[Voice], voice_name) -> Voice:
        filtered_voice: List[Voice] = list(filter(lambda voice: voice.name == voice_name, voices))

        if not filtered_voice:
            raise ValueError(f'Voice {voice_name} not found!')

        return filtered_voice[0]

    def __configure_logger(self, command: ParsedCommand) -> None:
        logging_level: str = DEFAULT_LOGGING_LEVEL if not command.is_option_used(LOG_LEVEL_OPTION) \
                                                   else command.options[LOG_LEVEL_OPTION]
        logging.basicConfig(level=logging.getLevelName(logging_level.upper()),
                            format='[%(levelname)s][%(name)s] %(message)s')
