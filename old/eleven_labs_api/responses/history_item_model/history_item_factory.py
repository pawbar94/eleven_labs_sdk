from common.history_item_properties.feedback import Feedback
from common.history_item_properties.history_item import HistoryItem
from old.eleven_labs_api.responses.voice_model.voice_factory import VoiceFactory


class HistoryItemFactory:
    @staticmethod
    def create(item_properties: dict) -> HistoryItem:
        return HistoryItem(id=item_properties['history_item_id'],
                           request_id=item_properties['request_id'],
                           voice_id=item_properties['voice_id'],
                           voice_name=item_properties['voice_name'],
                           text=item_properties['text'],
                           date=item_properties['date_unix'],
                           character_count_change_from=item_properties['character_count_change_from'],
                           character_count_change_to=item_properties['character_count_change_to'],
                           content_type=item_properties['content_type'],
                           state=item_properties['state'],
                           settings=VoiceFactory.create_voice_settings(item_properties['settings']),
                           feedback=HistoryItemFactory.__create_feedback(item_properties['feedback']))

    @staticmethod
    def __create_feedback(feedback_properties: dict) -> Feedback:
        if feedback_properties is None:
            return None

        return Feedback(thumbs_up=feedback_properties['thumbs_up'],
                        feedback=feedback_properties['feedback'],
                        emotions=feedback_properties['emotions'],
                        inaccurate_clone=feedback_properties['inaccurate_clone'],
                        glitches=feedback_properties['glitches'],
                        audio_quality=feedback_properties['audio_quality'],
                        other=feedback_properties['other'],
                        review_status=feedback_properties['review_status'])
