import unittest
from api_client.input_validation.get_user_info_input_validator import GetUserInfoInputValidator


class TestGetUserInfoInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetUserInfoInputValidator()
        input_validator.validate()
