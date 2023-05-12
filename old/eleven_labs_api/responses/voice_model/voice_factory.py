from typing import List
from common.voice.fine_tuning_verification_attempt import FineTuningVerificationAttempt
from common.voice.voice import Voice
from common.voice.voice_fine_tuning import VoiceFineTuning
from common.voice.voice_recording import VoiceRecording
from common.voice.voice_sample import VoiceSample
from common.voice.voice_settings import VoiceSettings


class VoiceFactory:
    @staticmethod
    def create(voice_properties: dict) -> Voice:
        return Voice(available_for_tiers=voice_properties['available_for_tiers'],
                     category=voice_properties['category'],
                     description=voice_properties['description'],
                     fine_tuning=VoiceFactory.__create_fine_tuning(voice_properties['fine_tuning']),
                     labels=voice_properties['labels'],
                     name=voice_properties['name'],
                     preview_url=voice_properties['preview_url'],
                     samples=VoiceFactory.__create_voice_samples(voice_properties['samples']),
                     settings=VoiceFactory.create_voice_settings(voice_properties['settings']),
                     id=voice_properties['voice_id'])

    @staticmethod
    def create_voice_settings(voice_settings_properties: dict) -> VoiceSettings:
        settings: VoiceSettings = VoiceSettings()

        if voice_settings_properties:
            settings.stability = voice_settings_properties['stability']
            settings.similarity_boost = voice_settings_properties['similarity_boost']

        return settings

    @staticmethod
    def __create_fine_tuning(fine_tuning_properties: dict) -> VoiceFineTuning:
        return VoiceFineTuning(model_id=fine_tuning_properties['model_id'],
                               is_allowed_to_fine_tune=fine_tuning_properties['is_allowed_to_fine_tune'],
                               fine_tuning_requested=fine_tuning_properties['fine_tuning_requested'],
                               fine_tuning_state=fine_tuning_properties['finetuning_state'],
                               verification_attempts=VoiceFactory.__create_fine_tuning_verification_attempts(fine_tuning_properties['verification_attempts']),
                               verification_failures=fine_tuning_properties['verification_failures'],
                               verification_attempts_count=fine_tuning_properties['verification_attempts_count'],
                               slice_ids=fine_tuning_properties['slice_ids'])

    @staticmethod
    def __create_fine_tuning_verification_attempts(verification_attempts_properties: dict) -> List[FineTuningVerificationAttempt]:
        if not verification_attempts_properties:
            return []

        verification_attempts: List[FineTuningVerificationAttempt] = []

        for verification_attempt_properties in verification_attempts_properties:
            verification_attempts.append(FineTuningVerificationAttempt(text=verification_attempt_properties['text'],
                                                                       date=verification_attempt_properties['date_unix'],
                                                                       accepted=verification_attempt_properties['accepted'],
                                                                       similarity=verification_attempt_properties['similarity'],
                                                                       levenshtein_distance=verification_attempt_properties['levenshtein_distance'],
                                                                       recording=VoiceFactory.__create_voice_recording(verification_attempt_properties['recording'])))
        return verification_attempts

    @staticmethod
    def __create_voice_recording(voice_recording_properties: dict) -> VoiceRecording:
        return VoiceRecording(id=voice_recording_properties['recording_id'],
                              mime_type=voice_recording_properties['mime_type'],
                              size=voice_recording_properties['size_bytes'],
                              date=voice_recording_properties['upload_date_unix'],
                              transcription=voice_recording_properties['transcription'])

    @staticmethod
    def __create_voice_samples(voice_samples_properties: dict) -> List[VoiceSample]:
        if not voice_samples_properties:
            return []

        voice_samples: List[VoiceSample] = []

        for sample_properties in voice_samples_properties:
            voice_samples.append(VoiceSample(id=sample_properties['sample_id'],
                                             file_name=sample_properties['file_name'],
                                             mime_type=sample_properties['mime_type'],
                                             size=sample_properties['size_bytes'],
                                             hash=sample_properties['hash']))
        return voice_samples
