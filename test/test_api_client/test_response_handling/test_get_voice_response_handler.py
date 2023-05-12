import json
import unittest
from unittest.mock import MagicMock
from api_client.response_handling.get_voice_response_handler import GetVoiceResponseHandler
from common.voice.fine_tuning_verification_attempt import FineTuningVerificationAttempt
from common.voice.voice import Voice
from common.voice.voice_fine_tuning import VoiceFineTuning
from common.voice.voice_recording import VoiceRecording
from common.voice.voice_sample import VoiceSample
from common.voice.voice_settings import VoiceSettings


class TestGetVoiceResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
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
        }
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        samples = [
            VoiceSample(id='some sample ID 1', file_name='some file name 1', mime_type='some mime type 1',
                        size=1, hash='some hash 1')
        ]
        recording = VoiceRecording(id='some recording ID 1', mime_type='some mime type 1', size=1, upload_date=1,
                                   transcription='some transcription 1')
        verification_attempt = FineTuningVerificationAttempt(text='some text 1', date=1, accepted=True,
                                                             similarity=1, levenshtein_distance=1,
                                                             recording=recording)
        fine_tuning = VoiceFineTuning(model_id='some model ID 1', is_allowed_to_fine_tune=True,
                                      fine_tuning_requested=True, fine_tuning_state='some fine tuning state 1',
                                      verification_attempts=[verification_attempt],
                                      verification_failures=['some verification failure 1'],
                                      verification_attempts_count=1, slice_ids=['some slice ID 1'])
        settings = VoiceSettings(stability=1, similarity_boost=1)
        voice = Voice(id='some voice ID 1', name='some name 1', samples=samples, category='some category 1',
                      fine_tuning=fine_tuning, labels={'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},
                      description='some description 1', preview_url='some preview URL 1',
                      available_for_tiers=['some tier 1', 'some tier 2'], settings=settings)

        expected_data = voice

        response_handler = GetVoiceResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_data, processed_response)
