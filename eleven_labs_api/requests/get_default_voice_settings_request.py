from eleven_labs_api.requests.request_interface import RequestInterface


class GetDefaultVoiceSettingsRequest(RequestInterface):
    def uri(self) -> str:
        return '/v1/voices/settings/default'

    def payload(self) -> dict:
        return {}
