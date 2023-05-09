import unittest
from api_client.input_validation.get_voices_input_validator import GetVoicesInputValidator


class TestGetVoicesInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetVoicesInputValidator()
        input_validator.validate()
