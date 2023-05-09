import unittest

from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.get_voice_request import GetVoiceRequest


class TestGetVoiceRequest(unittest.TestCase):
    def test_get_voice_request_constructs_properly(self):
        voice_id = '123'
        expected_uri = f'/v1/voices/{voice_id}'
        expected_payload = {}

        request = GetVoiceRequest(voice_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_get_voice_request_raises_exception_when_voice_id_is_none(self):
        voice_id: str = ''

        with self.assertRaises(EmptyVoiceId):
            GetVoiceRequest(voice_id)
