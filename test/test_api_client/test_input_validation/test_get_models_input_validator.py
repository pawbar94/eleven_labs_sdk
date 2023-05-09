import unittest
from api_client.input_validation.get_models_input_validator import GetModelsInputValidator


class TestGetModelsInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetModelsInputValidator()
        input_validator.validate()
