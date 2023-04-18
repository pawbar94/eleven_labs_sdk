from dataclasses import dataclass, field


@dataclass
class VoiceSettings:
    stability: float = field(default=0.75)
    similarity_boost: float = field(default=0.75)
