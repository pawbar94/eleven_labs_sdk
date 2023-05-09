from typing import Dict
from old.cli.commands.text_file_readers.extensions.docx_file_reader import DocxFileReader
from old.cli.commands.text_file_readers.extensions.txt_file_reader import TxtFileReader
from old.cli.commands.text_file_readers.text_file_reader_interface import TextFileReaderInterface

SUPPORTED_READERS: Dict[str, TextFileReaderInterface] = {
    'txt': TxtFileReader(),
    'docx': DocxFileReader()
}


class TextFileReaderFactory:
    @staticmethod
    def create(file_extension: str) -> TextFileReaderInterface:
        if file_extension not in SUPPORTED_READERS:
            raise ValueError(f'Unsupported file extension for the given text file: {file_extension}! Currently the '
                             f'only supported extensions of text files are {list(SUPPORTED_READERS.keys())}.')

        return SUPPORTED_READERS[file_extension]
