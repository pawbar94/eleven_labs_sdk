import unittest
import json
from unittest.mock import MagicMock

from src.api_client.response_handling.get_user_subscription_info_response_handler import \
    GetUserSubscriptionInfoResponseHandler
from src.common.user_info.invoice import Invoice
from src.common.user_info.user_subscription_info import UserSubscriptionInfo


class TestGetUserSubscriptionInfoResponseHandler(unittest.TestCase):
    def test_process_returns_proper_value(self):
        received_data = {
            'tier': 'some tier',
            'character_count': 123,
            'character_limit': 456,
            'can_extend_character_limit': True,
            'allowed_to_extend_character_limit': True,
            'next_character_count_reset_unix': 789,
            'voice_limit': 987,
            'professional_voice_limit': 654,
            'can_extend_voice_limit': False,
            'can_use_instant_voice_cloning': True,
            'can_use_professional_voice_cloning': False,
            'currency': 'some currency',
            'status': 'some status',
            'next_invoice': {
                'amount_due_cents': 123,
                'next_payment_attempt_unix': 456
            },
            'has_open_invoices': True
        }

        response = MagicMock()
        response.status_code = 200
        response.text = json.dumps(received_data)

        expected_response = UserSubscriptionInfo(tier='some tier', character_count=123, character_limit=456,
                                                 can_extend_character_limit=True,
                                                 allowed_to_extend_character_limit=True,
                                                 next_character_count_reset_unix=789, voice_limit=987,
                                                 professional_voice_limit=654, can_extend_voice_limit=False,
                                                 can_use_instant_voice_cloning=True,
                                                 can_use_professional_voice_cloning=False, currency='some currency',
                                                 status='some status', next_invoice=Invoice(amount_due_cents=123,
                                                                                            next_payment_attempt_unix=456),
                                                 has_open_invoices=True)

        response_handler = GetUserSubscriptionInfoResponseHandler()
        processed_response = response_handler.process(response)

        self.assertEqual(expected_response, processed_response)
