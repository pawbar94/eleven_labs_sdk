from dataclasses import dataclass
from typing import Dict, List
from eleven_labs_api.responses.voice_model.voice_fine_tuning import VoiceFineTuning
from eleven_labs_api.responses.voice_model.voice_sample import VoiceSample
from eleven_labs_api.responses.voice_model.voice_settings import VoiceSettings

VoiceID = str


@dataclass
class Voice:
    available_for_tiers: list
    category: str
    description: str
    fine_tuning: VoiceFineTuning
    labels: Dict[str, str]
    name: str
    preview_url: str
    samples: List[VoiceSample]
    settings: VoiceSettings
    id: VoiceID
