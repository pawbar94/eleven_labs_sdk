import unittest
from src.api_client.input_validation.get_user_subscription_info_input_validator import GetUserSubscriptionInfoInputValidator


class TestGetUserSubscriptionInfoInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetUserSubscriptionInfoInputValidator()
        input_validator.validate()
