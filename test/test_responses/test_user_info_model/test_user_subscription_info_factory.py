import unittest
from eleven_labs_api.responses.user_info_model.user_subscription_info_factory import UserSubscriptionInfoFactory


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
                                                   "available_models": [
                                                       {"model_id": "test_model_id_1",
                                                        "display_name": "test_display_name_1",
                                                        "supported_language": [
                                                            {"iso_code": "test_iso_code_1",
                                                             "display_name": "test_display_name_1"
                                                             }
                                                        ]
                                                        },
                                                       {"model_id": "test_model_id_2",
                                                        "display_name": "test_display_name_2",
                                                        "supported_language": [
                                                            {"iso_code": "test_iso_code_2",
                                                             "display_name": "test_display_name_2"
                                                             }
                                                        ]
                                                        }
                                                   ],
                                                   "can_use_delayed_payment_methods": True,
                                                   "currency": "usd",
                                                   "status": "trialing",
                                                   "next_invoice": {
                                                       "amount_due_cents": 23430,
                                                       "next_payment_attempt_unix": 987654321
                                                   }
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
        self.assertEqual(user_subscription_info.available_models[0].id, "test_model_id_1")
        self.assertEqual(user_subscription_info.available_models[0].name, "test_display_name_1")
        self.assertEqual(user_subscription_info.available_models[0].supported_language[0].iso_code, "test_iso_code_1")
        self.assertEqual(user_subscription_info.available_models[0].supported_language[0].name, "test_display_name_1")
        self.assertEqual(user_subscription_info.available_models[1].id, "test_model_id_2")
        self.assertEqual(user_subscription_info.available_models[1].name, "test_display_name_2")
        self.assertEqual(user_subscription_info.available_models[1].supported_language[0].iso_code, "test_iso_code_2")
        self.assertEqual(user_subscription_info.available_models[1].supported_language[0].name, "test_display_name_2")
        self.assertEqual(user_subscription_info.can_use_delayed_payment_methods, True)
        self.assertEqual(user_subscription_info.currency, "usd")
        self.assertEqual(user_subscription_info.status, "trialing")
        self.assertEqual(user_subscription_info.next_invoice.amount_due_cents, 23430)
        self.assertEqual(user_subscription_info.next_invoice.next_payment_attempt_unix, 987654321)
