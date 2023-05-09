from dataclasses import dataclass
from typing import List
from common.voice_model.language import Language


@dataclass
class Model:
    id: str
    name: str
    supported_language: List[Language]
