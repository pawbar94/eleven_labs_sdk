from dataclasses import dataclass


@dataclass
class Feedback:
    thumbs_up: bool
    feedback: str
    emotions: bool
    inaccurate_clone: bool
    glitches: bool
    audio_quality: bool
    other: bool
    review_status: str
