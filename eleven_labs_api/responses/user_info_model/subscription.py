from dataclasses import dataclass
from typing import List

from eleven_labs_api.responses.user_info_model.model import Model


@dataclass
class Subscription:
    tier: str
    character_count: int
    character_limit: int
    can_extend_character_limit: bool
    allowed_to_extend_character_limit: bool
    next_character_count_reset_unix: int
    voice_limit: int
    professional_voice_limit: int
    can_extend_voice_limit: bool
    can_use_instant_voice_cloning: bool
    can_use_professional_voice_cloning: bool
    available_models: List[Model]
    can_use_delayed_payment_methods: bool
    currency: str
    status: str
