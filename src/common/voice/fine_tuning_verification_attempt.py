from dataclasses import dataclass
from src.common.voice.voice_recording import VoiceRecording


@dataclass
class FineTuningVerificationAttempt:
    text: str
    date: int
    accepted: bool
    similarity: int
    levenshtein_distance: int
    recording: VoiceRecording
