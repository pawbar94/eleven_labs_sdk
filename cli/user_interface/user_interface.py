from typing import List

from cli.commands.add_voice_command import AddVoiceCommand
from cli.commands.delete_history_command import DeleteHistoryCommand
from cli.commands.delete_sample_command import DeleteSampleCommand
from cli.commands.delete_voice_command import DeleteVoiceCommand
from cli.commands.download_history_command import DownloadHistoryCommand
from cli.commands.download_sample_command import DownloadSampleCommand
from cli.commands.edit_settings_command import EditSettingsCommand
from cli.commands.edit_voice_command import EditVoiceCommand
from cli.commands.get_history_command import GetHistoryCommand
from cli.commands.get_settings_command import GetSettingsCommand
from cli.commands.get_sub_info_command import GetSubInfoCommand
from cli.commands.get_user_info_command import GetUserInfoCommand
from cli.commands.get_voices_command import GetVoicesCommand
from cli.commands.to_dialogue_command import ToDialogueCommand
from cli.commands.to_speech_command import ToSpeechCommand
from cli.user_interface.interface_definition import TO_SPEECH_COMMAND, INPUT_OPTION, NAME_OPTION, OUTPUT_OPTION, \
    LOG_LEVEL_OPTION, TO_DIALOGUE_COMMAND, CONFIG_OPTION, GET_VOICES_COMMAND, GET_HISTORY_COMMAND, \
    GET_USER_INFO_COMMAND, GET_SUB_INFO_COMMAND, GET_SETTINGS_COMMAND, DELETE_VOICE_COMMAND, DELETE_SAMPLE_COMMAND, \
    ID_OPTION, DELETE_HISTORY_COMMAND, EDIT_SETTINGS_COMMAND, STABILITY_OPTION, SIMILARITY_BOOST_OPTION, \
    EDIT_VOICE_COMMAND, FILES_OPTION, DESCRIPTION_OPTION, LABELS_OPTION, ADD_VOICE_COMMAND, DOWNLOAD_SAMPLE_COMMAND, \
    DOWNLOAD_HISTORY_COMMAND, DEFAULT_FLAG
from thirdparty.comlint_py import CommandLineInterface
from eleven_labs_api.eleven_labs_api import ElevenLabsApi


