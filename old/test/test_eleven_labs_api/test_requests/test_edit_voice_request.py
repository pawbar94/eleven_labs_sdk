import unittest
from old.eleven_labs_api.requests.edit_voice_request import EditVoiceRequest
from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId


class TestEditVoiceRequest(unittest.TestCase):
    def test_edit_voice_request_constructs_properly(self):
        voice_id = "123"
        name = "name"
        files = ["file1", "file2"]
        description = "description"
        labels = "labels"

        expected_uri = f'/v1/voices/{voice_id}/edit'
        expected_payload = {
            "name": name,
            "files": files,
            "description": description,
            "labels": labels
        }

        edit_voice_request = EditVoiceRequest(voice_id, name, files, description, labels)

        self.assertEqual(edit_voice_request.uri(), expected_uri)
        self.assertEqual(edit_voice_request.payload(), expected_payload)

    def test_edit_voice_request_raises_exception_when_voice_id_is_empty(self):
        voice_id = ""
        name = "name"
        files = ["file1", "file2"]
        description = "description"
        labels = "labels"

        with self.assertRaises(EmptyVoiceId):
            EditVoiceRequest(voice_id, name, files, description, labels)
