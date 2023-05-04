import os.path
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
from cli.utils import read_api_key
from cli.user_interface.user_interface import UserInterface
from eleven_labs_api.eleven_labs_api import ElevenLabsApi
from logging import getLogger

logger = getLogger('ElevenLabsCli')

if __name__ == "__main__":
    try:
        api: ElevenLabsApi = ElevenLabsApi(api_key=read_api_key())
        app: UserInterface = UserInterface(sys.argv, api)

        app.init()
        app.run()
    except Exception as e:
        logger.error(e)
        sys.exit(1)
