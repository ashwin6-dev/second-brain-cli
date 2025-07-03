from agent.core.config import get_user_config
from pathlib import Path
import shutil
from agent.core.vector_db.setup import client
import uuid

notes_collection = client.get_or_create_collection('notes')

def get_inbox_path():
    brain_location = get_user_config()
    path = Path(brain_location['brain_location']) / 'inbox'

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