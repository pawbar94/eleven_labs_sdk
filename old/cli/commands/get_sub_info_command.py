from old.cli.commands.base_command import BaseCommand
from thirdparty.comlint_py import ParsedCommand
from common.user_info_properties.user_subscription_info import UserSubscriptionInfo


class GetSubInfoCommand(BaseCommand):
    def run(self, command: ParsedCommand) -> None:
        subscription_info: UserSubscriptionInfo = self._api.get_user_subscription_info()

        print(subscription_info)
