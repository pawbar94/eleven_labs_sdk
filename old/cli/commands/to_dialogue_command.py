import json
import os
from typing import Dict, List
from old.cli.directories import ACTORS_FILE_PATH, SCRIPT_DIR
from old.cli.commands.base_command import BaseCommand
from old.cli.commands.text_file_readers.text_file_reader import TextFileReader
from old.cli.user_interface.interface_definition import INPUT_OPTION, OUTPUT_OPTION
from thirdparty.comlint_py import ParsedCommand
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi
from old.conversation_creator.conversation_creator import ConversationCreator
from old.conversation_creator.dialogue_decomposer import ActorName
from common.voice.voice import Voice


class ToDialogueCommand(BaseCommand):
    def __init__(self, api: ElevenLabsApi):
        super().__init__(api)

    def _execute(self, command: ParsedCommand) -> None:
        voices: Dict[ActorName, Voice] = self.__get_actor_to_voice_mapping()
        conversation_creator: ConversationCreator = ConversationCreator(self._api, voices)
        text: str = TextFileReader.read(file_path=command.options[INPUT_OPTION])

        conversation_creator.create(text, self.__get_output_dir(command))

    def __get_actor_to_voice_mapping(self) -> Dict[ActorName, Voice]:
        with open(ACTORS_FILE_PATH) as file:
            names_map: Dict[str, str] = json.load(file)

        all_voices: List[Voice] = self._api.get_voices()
        voice_map: Dict[ActorName, Voice] = {}

        for actor_name, voice_name in names_map.items():
            voice_map[actor_name] = self._find_voice(all_voices, voice_name)

        return voice_map

    def __get_output_dir(self, command: ParsedCommand) -> str:
        return os.path.join(SCRIPT_DIR, 'dialogue_project') \
                if not command.is_option_used(OUTPUT_OPTION) \
                else command.options[OUTPUT_OPTION]
