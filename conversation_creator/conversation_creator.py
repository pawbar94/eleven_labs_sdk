import os
from typing import List, Dict, Tuple
from conversation_creator.dialogue_decomposer import DialogueDecomposer, ActorName
from eleven_labs_api.eleven_labs_api import Voice, ElevenLabsApi
from moviepy.editor import AudioFileClip, concatenate_audioclips

AudioStream = bytes

DIALOGUE_FILE_NAME: str = 'dialogue.mp3'


class ConversationCreator:
    def __init__(self, api: ElevenLabsApi, voices: Dict[ActorName, Voice]):
        self.__api: ElevenLabsApi = api
        self.__voices: Dict[ActorName, Voice] = voices

    def create(self, dialogue: str, output_dir: str) -> None:
        self.__create_project_folder(output_dir)

        roles: List[Tuple[ActorName, str]] = DialogueDecomposer.split_into_roles(actors=list(self.__voices.keys()),
                                                                                 dialogue=dialogue)
        audios: List[Tuple[ActorName, AudioStream]] = self.__get_audio_streams(roles)
        self.__save_individual_files(audios, output_dir)

        audio_clips: List[AudioFileClip] = self.__load_audio_clips(output_dir)
        final_audio = concatenate_audioclips(audio_clips)
        final_audio.write_audiofile(os.path.join(output_dir, DIALOGUE_FILE_NAME))

    def __create_project_folder(self, output_dir: str) -> None:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

    def __get_audio_streams(self, roles: List[Tuple[ActorName, str]]) -> List[Tuple[ActorName, AudioStream]]:
        audio_streams: List[Tuple[ActorName, AudioStream]] = []

        for actor_name, actor_text in roles:
            audio_stream = self.__api.text_to_speech_stream(text=actor_text, voice=self.__voices[actor_name])
            audio_streams.append((actor_name, audio_stream))

        return audio_streams

    def __save_individual_files(self, audios: List[Tuple[ActorName, AudioStream]], output_dir: str) -> None:
        for index, element in enumerate(audios):
            with open(os.path.join(output_dir, f'{element[0]}_{index}.mp3'), 'wb') as f:
                f.write(element[1])

    def __load_audio_clips(self, project_folder: str) -> List[AudioFileClip]:
        audio_clips: List[AudioFileClip] = []

        for filename in os.listdir(project_folder):
            if filename.endswith('.mp3') and filename != DIALOGUE_FILE_NAME:
                audio_clips.append(AudioFileClip(os.path.join(project_folder, filename)))

        return sorted(audio_clips, key=lambda clip: int(os.path.basename(clip.filename).split('_')[1].split('.')[0]))
