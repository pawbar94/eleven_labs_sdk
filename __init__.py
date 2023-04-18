import os
import sys

ELEVEN_LABS_SDK_DIR: str = os.path.dirname(os.path.realpath(__file__))
sys.path.append(ELEVEN_LABS_SDK_DIR)

from .eleven_labs_api.eleven_labs_api import ElevenLabsApi
from .eleven_labs_api.responses.voice_model.voice import Voice
from .eleven_labs_api.responses.voice_model.voice_settings import VoiceSettings
from .eleven_labs_api.responses.history_item_model.history_item import HistoryItem
from .eleven_labs_api.responses.user_info_model.user_subscription_info import UserSubscriptionInfo
from .eleven_labs_api.responses.user_info_model.user_info import UserInfo