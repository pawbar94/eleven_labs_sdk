import unittest
from eleven_labs_api.responses.user_info_model.user_info_factory import UserInfoFactory


class TestUserInfoFactory(unittest.TestCase):
    def test_create(self):
        user_info_properties: dict = {
            "subscription": {
                "tier": "test_tier",
                "character_count": 12337,
                "character_limit": 20000,
                "can_extend_character_limit": True,
                "allowed_to_extend_character_limit": True,
                "next_character_count_reset_unix": 123456789,
                "voice_limit": 10,
                "professional_voice_limit": 3,
                "can_extend_voice_limit": True,
                "can_use_instant_voice_cloning": True,
                "can_use_professional_voice_cloning": True,
                "currency": "usd",
                "status": "trialing"
            },
            "is_new_user": True,
            "xi_api_key": "test_xi_api_key",
            "can_use_delayed_payment_methods": True
        }

        user_info = UserInfoFactory.create(user_info_properties)

        self.assertEqual(user_info.subscription.tier, "test_tier")
        self.assertEqual(user_info.subscription.character_count, 12337)
        self.assertEqual(user_info.subscription.character_limit, 20000)
        self.assertEqual(user_info.subscription.can_extend_character_limit, True)
        self.assertEqual(user_info.subscription.allowed_to_extend_character_limit, True)
        self.assertEqual(user_info.subscription.next_character_count_reset_unix, 123456789)
        self.assertEqual(user_info.subscription.voice_limit, 10)
        self.assertEqual(user_info.subscription.professional_voice_limit, 3)
        self.assertEqual(user_info.subscription.can_extend_voice_limit, True)
        self.assertEqual(user_info.subscription.can_use_instant_voice_cloning, True)
        self.assertEqual(user_info.subscription.can_use_professional_voice_cloning, True)
        self.assertEqual(user_info.subscription.currency, "usd")
        self.assertEqual(user_info.subscription.status, "trialing")
        self.assertEqual(user_info.is_new_user, True)
        self.assertEqual(user_info.xi_api_key, "test_xi_api_key")
        self.assertEqual(user_info.can_use_delayed_payment_methods, True)
