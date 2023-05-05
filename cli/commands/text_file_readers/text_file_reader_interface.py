from abc import abstractmethod


class TextFileReaderInterface:
    @abstractmethod
    def get_file_content(self, file_path: str) -> str:
        pass
