import unittest
from old.eleven_labs_api.responses.user_info_model.user_subscription_info_factory import UserSubscriptionInfoFactory


class TestUserSubscriptionInfoFactory(unittest.TestCase):
    def test_create(self):
        user_subscription_info_properties: dict = {"tier": "test_tier",
                                                   "character_count": 12839,
                                                   "character_limit": 50000,
                                                   "can_extend_character_limit": True,
                                                   "allowed_to_extend_character_limit": True,
                                                   "next_character_count_reset_unix": 123456789,
                                                   "voice_limit": 7,
                                                   "professional_voice_limit": 3,
                                                   "can_extend_voice_limit": True,
                                                   "can_use_instant_voice_cloning": True,
                                                   "can_use_professional_voice_cloning": True,
                                                   "can_use_delayed_payment_methods": True,
                                                   "currency": "usd",
                                                   "status": "trialing",
                                                   "next_invoice": {
                                                       "amount_due_cents": 23430,
                                                       "next_payment_attempt_unix": 987654321
                                                        },
                                                   "has_open_invoices": True
                                                   }

        user_subscription_info = UserSubscriptionInfoFactory.create(user_subscription_info_properties)

        self.assertEqual(user_subscription_info.tier, "test_tier")
        self.assertEqual(user_subscription_info.character_count, 12839)
        self.assertEqual(user_subscription_info.character_limit, 50000)
        self.assertEqual(user_subscription_info.can_extend_character_limit, True)
        self.assertEqual(user_subscription_info.allowed_to_extend_character_limit, True)
        self.assertEqual(user_subscription_info.next_character_count_reset_unix, 123456789)
        self.assertEqual(user_subscription_info.voice_limit, 7)
        self.assertEqual(user_subscription_info.professional_voice_limit, 3)
        self.assertEqual(user_subscription_info.can_extend_voice_limit, True)
        self.assertEqual(user_subscription_info.can_use_instant_voice_cloning, True)
        self.assertEqual(user_subscription_info.can_use_professional_voice_cloning, True)
        self.assertEqual(user_subscription_info.currency, "usd")
        self.assertEqual(user_subscription_info.status, "trialing")
        self.assertEqual(user_subscription_info.next_invoice.amount_due_cents, 23430)
        self.assertEqual(user_subscription_info.next_invoice.next_payment_attempt_unix, 987654321)
        self.assertEqual(user_subscription_info.has_open_invoices, True)
