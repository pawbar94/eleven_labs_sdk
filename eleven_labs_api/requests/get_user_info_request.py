from eleven_labs_api.requests.request_interface import RequestInterface


class GetUserInfoRequest(RequestInterface):
    def uri(self) -> str:
        return f'/v1/user'

    def payload(self) -> dict:
        return {}
