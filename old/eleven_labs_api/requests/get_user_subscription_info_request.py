from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetUserSubscriptionInfoRequest(RequestInterface):
    def uri(self) -> str:
        return f'/v1/user/subscription'

    def payload(self) -> dict:
        return {}
