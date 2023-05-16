from dataclasses import dataclass
from src.common.history_item.feedback import Feedback
from src.common.voice.voice_settings import VoiceSettings


@dataclass
class HistoryItem:
    id: str
    request_id: str
    voice_id: str
    voice_name: str
    text: str
    date: int
    character_count_change_from: int
    character_count_change_to: int
    content_type: str
    state: str
    settings: VoiceSettings
    feedback: Feedback
