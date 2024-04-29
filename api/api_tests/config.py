import os


def get_env_var(name):
    """Retrieve an environment variable and raise an exception if it is not found."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} environment variable is not set!")
    else:
        print("DEBUG!!!!! ENV IS CORRECT!")
    return value


# Secrets:
API_KEY = get_env_var("API_KEY")
TOKEN = get_env_var("TOKEN")

# Constant:
BOARD_ID = "bzH1Yram"


