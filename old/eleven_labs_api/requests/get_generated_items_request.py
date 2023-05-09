from old.eleven_labs_api.requests.request_interface import RequestInterface


class GetGeneratedItemsRequest(RequestInterface):
    def uri(self) -> str:
        return '/v1/history'

    def payload(self) -> dict:
        return {}
