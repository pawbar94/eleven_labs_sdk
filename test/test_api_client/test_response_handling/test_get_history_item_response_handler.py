import unittest
import json
from unittest.mock import MagicMock
from src.api_client.response_handling.get_history_item_response_handler import GetHistoryItemResponseHandler
from src.common.history_item.feedback import Feedback
from src.common.history_item.history_item import HistoryItem
from src.common.voice.voice_settings import VoiceSettings


class TestGetHistoryItemResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
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
        }

        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = HistoryItem(id='some history item ID 1', request_id='some request ID 1',
                                        voice_id='some voice ID 1',
                                        voice_name='some voice name 1', text='some text 1', date=1,
                                        character_count_change_from=1,
                                        character_count_change_to=1, content_type='some content type 1',
                                        state='some state 1',
                                        settings=VoiceSettings(stability=1, similarity_boost=1),
                                        feedback=Feedback(thumbs_up=True, feedback='some feedback 1', emotions=True,
                                                          inaccurate_clone=True, glitches=True, audio_quality=True,
                                                          other=True, review_status='some review status 1'))

        response_handler = GetHistoryItemResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
