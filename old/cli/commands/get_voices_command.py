from typing import List
from old.cli.commands.base_command import BaseCommand
from old.cli.user_interface.interface_definition import NAME_OPTION, PREMADE_FLAG, GENERATED_FLAG
from thirdparty.comlint_py import ParsedCommand
from common.voice_properties.voice import Voice


class GetVoicesCommand(BaseCommand):
    def _execute(self, command: ParsedCommand) -> None:
        voices: List[Voice] = self._api.get_voices()

        if command.is_option_used(NAME_OPTION):
            voices = [self._find_voice(voices, command.options[NAME_OPTION])]
        elif command.flags[PREMADE_FLAG]:
            voices = list(filter(lambda voice: voice.category == 'premade', voices))
        elif command.flags[GENERATED_FLAG]:
            voices = list(filter(lambda voice: voice.category == 'generated', voices))

        for index, voice in enumerate(voices):
            print(f'[{index}] {voice}')
