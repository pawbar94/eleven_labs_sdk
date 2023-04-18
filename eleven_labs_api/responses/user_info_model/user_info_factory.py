from typing import List

from eleven_labs_api.responses.user_info_model.language import Language
from eleven_labs_api.responses.user_info_model.model import Model
from eleven_labs_api.responses.user_info_model.subscription import Subscription
from eleven_labs_api.responses.user_info_model.user_info import UserInfo


class UserInfoFactory:
    @staticmethod
    def create(user_info_properties: dict) -> UserInfo:
        return UserInfo(
            subscription=UserInfoFactory.__create_subscription(user_info_properties["subscription"]),
            is_new_user=user_info_properties["is_new_user"],
            xi_api_key=user_info_properties["xi_api_key"],
        )

    @staticmethod
    def __create_subscription(subscription_properties: dict) -> Subscription:
        return Subscription(tier=subscription_properties["tier"],
                            character_count=subscription_properties["character_count"],
                            character_limit=subscription_properties["character_limit"],
                            can_extend_character_limit=subscription_properties["can_extend_character_limit"],
                            allowed_to_extend_character_limit=subscription_properties["allowed_to_extend_character_limit"],
                            next_character_count_reset_unix=subscription_properties["next_character_count_reset_unix"],
                            voice_limit=subscription_properties["voice_limit"],
                            professional_voice_limit=subscription_properties["professional_voice_limit"],
                            can_extend_voice_limit=subscription_properties["can_extend_voice_limit"],
                            can_use_instant_voice_cloning=subscription_properties["can_use_instant_voice_cloning"],
                            can_use_professional_voice_cloning=subscription_properties["can_use_professional_voice_cloning"],
                            available_models=UserInfoFactory.__create_available_models(subscription_properties["available_models"]),
                            can_use_delayed_payment_methods=subscription_properties["can_use_delayed_payment_methods"],
                            currency=subscription_properties["currency"],
                            status=subscription_properties["status"],
                            )

    @staticmethod
    def __create_available_models(available_models_properties: list) -> List[Model]:
        available_models: List[Model] = []

        for available_model_properties in available_models_properties:
            available_models.append(Model(
                id=available_model_properties["model_id"],
                name=available_model_properties["display_name"],
                supported_language=UserInfoFactory.__create_supported_language(
                    available_model_properties["supported_language"])
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
