from dataclasses import dataclass


@dataclass
class VoiceSample:
    id: str
    file_name: str
    mime_type: str
    size: int
    hash: str
