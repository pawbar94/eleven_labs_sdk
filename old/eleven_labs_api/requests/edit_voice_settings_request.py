from old.eleven_labs_api.requests.exceptions.empty_voice_id import EmptyVoiceId
from old.eleven_labs_api.requests.exceptions.invalid_similarity_boost_value import InvalidSimilarityBoostValue
from old.eleven_labs_api.requests.exceptions.invalid_stability_value import InvalidStabilityValue
from old.eleven_labs_api.requests.request_interface import RequestInterface


class EditVoiceSettingsRequest(RequestInterface):
    def __init__(self, voice_id: str, stability: float, similarity_boost: float):
        if not voice_id:
            raise EmptyVoiceId('Voice id cannot be empty!')
        if stability < 0 or stability > 1:
            raise InvalidStabilityValue(f'Stability must be between 0 and 1! The given value is {stability}')
        if similarity_boost < 0 or similarity_boost > 1:
            raise InvalidSimilarityBoostValue(f'Similarity boost must be between 0 and 1! The given value is '
                                              f'{similarity_boost}')

        self.__voice_id: str = voice_id
        self.__stability: float = stability
        self.__similarity_boost: float = similarity_boost

    def uri(self) -> str:
        return f'/v1/voices/{self.__voice_id}/settings/edit'

    def payload(self) -> dict:
        return {
            "stability": self.__stability,
            "similarity_boost": self.__similarity_boost
        }
