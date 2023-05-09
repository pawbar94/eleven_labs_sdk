from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetVoicesRequest(RequestInterface):
    def uri(self) -> str:
        return '/v1/voices'

    def payload(self) -> dict:
        return {}
