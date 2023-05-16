from src.api_client.api_client import ApiClient
from src.api_client.input_validation.command_input_validators import COMMAND_INPUT_VALIDATORS
from src.api_client.input_validation.input_validator import InputValidator
from src.api_client.params_building.command_params_builders import COMMAND_PARAMS_BUILDERS
from src.api_client.params_building.params_builder import ParamsBuilder
from src.api_client.request_handling.command_request_handlers import COMMAND_REQUEST_HANDLERS
from src.api_client.request_handling.request_handler import RequestHandler
from src.api_client.response_handling.command_response_handlers import COMMAND_RESPONSE_HANDLERS
from src.api_client.response_handling.response_handler import ResponseHandler
from src.api_client.url_building.command_url_builders import COMMAND_URL_BUILDERS
from src.api_client.url_building.url_builder import UrlBuilder


class ElevenLabsApi(ApiClient):
    def __init__(self, api_key: str):
        input_validator: InputValidator = InputValidator(COMMAND_INPUT_VALIDATORS)
        url_builder: UrlBuilder = UrlBuilder(COMMAND_URL_BUILDERS)
        params_builder: ParamsBuilder = ParamsBuilder(COMMAND_PARAMS_BUILDERS)
        request_handler: RequestHandler = RequestHandler(api_key, COMMAND_REQUEST_HANDLERS)
        response_handler: ResponseHandler = ResponseHandler(COMMAND_RESPONSE_HANDLERS)

        super().__init__(input_validator, url_builder, params_builder, request_handler, response_handler)
