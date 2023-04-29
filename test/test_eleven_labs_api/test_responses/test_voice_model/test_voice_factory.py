import unittest
from eleven_labs_api.responses.voice_model.voice_factory import VoiceFactory


class TestVoiceFactory(unittest.TestCase):
    def test_create(self):
        voice_properties: dict = {
            "voice_id": "test_voice_id",
            "name": "test_name",
            "samples": [
                {
                    "sample_id": "test_sample_id_1",
                    "file_name": "test_file_name_1",
                    "mime_type": "test_mime_type_1",
                    "size_bytes": 123,
                    "hash": "test_hash_1",
                },
                {
                    "sample_id": "test_sample_id_2",
                    "file_name": "test_file_name_2",
                    "mime_type": "test_mime_type_2",
                    "size_bytes": 456,
                    "hash": "test_hash_2",
                }
            ],
            "category": "test_category",
            "fine_tuning": {
                "model_id": "test_model_id",
                "is_allowed_to_fine_tune": True,
                "fine_tuning_requested": True,
                "finetuning_state": "not_started",
                "verification_attempts": [
                    {
                        "text": "test_text_1",
                        "date_unix": 12345,
                        "accepted": True,
                        "similarity": 0.1,
                        "levenshtein_distance": 2,
                        "recording": {
                            "recording_id": "test_recording_id_1",
                            "mime_type": "test_mime_type_1",
                            "size_bytes": 876,
                            "upload_date_unix": 34212,
                            "transcription": "test_transcription_1"
                        }
                    },
                    {
                        "text": "test_text_2",
                        "date_unix": 567789,
                        "accepted": False,
                        "similarity": 0.6,
                        "levenshtein_distance": 3,
                        "recording": {
                            "recording_id": "test_recording_id_2",
                            "mime_type": "test_mime_type_2",
                            "size_bytes": 543,
                            "upload_date_unix": 848775,
                            "transcription": "test_transcription_2"
                        }
                    }
                ],
                "verification_failures": [
                    "test_verification_failure_1",
                    "test_verification_failure_2"
                ],
                "verification_attempts_count": 12,
                "slice_ids": [
                    "test_slice_id_1",
                    "test_slice_id_2"
                ]
            },
            "labels": {
                "additionalProp1": "test_additional_prop_1",
                "additionalProp2": "test_additional_prop_2",
                "additionalProp3": "test_additional_prop_3"
            },
            "description": "test_description",
            "preview_url": "test_preview_url",
            "available_for_tiers": [
                "test_available_for_tier_1",
                "test_available_for_tier_2"
            ],
            "settings": {
                "stability": 0.3,
                "similarity_boost": 0.4
            }
        }

        voice = VoiceFactory.create(voice_properties)

        self.assertEqual(voice.id, "test_voice_id")
        self.assertEqual(voice.name, "test_name")
        self.assertEqual(voice.samples[0].id, "test_sample_id_1")
        self.assertEqual(voice.samples[0].file_name, "test_file_name_1")
        self.assertEqual(voice.samples[0].mime_type, "test_mime_type_1")
        self.assertEqual(voice.samples[0].size, 123)
        self.assertEqual(voice.samples[0].hash, "test_hash_1")
        self.assertEqual(voice.samples[1].id, "test_sample_id_2")
        self.assertEqual(voice.samples[1].file_name, "test_file_name_2")
        self.assertEqual(voice.samples[1].mime_type, "test_mime_type_2")
        self.assertEqual(voice.samples[1].size, 456)
        self.assertEqual(voice.samples[1].hash, "test_hash_2")
        self.assertEqual(voice.category, "test_category")
        self.assertEqual(voice.fine_tuning.model_id, "test_model_id")
        self.assertEqual(voice.fine_tuning.is_allowed_to_fine_tune, True)
        self.assertEqual(voice.fine_tuning.fine_tuning_requested, True)
        self.assertEqual(voice.fine_tuning.fine_tuning_state, "not_started")
        self.assertEqual(voice.fine_tuning.verification_attempts[0].text, "test_text_1")
        self.assertEqual(voice.fine_tuning.verification_attempts[0].date, 12345)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].accepted, True)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].similarity, 0.1)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].levenshtein_distance, 2)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].recording.id, "test_recording_id_1")
        self.assertEqual(voice.fine_tuning.verification_attempts[0].recording.mime_type, "test_mime_type_1")
        self.assertEqual(voice.fine_tuning.verification_attempts[0].recording.size, 876)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].recording.date, 34212)
        self.assertEqual(voice.fine_tuning.verification_attempts[0].recording.transcription, "test_transcription_1")
        self.assertEqual(voice.fine_tuning.verification_attempts[1].text, "test_text_2")
        self.assertEqual(voice.fine_tuning.verification_attempts[1].date, 567789)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].accepted, False)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].similarity, 0.6)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].levenshtein_distance, 3)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].recording.id, "test_recording_id_2")
        self.assertEqual(voice.fine_tuning.verification_attempts[1].recording.mime_type, "test_mime_type_2")
        self.assertEqual(voice.fine_tuning.verification_attempts[1].recording.size, 543)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].recording.date, 848775)
        self.assertEqual(voice.fine_tuning.verification_attempts[1].recording.transcription, "test_transcription_2")
        self.assertEqual(voice.fine_tuning.verification_failures[0], "test_verification_failure_1")
        self.assertEqual(voice.fine_tuning.verification_failures[1], "test_verification_failure_2")
        self.assertEqual(voice.fine_tuning.verification_attempts_count, 12)
        self.assertEqual(voice.fine_tuning.slice_ids[0], "test_slice_id_1")
        self.assertEqual(voice.fine_tuning.slice_ids[1], "test_slice_id_2")
        self.assertEqual(voice.labels["additionalProp1"], "test_additional_prop_1")
        self.assertEqual(voice.labels["additionalProp2"], "test_additional_prop_2")
        self.assertEqual(voice.labels["additionalProp3"], "test_additional_prop_3")
        self.assertEqual(voice.description, "test_description")
        self.assertEqual(voice.preview_url, "test_preview_url")
        self.assertEqual(voice.available_for_tiers[0], "test_available_for_tier_1")
        self.assertEqual(voice.available_for_tiers[1], "test_available_for_tier_2")
        self.assertEqual(voice.settings.stability, 0.3)
        self.assertEqual(voice.settings.similarity_boost, 0.4)

    def test_create_voice_settings(self):
        settings_properties = {
            "stability": 0.3,
            "similarity_boost": 0.4
        }

        voice_settings = VoiceFactory.create_voice_settings(settings_properties)

        self.assertEqual(voice_settings.stability, 0.3)
        self.assertEqual(voice_settings.similarity_boost, 0.4)
