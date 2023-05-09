import unittest

from old.eleven_labs_api.requests.exceptions.empty_text import EmptyText
from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from old.eleven_labs_api.requests.exceptions.invalid_stability_value import InvalidStabilityValue
from old.eleven_labs_api.requests.text_to_speech_audio_request import TextToSpeechAudioRequest


class TestTextToSpeechAudioRequest(unittest.TestCase):
    def test_text_to_speech_audio_request_constructs_properly(self):
        voice_id = 'test_voice_id'
        text = 'test_text'
        stability = 0.5
        similarity_boost = 0.7

        expected_uri = f'/v1/text-to-speech/{voice_id}'
        expected_payload = {
            "text": text,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost
            }
        }

        request = TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_text_to_speech_audio_request_raises_exception_when_voice_id_is_empty(self):
        voice_id = ''
        text = 'test_text'
        stability = 0.5
        similarity_boost = 0.7

        with self.assertRaises(EmptyVoiceId):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

    def test_text_to_speech_audio_request_raises_exception_when_text_is_empty(self):
        voice_id = 'test_voice_id'
        text = ''
        stability = 0.5
        similarity_boost = 0.7

        with self.assertRaises(EmptyText):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

    def test_text_to_speech_audio_request_raises_exception_when_stability_is_less_than_zero(self):
        voice_id = 'test_voice_id'
        text = 'test_text'
        stability = -0.1
        similarity_boost = 0.7

        with self.assertRaises(InvalidStabilityValue):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

    def test_text_to_speech_audio_request_raises_exception_when_stability_is_greater_than_one(self):
        voice_id = 'test_voice_id'
        text = 'test_text'
        stability = 1.1
        similarity_boost = 0.7

        with self.assertRaises(InvalidStabilityValue):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

    def test_text_to_speech_audio_request_raises_exception_when_similarity_boost_is_less_than_zero(self):
        voice_id = 'test_voice_id'
        text = 'test_text'
        stability = 0.5
        similarity_boost = -0.1

        with self.assertRaises(InvalidSimilarityBoostValue):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)

    def test_text_to_speech_audio_request_raises_exception_when_similarity_boost_is_greater_than_one(self):
        voice_id = 'test_voice_id'
        text = 'test_text'
        stability = 0.5
        similarity_boost = 1.1

        with self.assertRaises(InvalidSimilarityBoostValue):
            TextToSpeechAudioRequest(voice_id, text, stability, similarity_boost)
