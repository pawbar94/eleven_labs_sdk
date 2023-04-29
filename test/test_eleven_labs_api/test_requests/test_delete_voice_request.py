import unittest
from eleven_labs_api.requests.delete_voice_request import DeleteVoiceRequest
from eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId


class TestDeleteVoiceRequest(unittest.TestCase):
    def test_delete_voice_request_constructs_properly(self):
        voice_id = 'voice_id'

        expected_uri = f'/v1/voices/{voice_id}'
        expected_payload = {}

        request = DeleteVoiceRequest(voice_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_delete_voice_request_raises_exception_when_voice_id_is_empty(self):
        voice_id = ''

        with self.assertRaises(EmptyVoiceId):
            DeleteVoiceRequest(voice_id)
