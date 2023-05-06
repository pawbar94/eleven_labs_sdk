from dataclasses import dataclass
from eleven_labs_api.responses.user_info_model.subscription import Subscription


@dataclass
class UserInfo:
    subscription: Subscription
    is_new_user: bool
    xi_api_key: str
    can_use_delayed_payment_methods: bool

    def __str__(self) -> str:
        return f'subscription:\n' \
               f'   tier: {self.subscription.tier}\n' \
               f'   character_count: {self.subscription.character_count}\n' \
               f'   character_limit: {self.subscription.character_limit}\n' \
               f'   can_extend_character_limit: {self.subscription.can_extend_character_limit}\n' \
               f'   allowed_to_extend_character_limit: {self.subscription.allowed_to_extend_character_limit}\n' \
               f'   next_character_count_reset_unix: {self.subscription.next_character_count_reset_unix}\n' \
               f'   voice_limit: {self.subscription.voice_limit}\n' \
               f'   professional_voice_limit: {self.subscription.professional_voice_limit}\n' \
               f'   can_extend_voice_limit: {self.subscription.can_extend_voice_limit}\n' \
               f'   can_use_instant_voice_cloning: {self.subscription.can_use_instant_voice_cloning}\n' \
               f'   can_use_professional_voice_cloning: {self.subscription.can_use_professional_voice_cloning}\n' \
               f'   currency: {self.subscription.currency}\n' \
               f'   status: {self.subscription.status}\n' \
               f'is_new_user: {self.is_new_user}\n' \
               f'xi_api_key: {self.xi_api_key}\n' \
               f'can_use_delayed_payment_methods: {self.can_use_delayed_payment_methods}'
