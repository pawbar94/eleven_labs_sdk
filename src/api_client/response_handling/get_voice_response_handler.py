import json
from typing import Any, List
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler
from src.api_client.response_handling.utils import create_voice_settings
from src.common.voice.fine_tuning_verification_attempt import FineTuningVerificationAttempt
from src.common.voice.voice import Voice
from src.common.voice.voice_fine_tuning import VoiceFineTuning
from src.common.voice.voice_recording import VoiceRecording
from src.common.voice.voice_sample import VoiceSample


class GetVoiceResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_voice(data)

    def __create_voice(self, voice_properties: dict) -> Voice:
        return Voice(id=voice_properties['voice_id'], name=voice_properties['name'],
                     samples=self.__create_samples(voice_properties['samples']),
                     category=voice_properties['category'],
                     fine_tuning=self.__create_fine_tuning(voice_properties['fine_tuning']),
                     labels=voice_properties['labels'], description=voice_properties['description'],
                     preview_url=voice_properties['preview_url'],
                     available_for_tiers=voice_properties['available_for_tiers'],
                     settings=create_voice_settings(voice_properties['settings']))

    def __create_samples(self, samples_properties: list) -> List[VoiceSample]:
        samples: List[VoiceSample] = []

        if not samples_properties:
            return []

        for sample_properties in samples_properties:
            samples.append(VoiceSample(id=sample_properties['sample_id'], file_name=sample_properties['file_name'],
                                       mime_type=sample_properties['mime_type'], size=sample_properties['size_bytes'],
                                       hash=sample_properties['hash']))
        return samples

    def __create_fine_tuning(self, fine_tuning_properties: dict) -> VoiceFineTuning:
        return VoiceFineTuning(model_id=fine_tuning_properties['model_id'],
                               is_allowed_to_fine_tune=fine_tuning_properties['is_allowed_to_fine_tune'],
                               fine_tuning_requested=fine_tuning_properties['fine_tuning_requested'],
                               fine_tuning_state=fine_tuning_properties['finetuning_state'],
                               verification_attempts=self.__create_verification_attempts(
                                   fine_tuning_properties['verification_attempts']),
                               verification_failures=fine_tuning_properties['verification_failures'],
                               verification_attempts_count=fine_tuning_properties['verification_attempts_count'],
                               slice_ids=fine_tuning_properties['slice_ids'])

    def __create_verification_attempts(self,
                                       verification_attempts_properties: list) -> List[FineTuningVerificationAttempt]:
        attempts: List[FineTuningVerificationAttempt] = []

        if not verification_attempts_properties:
            return []

        for attempt_properties in verification_attempts_properties:
            attempts.append(FineTuningVerificationAttempt(text=attempt_properties['text'],
                                                          date=attempt_properties['date_unix'],
                                                          accepted=attempt_properties['accepted'],
                                                          similarity=attempt_properties['similarity'],
                                                          levenshtein_distance=attempt_properties[
                                                              'levenshtein_distance'],
                                                          recording=self.__create_recording(
                                                              attempt_properties['recording'])))
        return attempts

    def __create_recording(self, recording_properties: dict) -> VoiceRecording:
        return VoiceRecording(id=recording_properties['recording_id'], mime_type=recording_properties['mime_type'],
                              size=recording_properties['size_bytes'],
                              upload_date=recording_properties['upload_date_unix'],
                              transcription=recording_properties['transcription'])
