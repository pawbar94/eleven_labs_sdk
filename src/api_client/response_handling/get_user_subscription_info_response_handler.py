import json
from typing import Any
from requests import Response
from src.api_client.response_handling.base_response_handler import BaseResponseHandler
from src.common.user_info.invoice import Invoice
from src.common.user_info.user_subscription_info import UserSubscriptionInfo


class GetUserSubscriptionInfoResponseHandler(BaseResponseHandler):
    def __init__(self):
        super().__init__()

    def _get_processed_response(self, response: Response) -> Any:
        data: dict = json.loads(response.text)

        return self.__create_user_subscription_info(data)

    def __create_user_subscription_info(self, user_subscription_info_properties: dict) -> UserSubscriptionInfo:
        return UserSubscriptionInfo(tier=user_subscription_info_properties['tier'],
                                    character_count=user_subscription_info_properties['character_count'],
                                    character_limit=user_subscription_info_properties['character_limit'],
                                    can_extend_character_limit=user_subscription_info_properties['can_extend_character_limit'],
                                    allowed_to_extend_character_limit=user_subscription_info_properties['allowed_to_extend_character_limit'],
                                    next_character_count_reset_unix=user_subscription_info_properties['next_character_count_reset_unix'],
                                    voice_limit=user_subscription_info_properties['voice_limit'],
                                    professional_voice_limit=user_subscription_info_properties['professional_voice_limit'],
                                    can_extend_voice_limit=user_subscription_info_properties['can_extend_voice_limit'],
                                    can_use_instant_voice_cloning=user_subscription_info_properties['can_use_instant_voice_cloning'],
                                    can_use_professional_voice_cloning=user_subscription_info_properties['can_use_professional_voice_cloning'],
                                    currency=user_subscription_info_properties['currency'],
                                    status=user_subscription_info_properties['status'],
                                    next_invoice=self.__create_invoice(user_subscription_info_properties['next_invoice']),
                                    has_open_invoices=user_subscription_info_properties['has_open_invoices'])

    def __create_invoice(self, invoice_properties: dict) -> Invoice:
        return Invoice(amount_due_cents=invoice_properties['amount_due_cents'],
                       next_payment_attempt_unix=invoice_properties['next_payment_attempt_unix'])
