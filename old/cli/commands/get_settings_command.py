from thirdparty.comlint_py import CommandHandlerInterface, ParsedCommand


class GetSettingsCommand(CommandHandlerInterface):
    def run(self, command: ParsedCommand) -> None:
        print('Not implemented yet')
