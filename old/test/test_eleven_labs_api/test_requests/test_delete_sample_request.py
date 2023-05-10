import unittest
from old.eleven_labs_api.requests.delete_sample_request import DeleteSampleRequest
from api_client.input_validation.exceptions.empty_sample_id import EmptySampleId
from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId


class TestDeleteSampleRequest(unittest.TestCase):
    def test_delete_sample_request_constructs_properly(self):
        voice_id = 'voice_id'
        sample_id = 'sample_id'

        expected_uri = f'/v1/voices/{voice_id}/samples/{sample_id}'
        expected_payload = {}

        request = DeleteSampleRequest(voice_id, sample_id)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_delete_sample_request_raises_exception_when_voice_id_is_empty(self):
        voice_id = ''
        sample_id = 'sample_id'

        with self.assertRaises(EmptyVoiceId):
            DeleteSampleRequest(voice_id, sample_id)

    def test_delete_sample_request_raises_exception_when_sample_id_is_empty(self):
        voice_id = 'voice_id'
        sample_id = ''

        with self.assertRaises(EmptySampleId):
            DeleteSampleRequest(voice_id, sample_id)
