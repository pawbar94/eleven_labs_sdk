import unittest
from api_client.input_validation.get_generated_items_input_validator import GetGeneratedItemsInputValidator


class TestGetGeneratedItemsInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetGeneratedItemsInputValidator()
        input_validator.validate()