class UserInterface:
    def __init__(self, argv: List[str], api: ElevenLabsApi):
        self.__cli: CommandLineInterface = CommandLineInterface(argv=argv, program_name='Command line interface for '
                                                                                        'Eleven Labs API',
                                                                allow_no_arguments=False)
        self.__api: ElevenLabsApi = api

    def init(self) -> None:
        self.__define_text_converting_commands()
        self.__define_get_commands()
        self.__define_delete_commands()
        self.__define_edit_commands()
        self.__define_add_commands()
        self.__define_download_commands()

        self.__define_options()
        self.__define_flags()

        self.__register_command_handlers(self.__api)

    def run(self) -> None:
        self.__cli.run()

    def __define_text_converting_commands(self) -> None:
        self.__cli.add_command(command_name=TO_SPEECH_COMMAND,
                               description='Converts text from the given file to speech with the given voice.',
                               allowed_options=[INPUT_OPTION, NAME_OPTION, OUTPUT_OPTION, LOG_LEVEL_OPTION],
                               required_options=[INPUT_OPTION, NAME_OPTION])
        self.__cli.add_command(command_name=TO_DIALOGUE_COMMAND,
                               description='Converts text from the given file to a dialogue between two or more people '
                                           'basing on voice mapping provided in JSON configuration file.',
                               allowed_options=[INPUT_OPTION, CONFIG_OPTION, OUTPUT_OPTION, LOG_LEVEL_OPTION],
                               required_options=[INPUT_OPTION, CONFIG_OPTION])

    def __define_get_commands(self) -> None:
        self.__cli.add_command(command_name=GET_VOICES_COMMAND,
                               description=f'Displays properties of all voices available on the account. If '
                                           f'{NAME_OPTION} option is used, the output will be filtered only for the '
                                           f'given voice.',
                               allowed_options=[NAME_OPTION, LOG_LEVEL_OPTION])
        self.__cli.add_command(command_name=GET_HISTORY_COMMAND,
                               description=f'Displays properties of all generated items. If {NAME_OPTION} option is '
                                           f'used, the output will be filtered only for the given voice.',
                               allowed_options=[NAME_OPTION, LOG_LEVEL_OPTION])
        self.__cli.add_command(command_name=GET_USER_INFO_COMMAND,
                               description='Displays properties of the user account.',
                               allowed_options=[LOG_LEVEL_OPTION])
        self.__cli.add_command(command_name=GET_SUB_INFO_COMMAND,
                               description='Displays properties of the user subscription plan.',
                               allowed_options=[LOG_LEVEL_OPTION])
        self.__cli.add_command(command_name=GET_SETTINGS_COMMAND,
                               description='Displays settings of the voice with the given name.',
                               allowed_options=[NAME_OPTION, LOG_LEVEL_OPTION],
                               allowed_flags=[DEFAULT_FLAG],
                               required_options=[NAME_OPTION])

    def __define_delete_commands(self) -> None:
        self.__cli.add_command(command_name=DELETE_VOICE_COMMAND,
                               description='Deletes the voice with the given name.',
                               allowed_options=[NAME_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION])
        self.__cli.add_command(command_name=DELETE_SAMPLE_COMMAND,
                               description='Deletes the sample with the given id for the voice with the given name.',
                               allowed_options=[NAME_OPTION, ID_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION, ID_OPTION])
        self.__cli.add_command(command_name=DELETE_HISTORY_COMMAND,
                               description=f'Deletes the history item with the given id.',
                               allowed_options=[ID_OPTION, LOG_LEVEL_OPTION])

    def __define_edit_commands(self) -> None:
        self.__cli.add_command(command_name=EDIT_SETTINGS_COMMAND,
                               description='Edits settings of the voice with the given name.',
                               allowed_options=[NAME_OPTION, STABILITY_OPTION, SIMILARITY_BOOST_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION, STABILITY_OPTION, SIMILARITY_BOOST_OPTION])
        self.__cli.add_command(command_name=EDIT_VOICE_COMMAND,
                               description='Edits properties of the voice with the given name.',
                               allowed_options=[NAME_OPTION, FILES_OPTION, DESCRIPTION_OPTION, LABELS_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION])

    def __define_add_commands(self) -> None:
        self.__cli.add_command(command_name=ADD_VOICE_COMMAND,
                               description='Adds a new voice with the given name.',
                               allowed_options=[NAME_OPTION, FILES_OPTION, DESCRIPTION_OPTION, LABELS_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION, FILES_OPTION])

    def __define_download_commands(self) -> None:
        self.__cli.add_command(command_name=DOWNLOAD_SAMPLE_COMMAND,
                               description='Downloads the sample with the given id for the voice with the given name.',
                               allowed_options=[NAME_OPTION, ID_OPTION, OUTPUT_OPTION, LOG_LEVEL_OPTION],
                               required_options=[NAME_OPTION, ID_OPTION, OUTPUT_OPTION])
        self.__cli.add_command(command_name=DOWNLOAD_HISTORY_COMMAND,
                               description=f'Downloads the audio from the history item with the given id.',
                               allowed_options=[ID_OPTION, OUTPUT_OPTION, LOG_LEVEL_OPTION])

    def __define_options(self) -> None:
        self.__cli.add_option(option_name=INPUT_OPTION,
                              description='Path to file with text to convert to speech.')
        self.__cli.add_option(option_name=NAME_OPTION,
                              description='Name of the voice.')
        self.__cli.add_option(option_name=OUTPUT_OPTION,
                              description='Path to file to save converted text to speech.')
        self.__cli.add_option(option_name=CONFIG_OPTION,
                              description='Path to JSON configuration file with voice mapping between actor\'s name '
                                          'and the corresponding voice name.')
        self.__cli.add_option(option_name=ID_OPTION,
                              description='ID of an item to act on (e.g. sample ID, history item ID etc.).')
        self.__cli.add_option(option_name=STABILITY_OPTION,
                              description='Stability of the voice. It must be a number between 0 and 1.')
        self.__cli.add_option(option_name=SIMILARITY_BOOST_OPTION,
                              description='Similarity boost of the voice. It must be a number between 0 and 1.')
        self.__cli.add_option(option_name=FILES_OPTION,
                              description='List of paths to files with samples to upload. Remember to use quotes when '
                                          'providing a list of multiple files.')
        self.__cli.add_option(option_name=DESCRIPTION_OPTION,
                              description='Description of the voice. Remember to use quotes when providing a '
                                          'multi-word description.')
        self.__cli.add_option(option_name=LABELS_OPTION,
                              description='Serialized string with labels for the new voice. Remember to use quotes.')
        self.__cli.add_option(option_name=LOG_LEVEL_OPTION,
                              description='Specifies logging level of the application.',
                              allowed_values=['debug', 'info', 'warning', 'error'])

    def __define_flags(self) -> None:
        self.__cli.add_flag(flag_name=DEFAULT_FLAG,
                            description='If used, a default voice settings will be downloaded.')

    def __register_command_handlers(self, api: ElevenLabsApi) -> None:
        self.__cli.add_command_handler(command_name=TO_SPEECH_COMMAND, command_handler=ToSpeechCommand())
        self.__cli.add_command_handler(command_name=TO_DIALOGUE_COMMAND, command_handler=ToDialogueCommand())

        self.__cli.add_command_handler(command_name=GET_VOICES_COMMAND, command_handler=GetVoicesCommand())
        self.__cli.add_command_handler(command_name=GET_HISTORY_COMMAND, command_handler=GetHistoryCommand())
        self.__cli.add_command_handler(command_name=GET_USER_INFO_COMMAND, command_handler=GetUserInfoCommand())
        self.__cli.add_command_handler(command_name=GET_SUB_INFO_COMMAND, command_handler=GetSubInfoCommand())
        self.__cli.add_command_handler(command_name=GET_SETTINGS_COMMAND, command_handler=GetSettingsCommand())

        self.__cli.add_command_handler(command_name=DELETE_VOICE_COMMAND, command_handler=DeleteVoiceCommand())
        self.__cli.add_command_handler(command_name=DELETE_SAMPLE_COMMAND, command_handler=DeleteSampleCommand())
        self.__cli.add_command_handler(command_name=DELETE_HISTORY_COMMAND, command_handler=DeleteHistoryCommand())

        self.__cli.add_command_handler(command_name=EDIT_SETTINGS_COMMAND, command_handler=EditSettingsCommand())
        self.__cli.add_command_handler(command_name=EDIT_VOICE_COMMAND, command_handler=EditVoiceCommand())

        self.__cli.add_command_handler(command_name=ADD_VOICE_COMMAND, command_handler=AddVoiceCommand())

        self.__cli.add_command_handler(command_name=DOWNLOAD_SAMPLE_COMMAND, command_handler=DownloadSampleCommand())
        self.__cli.add_command_handler(command_name=DOWNLOAD_HISTORY_COMMAND, command_handler=DownloadHistoryCommand())
