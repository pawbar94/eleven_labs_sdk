from dataclasses import dataclass
from typing import Dict, List
from common.voice.voice_fine_tuning import VoiceFineTuning
from common.voice.voice_sample import VoiceSample
from common.voice.voice_settings import VoiceSettings

VoiceID = str


@dataclass
class Voice:
    id: VoiceID
    name: str
    samples: List[VoiceSample]
    category: str
    fine_tuning: VoiceFineTuning
    labels: Dict[str, str]
    description: str
    preview_url: str
    available_for_tiers: list
    settings: VoiceSettings
