from dataclasses import dataclass
from common.user_info.invoice import Invoice


@dataclass
class UserSubscriptionInfo:
    tier: str
    character_count: int
    character_limit: int
    can_extend_character_limit: bool
    allowed_to_extend_character_limit: bool
    next_character_count_reset_unix: int
    voice_limit: int
    professional_voice_limit: int
    can_extend_voice_limit: bool
    can_use_instant_voice_cloning: bool
    can_use_professional_voice_cloning: bool
    currency: str
    status: str
    next_invoice: Invoice
    has_open_invoices: bool

    def __str__(self) -> str:
        return f'tier: {self.tier}\n' \
               f'character_count: {self.character_count}\n' \
               f'character_limit: {self.character_limit}\n' \
               f'can_extend_character_limit: {self.can_extend_character_limit}\n' \
               f'allowed_to_extend_character_limit: {self.allowed_to_extend_character_limit}\n' \
               f'next_character_count_reset_unix: {self.next_character_count_reset_unix}\n' \
               f'voice_limit: {self.voice_limit}\n' \
               f'professional_voice_limit: {self.professional_voice_limit}\n' \
               f'can_extend_voice_limit: {self.can_extend_voice_limit}\n' \
               f'can_use_instant_voice_cloning: {self.can_use_instant_voice_cloning}\n' \
               f'can_use_professional_voice_cloning: {self.can_use_professional_voice_cloning}\n' \
               f'currency: {self.currency}\n' \
               f'status: {self.status}\n' \
               f'next_invoice: {self.next_invoice}\n' \
               f'has_open_invoices: {self.has_open_invoices}\n'
