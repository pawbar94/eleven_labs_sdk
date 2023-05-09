import docx2txt
from old.cli.commands.text_file_readers.text_file_reader_interface import TextFileReaderInterface


class DocxFileReader(TextFileReaderInterface):
    def get_file_content(self, file_path: str) -> str:
        return docx2txt.process(file_path)
