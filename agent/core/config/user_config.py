import json
from pathlib import Path

def get_config_path() -> Path:
    config_path = Path(__file__).parent / 'config.json'
    return config_path

def get_user_config() -> dict:
    json_text = get_config_path().read_text(encoding='utf-8')
    return json.loads(json_text)

def update_user_config(new_config: dict):
    if not isinstance(new_config, dict):
        raise TypeError("new_config must be a dictionary.")

    get_config_path().write_text(json.dumps(new_config, indent=4), encoding='utf-8')