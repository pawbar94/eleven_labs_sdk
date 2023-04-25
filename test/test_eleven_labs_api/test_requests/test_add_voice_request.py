import unittest
from eleven_labs_api.requests.add_voice_request import AddVoiceRequest
from eleven_labs_api.requests.exceptions.empty_voice_name import EmptyVoiceName
from eleven_labs_api.requests.exceptions.no_sample_files_provided import NoSampleFilesProvided


class TestAddVoiceRequest(unittest.TestCase):
    def test_add_voice_request_constructs_properly(self):
        name = 'test_name'
        files = ['test_file_1', 'test_file_2']
        description = 'test description'
        labels = 'test_label_1,test_label_2'

        expected_uri = '/v1/voices/add'
        expected_payload = {
            'name': name,
            'files': files,
            'description': description,
            'labels': labels
        }

        request = AddVoiceRequest(name, files, description, labels)

        self.assertEqual(request.uri(), expected_uri)
        self.assertEqual(request.payload(), expected_payload)

    def test_add_voice_raises_exception_when_name_is_empty(self):
        name = ''
        files = ['test_file_1', 'test_file_2']
        description = 'test description'
        labels = 'test_label_1,test_label_2'

        with self.assertRaises(EmptyVoiceName):
            AddVoiceRequest(name, files, description, labels)

    def test_add_voice_raises_exception_when_files_are_empty(self):
        name = 'test_name'
        files = []
        description = 'test description'
        labels = 'test_label_1,test_label_2'

        with self.assertRaises(NoSampleFilesProvided):
            AddVoiceRequest(name, files, description, labels)
