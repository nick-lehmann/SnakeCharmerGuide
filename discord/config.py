import os
import sys

from dotenv import load_dotenv

load_dotenv()


def get_env_or_exit(name: str) -> str:
    """ Gets an environment variable or exits the program with an error message. """
    value = os.getenv(name)
    if value is None:
        print(f'Please set the "{name}" variable in your environment or `.env` file.')
        sys.exit(1)
    return value


TOKEN = get_env_or_exit('TOKEN')
GUILD = get_env_or_exit('GUILD')
