import unittest
import json
from unittest.mock import MagicMock
from src.api_client.response_handling.get_generated_items_response_handler import GetGeneratedItemsResponseHandler
from src.common.history_item.feedback import Feedback
from src.common.history_item.history_item import HistoryItem
from src.common.voice.voice_settings import VoiceSettings


class TestGetGeneratedItemsResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
            'history': [
                {
                    'history_item_id': 'some history item ID 1',
                    'request_id': 'some request ID 1',
                    'voice_id': 'some voice ID 1',
                    'voice_name': 'some voice name 1',
                    'text': 'some text 1',
                    'date_unix': 1,
                    'character_count_change_from': 1,
                    'character_count_change_to': 1,
                    'content_type': 'some content type 1',
                    'state': 'some state 1',
                    'settings': {
                        'stability': 1,
                        'similarity_boost': 1,
                    },
                    'feedback': {
                        'thumbs_up': True,
                        'feedback': 'some feedback 1',
                        'emotions': True,
                        'inaccurate_clone': True,
                        'glitches': True,
                        'audio_quality': True,
                        'other': True,
                        'review_status': 'some review status 1'
                    }
                },
                {
                    'history_item_id': 'some history item ID 2',
                    'request_id': 'some request ID 2',
                    'voice_id': 'some voice ID 2',
                    'voice_name': 'some voice name 2',
                    'text': 'some text 2',
                    'date_unix': 2,
                    'character_count_change_from': 2,
                    'character_count_change_to': 2,
                    'content_type': 'some content type 2',
                    'state': 'some state 2',
                    'settings': {
                        'stability': 2,
                        'similarity_boost': 2,
                    },
                    'feedback': {
                        'thumbs_up': False,
                        'feedback': 'some feedback 2',
                        'emotions': False,
                        'inaccurate_clone': False,
                        'glitches': False,
                        'audio_quality': False,
                        'other': False,
                        'review_status': 'some review status 2'
                    }
                }
            ]
        }
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = [
            HistoryItem(id='some history item ID 1', request_id='some request ID 1', voice_id='some voice ID 1',
                        voice_name='some voice name 1', text='some text 1', date=1, character_count_change_from=1,
                        character_count_change_to=1, content_type='some content type 1', state='some state 1',
                        settings=VoiceSettings(stability=1, similarity_boost=1),
                        feedback=Feedback(thumbs_up=True, feedback='some feedback 1', emotions=True,
                                          inaccurate_clone=True, glitches=True, audio_quality=True,
                                          other=True, review_status='some review status 1')),
            HistoryItem(id='some history item ID 2', request_id='some request ID 2', voice_id='some voice ID 2',
                        voice_name='some voice name 2', text='some text 2', date=2, character_count_change_from=2,
                        character_count_change_to=2, content_type='some content type 2', state='some state 2',
                        settings=VoiceSettings(stability=2, similarity_boost=2),
                        feedback=Feedback(thumbs_up=False, feedback='some feedback 2', emotions=False,
                                          inaccurate_clone=False, glitches=False, audio_quality=False,
                                          other=False, review_status='some review status 2'))
        ]

        response_handler = GetGeneratedItemsResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
