from dataclasses import dataclass
from typing import List
from eleven_labs_api.responses.user_info_model.language import Language


@dataclass
class Model:
    id: str
    name: str
    supported_language: List[Language]
