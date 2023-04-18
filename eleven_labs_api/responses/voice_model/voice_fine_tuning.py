from dataclasses import dataclass
from typing import List
from eleven_labs_api.responses.voice_model.fine_tuning_verification_attempt import FineTuningVerificationAttempt


@dataclass
class VoiceFineTuning:
    model_id: str
    is_allowed_to_fine_tune: bool
    fine_tuning_requested: bool
    fine_tuning_state: str
    verification_attempts: List[FineTuningVerificationAttempt]
    verification_failures: List[str]
    verification_attempts_count: int
    slice_ids: List[str]
