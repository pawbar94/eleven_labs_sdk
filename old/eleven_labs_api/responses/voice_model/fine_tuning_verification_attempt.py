from dataclasses import dataclass
from old.eleven_labs_api.responses.voice_model.voice_recording import VoiceRecording


@dataclass
class FineTuningVerificationAttempt:
    text: str
    date: int
    accepted: bool
    similarity: int
    levenshtein_distance: int
    recording: VoiceRecording
