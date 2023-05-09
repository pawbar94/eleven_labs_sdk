from old.cli.commands.text_file_readers.text_file_reader_factory import TextFileReaderFactory
from old.cli.commands.text_file_readers.text_file_reader_interface import TextFileReaderInterface
from old.cli.utils import get_file_extension


class TextFileReader:
    @staticmethod
    def read(file_path: str) -> str:
        reader: TextFileReaderInterface = TextFileReaderFactory.create(file_extension=get_file_extension(file_path))

        return reader.get_file_content(file_path)
