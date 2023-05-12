import json

import requests
from old.eleven_labs_api.responses.base_response import BaseResponse
from common.user_info.user_subscription_info import UserSubscriptionInfo
from old.eleven_labs_api.responses.user_info_model.user_subscription_info_factory import UserSubscriptionInfoFactory


class GetUserSubscriptionInfoResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> UserSubscriptionInfo:
        return UserSubscriptionInfoFactory.create(json.loads(self._raw_response.text))
