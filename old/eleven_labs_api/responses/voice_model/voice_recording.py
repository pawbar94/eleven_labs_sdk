from dataclasses import dataclass


@dataclass
class VoiceRecording:
    id: str
    mime_type: str
    size: int
    date: int
    transcription: str
