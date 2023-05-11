import unittest


class TestTextToSpeechParamsBuilder(unittest.TestCase):
    def test_build_returns_proper_params(self):
        expected_params = {
            'text': 'some text',
            'model_id': 'some model id',
            'voice_settings': {
                'stability': 0.25,
                'similarity_boost': 0.75
            }
        }
        # params_builder = TextToSpeechParamsBuilder()
        #
        # params = params_builder.build(text='some text', model_id='some model id', stability=0.25, similarity_boost=0.75)
        #
        # self.assertEqual(expected_params, params)
