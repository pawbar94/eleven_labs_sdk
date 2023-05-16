from dataclasses import dataclass


@dataclass
class VoiceRecording:
    id: str
    mime_type: str
    size: int
    upload_date: int
    transcription: str
