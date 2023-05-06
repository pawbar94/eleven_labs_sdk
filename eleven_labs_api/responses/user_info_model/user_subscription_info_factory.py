from typing import List

from eleven_labs_api.responses.user_info_model.invoice import Invoice
from eleven_labs_api.responses.user_info_model.language import Language
from eleven_labs_api.responses.user_info_model.model import Model
from eleven_labs_api.responses.user_info_model.user_subscription_info import UserSubscriptionInfo


class UserSubscriptionInfoFactory:
    @staticmethod
    def create(user_subscription_info_properties: dict) -> UserSubscriptionInfo:
        return UserSubscriptionInfo(
            tier=user_subscription_info_properties["tier"],
            character_count=user_subscription_info_properties["character_count"],
            character_limit=user_subscription_info_properties["character_limit"],
            can_extend_character_limit=user_subscription_info_properties["can_extend_character_limit"],
            allowed_to_extend_character_limit=user_subscription_info_properties["allowed_to_extend_character_limit"],
            next_character_count_reset_unix=user_subscription_info_properties["next_character_count_reset_unix"],
            voice_limit=user_subscription_info_properties["voice_limit"],
            professional_voice_limit=user_subscription_info_properties["professional_voice_limit"],
            can_extend_voice_limit=user_subscription_info_properties["can_extend_voice_limit"],
            can_use_instant_voice_cloning=user_subscription_info_properties["can_use_instant_voice_cloning"],
            can_use_professional_voice_cloning=user_subscription_info_properties["can_use_professional_voice_cloning"],
            currency=user_subscription_info_properties["currency"],
            status=user_subscription_info_properties["status"],
            next_invoice=UserSubscriptionInfoFactory.__create_next_invoice(user_subscription_info_properties["next_invoice"]),
            has_open_invoices=user_subscription_info_properties["has_open_invoices"]
        )

    @staticmethod
    def __create_available_models(available_models_properties: dict) -> List[Model]:
        available_models: List[Model] = []

        for available_model_properties in available_models_properties:
            available_models.append(Model(
                id=available_model_properties["model_id"],
                name=available_model_properties["display_name"],
                supported_language=UserSubscriptionInfoFactory.__create_supported_language(available_model_properties["supported_language"])
            ))

        return available_models

    @staticmethod
    def __create_supported_language(supported_language_properties: dict) -> List[Language]:
        supported_language: List[Language] = []

        for language_properties in supported_language_properties:
            supported_language.append(Language(
                iso_code=language_properties["iso_code"],
                name=language_properties["display_name"]
            ))

        return supported_language

    @staticmethod
    def __create_next_invoice(next_invoice_properties: dict) -> Invoice:
        return Invoice(amount_due_cents=next_invoice_properties["amount_due_cents"],
                       next_payment_attempt_unix=next_invoice_properties["next_payment_attempt_unix"])
