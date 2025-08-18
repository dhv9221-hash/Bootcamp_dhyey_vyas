import os
from dotenv import load_dotenv

def load_env(environment_path):
    load_dotenv(dotenv_path=environment_path)

def get_key(key_name):
    val = os.getenv(key_name)
    if val is None:
        print(f"{val} is not an env variable.")
    return val
    