from old.cli.commands.base_command import BaseCommand
from thirdparty.comlint_py import ParsedCommand
from common.user_info_properties.user_info import UserInfo


class GetUserInfoCommand(BaseCommand):
    def run(self, command: ParsedCommand) -> None:
        user_info: UserInfo = self._api.get_user_info()

        print(user_info)
