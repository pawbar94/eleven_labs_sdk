from thirdparty.comlint_py import CommandHandlerInterface, ParsedCommand


class GetHistoryCommand(CommandHandlerInterface):
    def run(self, command: ParsedCommand) -> None:
        print('Not implemented yet')