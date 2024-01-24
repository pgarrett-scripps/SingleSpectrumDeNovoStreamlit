import os


def get_env_int(var_name, default):
    return int(os.getenv(var_name, default))


def get_env_float(var_name, default):
    return float(os.getenv(var_name, default))


def get_env_str(var_name, default):
    return os.getenv(var_name, default)


BASE_URL = get_env_str('BASE_URL', 'https://spectrum-viewer.streamlit.app/')