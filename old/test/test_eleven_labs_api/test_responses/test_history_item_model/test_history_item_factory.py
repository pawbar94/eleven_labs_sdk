import unittest
from old.eleven_labs_api.responses.history_item_model.history_item_factory import HistoryItemFactory


class TestHistoryItemFactory(unittest.TestCase):
    def test_create(self):
        item_properties: dict = {"history_item_id": "test_item_id",
                                 "request_id": "test_request_id",
                                 "voice_id": "test_voice_id",
                                 "voice_name": "test_voice_name",
                                 "text": "test_text",
                                 "date_unix": 123456789,
                                 "character_count_change_from": 31789,
                                 "character_count_change_to": 27428,
                                 "content_type": "test_content_type",
                                 "state": "created",
                                 "settings": {
                                     "stability": 0.5,
                                     "similarity_boost": 0.3,
                                 },
                                 "feedback": {
                                     "thumbs_up": True,
                                     "feedback": "test_feedback",
                                     "emotions": True,
                                     "inaccurate_clone": True,
                                     "glitches": True,
                                     "audio_quality": True,
                                     "other": True,
                                     "review_status": "not_reviewed"
                                 }
                                 }

        history_item = HistoryItemFactory.create(item_properties)

        self.assertEqual(history_item.id, "test_item_id")
        self.assertEqual(history_item.request_id, "test_request_id")
        self.assertEqual(history_item.voice_id, "test_voice_id")
        self.assertEqual(history_item.voice_name, "test_voice_name")
        self.assertEqual(history_item.text, "test_text")
        self.assertEqual(history_item.date, 123456789)
        self.assertEqual(history_item.character_count_change_from, 31789)
        self.assertEqual(history_item.character_count_change_to, 27428)
        self.assertEqual(history_item.content_type, "test_content_type")
        self.assertEqual(history_item.state, "created")
        self.assertEqual(history_item.settings.stability, 0.5)
        self.assertEqual(history_item.settings.similarity_boost, 0.3)
        self.assertEqual(history_item.feedback.thumbs_up, True)
        self.assertEqual(history_item.feedback.feedback, "test_feedback")
        self.assertEqual(history_item.feedback.emotions, True)
        self.assertEqual(history_item.feedback.inaccurate_clone, True)
        self.assertEqual(history_item.feedback.glitches, True)
        self.assertEqual(history_item.feedback.audio_quality, True)
        self.assertEqual(history_item.feedback.other, True)
        self.assertEqual(history_item.feedback.review_status, "not_reviewed")
