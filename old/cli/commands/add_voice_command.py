from thirdparty.comlint_py import CommandHandlerInterface, ParsedCommand


class AddVoiceCommand(CommandHandlerInterface):
    def run(self, command: ParsedCommand) -> None:
        print('Not implemented yet')
