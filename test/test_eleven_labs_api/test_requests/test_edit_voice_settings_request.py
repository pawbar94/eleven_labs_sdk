import unittest
from eleven_labs_api.requests.edit_voice_settings_request import EditVoiceSettingsRequest
from eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from eleven_labs_api.requests.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from eleven_labs_api.requests.exceptions.invalid_stability_value import InvalidStabilityValue


class TestEditVoiceSettingsRequest(unittest.TestCase):
    def test_edit_voice_settings_constructs_properly(self):
        voice_id = 'test-voice-id'
        stability = 0.5
        similarity_boost = 0.2

        expected_uri = f'/v1/voices/{voice_id}/settings/edit'
        expected_payload = {
            "stability": stability,
            "similarity_boost": similarity_boost
        }

        request = EditVoiceSettingsRequest(voice_id, stability, similarity_boost)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_edit_voice_settings_raises_exception_when_voice_id_is_empty(self):
        voice_id = ''
        stability = 0.5
        similarity_boost = 0.2

        with self.assertRaises(EmptyVoiceId):
            EditVoiceSettingsRequest(voice_id, stability, similarity_boost)

    def test_edit_voice_settings_raises_exception_when_stability_is_too_low(self):
        voice_id = 'test-voice-id'
        stability = -0.1
        similarity_boost = 0.2

        with self.assertRaises(InvalidStabilityValue):
            EditVoiceSettingsRequest(voice_id, stability, similarity_boost)

    def test_edit_voice_settings_raises_exception_when_stability_is_too_high(self):
        voice_id = 'test-voice-id'
        stability = 1.1
        similarity_boost = 0.2

        with self.assertRaises(InvalidStabilityValue):
            EditVoiceSettingsRequest(voice_id, stability, similarity_boost)

    def test_edit_voice_settings_raises_exception_when_similarity_boost_is_too_low(self):
        voice_id = 'test-voice-id'
        stability = 0.5
        similarity_boost = -0.1

        with self.assertRaises(InvalidSimilarityBoostValue):
            EditVoiceSettingsRequest(voice_id, stability, similarity_boost)

    def test_edit_voice_settings_raises_exception_when_similarity_boost_is_too_high(self):
        voice_id = 'test-voice-id'
        stability = 0.5
        similarity_boost = 1.1

        with self.assertRaises(InvalidSimilarityBoostValue):
            EditVoiceSettingsRequest(voice_id, stability, similarity_boost)
