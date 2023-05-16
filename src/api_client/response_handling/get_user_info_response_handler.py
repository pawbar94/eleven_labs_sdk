import json
from typing import Any
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler
from src.common.user_info.subscription import Subscription
from src.common.user_info.user_info import UserInfo


class GetUserInfoResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_user_subscription_info(data)

    def __create_user_subscription_info(self, user_subscription_info_properties: dict) -> UserInfo:
        return UserInfo(subscription=self.__create_subscription(user_subscription_info_properties['subscription']),
                        is_new_user=user_subscription_info_properties['is_new_user'],
                        xi_api_key=user_subscription_info_properties['xi_api_key'],
                        can_use_delayed_payment_methods=user_subscription_info_properties[
                            'can_use_delayed_payment_methods'])

    def __create_subscription(self, subscription):
        return Subscription(tier=subscription['tier'], character_count=subscription['character_count'],
                            character_limit=subscription['character_limit'],
                            can_extend_character_limit=subscription['can_extend_character_limit'],
                            allowed_to_extend_character_limit=subscription['allowed_to_extend_character_limit'],
                            next_character_count_reset_unix=subscription['next_character_count_reset_unix'],
                            voice_limit=subscription['voice_limit'],
                            professional_voice_limit=subscription['professional_voice_limit'],
                            can_extend_voice_limit=subscription['can_extend_voice_limit'],
                            can_use_instant_voice_cloning=subscription['can_use_instant_voice_cloning'],
                            can_use_professional_voice_cloning=subscription['can_use_professional_voice_cloning'],
                            currency=subscription['currency'], status=subscription['status'])
