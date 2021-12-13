import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_from_env(name,default_value=None):
    ret = os.getenv(name,default_value)
    if ret is None:
        raise NotImplementedError(f"You did not set variable '{name}' to your environment")

    return ret

TELEBOT_API_TOKEN = get_from_env("TELEBOT_API_TOKEN", None)
