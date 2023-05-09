import logging
from typing import List
from old.eleven_labs_api.eleven_labs_api import ElevenLabsApi
from common.voice_properties.voice import Voice

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s][%(name)s] %(message)s')
logger = logging.getLogger('SimpleTextConversion')


def find_voice_by_name(voices: List[Voice], name: str) -> Voice:
    for voice in voices:
        if voice.name == name:
            return voice


# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices = api.get_voices()
# Print all voices' properties
print('All voices:')
for voice in all_voices:
    print(f' * {voice}')
# Find the voice named 'Arnold'
arnold_voice = find_voice_by_name(all_voices, 'Arnold')
# optionally: tweak voice settings
arnold_voice.settings.stability = 0.3
arnold_voice.settings.similarity_boost = 0.95
# Convert text to audio file and save it to arnold_hello.mp3
api.text_to_speech_audio('Hello, this is Arnold speaking here', arnold_voice, 'arnold_hello.mp3')
