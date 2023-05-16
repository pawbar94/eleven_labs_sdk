import unittest
from src.api_client.input_validation.get_default_voice_settings_input_validator import GetDefaultVoiceSettingsInputValidator


class TestGetVoiceSettingsInputValidator(unittest.TestCase):
    def test_validate_raises_no_exception(self):
        input_validator = GetDefaultVoiceSettingsInputValidator()
        input_validator.validate()
