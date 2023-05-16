from dataclasses import dataclass
from typing import List
from src.common.model.language import Language


@dataclass
class Model:
    model_id: str
    name: str
    can_be_finetuned: bool
    can_do_text_to_speech: bool
    can_do_voice_conversion: bool
    token_cost_factor: int
    description: str
    languages: List[Language]
