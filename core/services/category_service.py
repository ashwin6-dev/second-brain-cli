from core.config import get_user_config
from pathlib import Path

def get_brain_location():
    user_config = get_user_config()
    path = Path(user_config['brain_location'])

    return path

def create_category_folder(category: str, folder_name: str):
    folder_path = get_brain_location() / category / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)