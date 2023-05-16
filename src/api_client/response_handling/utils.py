from src.common.history_item.feedback import Feedback
from src.common.voice.voice_settings import VoiceSettings


def create_voice_settings(voice_settings_properties: dict) -> VoiceSettings:
    if not voice_settings_properties:
        return VoiceSettings(stability=0.75, similarity_boost=0.75)

    return VoiceSettings(stability=voice_settings_properties['stability'],
                         similarity_boost=voice_settings_properties['similarity_boost'])


def create_feedback(feedback_properties: dict) -> Feedback:
    return Feedback(thumbs_up=feedback_properties['thumbs_up'], feedback=feedback_properties['feedback'],
                    emotions=feedback_properties['emotions'],
                    inaccurate_clone=feedback_properties['inaccurate_clone'],
                    glitches=feedback_properties['glitches'], audio_quality=feedback_properties['audio_quality'],
                    other=feedback_properties['other'], review_status=feedback_properties['review_status'])
