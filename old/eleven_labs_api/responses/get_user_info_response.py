import json
import requests
from old.eleven_labs_api.responses.base_response import BaseResponse
from common.user_info.user_info import UserInfo
from old.eleven_labs_api.responses.user_info_model.user_info_factory import UserInfoFactory


class GetUserInfoResponse(BaseResponse):
    def __init__(self, raw_response: requests.Response):
        super().__init__(raw_response)

    def _get_processed_response(self) -> UserInfo:
        return UserInfoFactory.create(json.loads(self._raw_response.text))
