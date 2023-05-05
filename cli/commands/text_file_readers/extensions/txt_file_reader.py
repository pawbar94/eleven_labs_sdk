from cli.commands.text_file_readers.text_file_reader_interface import TextFileReaderInterface


class TxtFileReader(TextFileReaderInterface):
    def get_file_content(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()
