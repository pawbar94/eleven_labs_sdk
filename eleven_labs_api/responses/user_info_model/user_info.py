from dataclasses import dataclass
from eleven_labs_api.responses.user_info_model.subscription import Subscription


@dataclass
class UserInfo:
    subscription: Subscription
    is_new_user: bool
    xi_api_key: str
