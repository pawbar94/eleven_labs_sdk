from common.voice.voice_settings import VoiceSettings


def create_voice_settings(voice_settings_properties: dict) -> VoiceSettings:
    return VoiceSettings(stability=voice_settings_properties['stability'],
                         similarity_boost=voice_settings_properties['similarity_boost'])
