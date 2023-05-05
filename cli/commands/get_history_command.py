from typing import List
from cli.commands.base_command import BaseCommand
from cli.user_interface.interface_definition import NAME_OPTION, TEXT_OPTION
from thirdparty.comlint_py import ParsedCommand
from eleven_labs_api.responses.history_item_model.history_item import HistoryItem


class GetHistoryCommand(BaseCommand):
    def _execute(self, command: ParsedCommand) -> None:
        history_items: List[HistoryItem] = self._api.get_generated_items()

        if command.is_option_used(NAME_OPTION) and command.is_option_used(TEXT_OPTION):
            history_items = list(filter(lambda item: item.voice_name == command.options[NAME_OPTION] and command.options[TEXT_OPTION].lower() in item.text.lower(), history_items))
        elif command.is_option_used(NAME_OPTION):
            history_items = list(filter(lambda item: item.voice_name == command.options[NAME_OPTION], history_items))
        elif command.is_option_used(TEXT_OPTION):
            history_items = list(filter(lambda item: command.options[TEXT_OPTION].lower() in item.text.lower(), history_items))

        for index, item in enumerate(history_items):
            print(f'[{index}] {item}')
