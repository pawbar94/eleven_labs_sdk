import unittest
import json
from unittest.mock import MagicMock
from api_client.response_handling.get_models_response_handler import GetModelsResponseHandler
from common.model.language import Language
from common.model.model import Model


class TestGetModelsResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = [
            {
                'model_id': 'some model ID 1',
                'name': 'some name 1',
                'can_be_finetuned': True,
                'can_do_text_to_speech': True,
                'can_do_voice_conversion': True,
                'token_cost_factor': 0,
                'description': 'some description 1',
                'languages': [
                    {
                        'language_id': 'some language id 1',
                        'name': 'some language name 1'
                    }
                ]
            },
            {
                'model_id': 'some model ID 2',
                'name': 'some name 2',
                'can_be_finetuned': False,
                'can_do_text_to_speech': False,
                'can_do_voice_conversion': False,
                'token_cost_factor': 1,
                'description': 'some description 2',
                'languages': [
                    {
                        'language_id': 'some language id 2',
                        'name': 'some language name 2'
                    }
                ]
            }
        ]
        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = [
            Model(model_id='some model ID 1', name='some name 1', can_be_finetuned=True,
                  can_do_text_to_speech=True, can_do_voice_conversion=True, token_cost_factor=0,
                  description='some description 1',
                  languages=[Language(id='some language id 1', name='some language name 1')]),
            Model(model_id='some model ID 2', name='some name 2', can_be_finetuned=False,
                  can_do_text_to_speech=False, can_do_voice_conversion=False, token_cost_factor=1,
                  description='some description 2',
                  languages=[Language(id='some language id 2', name='some language name 2')])
        ]

        response_handler = GetModelsResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
