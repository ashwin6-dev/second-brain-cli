from core.config import get_user_config
from pathlib import Path
import shutil
from core.vector_db.setup import client
import uuid

notes_collection = client.get_or_create_collection('notes')

def get_inbox_path():
    user_config = get_user_config()
    path = Path(user_config['brain_location']) / 'inbox'

    return path

def add_file(filepath):
    source_path = Path(filepath)
    inbox_dir = get_inbox_path()

    inbox_dir.mkdir(parents=True, exist_ok=True)

    destination_path = inbox_dir / source_path.name
    shutil.copy2(str(source_path), str(destination_path))

    file_content = source_path.read_text()
    metadata = {
        'name': source_path.name,
        'category': 'inbox',
        'folder': ''
    }

    notes_collection.add(
        ids=[str(uuid.uuid4())],
        documents=[file_content],
        metadatas=[metadata]
    )