import json
import unittest
from unittest.mock import MagicMock

from src.api_client.response_handling.get_voices_response_handler import GetVoicesResponseHandler
from src.common.voice.fine_tuning_verification_attempt import FineTuningVerificationAttempt
from src.common.voice.voice import Voice
from src.common.voice.voice_fine_tuning import VoiceFineTuning
from src.common.voice.voice_recording import VoiceRecording
from src.common.voice.voice_sample import VoiceSample
from src.common.voice.voice_settings import VoiceSettings


class TestGetVoicesResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
            'voices': [
                {
                    'voice_id': 'some voice ID 1',
                    'name': 'some name 1',
                    'samples': [
                        {
                            'sample_id': 'some sample ID 1',
                            'file_name': 'some file name 1',
                            'mime_type': 'some mime type 1',
                            'size_bytes': 1,
                            'hash': 'some hash 1',
                        }
                    ],
                    'category': 'some category 1',
                    'fine_tuning': {
                        'model_id': 'some model ID 1',
                        'is_allowed_to_fine_tune': True,
                        'fine_tuning_requested': True,
                        'finetuning_state': 'some fine tuning state 1',
                        'verification_attempts': [
                            {
                                'text': 'some text 1',
                                'date_unix': 1,
                                'accepted': True,
                                'similarity': 1,
                                'levenshtein_distance': 1,
                                'recording': {
                                    'recording_id': 'some recording ID 1',
                                    'mime_type': 'some mime type 1',
                                    'size_bytes': 1,
                                    'upload_date_unix': 1,
                                    'transcription': 'some transcription 1'
                                }
                            }
                        ],
                        'verification_failures': [
                            'some verification failure 1'
                        ],
                        'verification_attempts_count': 1,
                        'slice_ids': [
                            'some slice ID 1'
                        ]
                    },
                    'labels': {
                        'key1': 'value1',
                        'key2': 'value2',
                        'key3': 'value3'
                    },
                    'description': 'some description 1',
                    'preview_url': 'some preview URL 1',
                    'available_for_tiers': [
                        'some tier 1',
                        'some tier 2'
                    ],
                    'settings': {
                        'stability': 1,
                        'similarity_boost': 1,
                    }
                },
                {
                    'voice_id': 'some voice ID 2',
                    'name': 'some name 2',
                    'samples': [
                        {
                            'sample_id': 'some sample ID 2',
                            'file_name': 'some file name 2',
                            'mime_type': 'some mime type 2',
                            'size_bytes': 2,
                            'hash': 'some hash 2',
                        }
                    ],
                    'category': 'some category 2',
                    'fine_tuning': {
                        'model_id': 'some model ID 2',
                        'is_allowed_to_fine_tune': False,
                        'fine_tuning_requested': False,
                        'finetuning_state': 'some fine tuning state 2',
                        'verification_attempts': [
                            {
                                'text': 'some text 2',
                                'date_unix': 2,
                                'accepted': False,
                                'similarity': 2,
                                'levenshtein_distance': 2,
                                'recording': {
                                    'recording_id': 'some recording ID 2',
                                    'mime_type': 'some mime type 2',
                                    'size_bytes': 2,
                                    'upload_date_unix': 2,
                                    'transcription': 'some transcription 2'
                                }
                            }
                        ],
                        'verification_failures': [
                            'some verification failure 2'
                        ],
                        'verification_attempts_count': 2,
                        'slice_ids': [
                            'some slice ID 2'
                        ]
                    },
                    'labels': {
                        'key1': 'value1',
                        'key2': 'value2',
                        'key3': 'value3'
                    },
                    'description': 'some description 2',
                    'preview_url': 'some preview URL 2',
                    'available_for_tiers': [
                        'some tier 2',
                        'some tier 2'
                    ],
                    'settings': {
                        'stability': 2,
                        'similarity_boost': 2,
                    }
                }
            ]
        }
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        samples_1 = [
            VoiceSample(id='some sample ID 1', file_name='some file name 1', mime_type='some mime type 1',
                        size=1, hash='some hash 1')
        ]
        recording_1 = VoiceRecording(id='some recording ID 1', mime_type='some mime type 1', size=1, upload_date=1,
                                     transcription='some transcription 1')
        verification_attempt_1 = FineTuningVerificationAttempt(text='some text 1', date=1, accepted=True,
                                                               similarity=1, levenshtein_distance=1,
                                                               recording=recording_1)
        fine_tuning_1 = VoiceFineTuning(model_id='some model ID 1', is_allowed_to_fine_tune=True,
                                        fine_tuning_requested=True, fine_tuning_state='some fine tuning state 1',
                                        verification_attempts=[verification_attempt_1],
                                        verification_failures=['some verification failure 1'],
                                        verification_attempts_count=1, slice_ids=['some slice ID 1'])
        settings_1 = VoiceSettings(stability=1, similarity_boost=1)
        voice_1 = Voice(id='some voice ID 1', name='some name 1', samples=samples_1, category='some category 1',
                        fine_tuning=fine_tuning_1, labels={'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},
                        description='some description 1', preview_url='some preview URL 1',
                        available_for_tiers=['some tier 1', 'some tier 2'], settings=settings_1)
        samples_2 = [
            VoiceSample(id='some sample ID 2', file_name='some file name 2', mime_type='some mime type 2',
                        size=2, hash='some hash 2')
        ]
        recording_2 = VoiceRecording(id='some recording ID 2', mime_type='some mime type 2', size=2, upload_date=2,
                                     transcription='some transcription 2')
        verification_attempt_2 = FineTuningVerificationAttempt(text='some text 2', date=2, accepted=False,
                                                               similarity=2, levenshtein_distance=2,
                                                               recording=recording_2)
        fine_tuning_2 = VoiceFineTuning(model_id='some model ID 2', is_allowed_to_fine_tune=False,
                                        fine_tuning_requested=False, fine_tuning_state='some fine tuning state 2',
                                        verification_attempts=[verification_attempt_2],
                                        verification_failures=['some verification failure 2'],
                                        verification_attempts_count=2, slice_ids=['some slice ID 2'])
        settings_2 = VoiceSettings(stability=2, similarity_boost=2)
        voice_2 = Voice(id='some voice ID 2', name='some name 2', samples=samples_2, category='some category 2',
                        fine_tuning=fine_tuning_2, labels={'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},
                        description='some description 2', preview_url='some preview URL 2',
                        available_for_tiers=['some tier 2', 'some tier 2'], settings=settings_2)

        expected_data = [voice_1, voice_2]

        response_handler = GetVoicesResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_data, processed_response)
