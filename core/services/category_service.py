from core.config import get_user_config
from pathlib import Path
import shutil

from core.services.constants import PROJECT_FOLDER, AREA_FOLDER, RESOURCE_FOLDER, ARCHIVE_FOLDER, INBOX_FOLDER
from core.services.note_service import notes_collection


def get_brain_location():
    user_config = get_user_config()
    path = Path(user_config['brain_location'])

    return path

def create_category_folder(category: str, folder_name: str):
    lower_category = category.lower()
    assert lower_category in [PROJECT_FOLDER, AREA_FOLDER, RESOURCE_FOLDER]

    folder_path = get_brain_location() / lower_category / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

def view_category(category: str):
    lower_category = category.lower()
    assert lower_category in [PROJECT_FOLDER, AREA_FOLDER, RESOURCE_FOLDER, ARCHIVE_FOLDER, INBOX_FOLDER]

    category_path = get_brain_location() / lower_category
    return map(lambda item: { "name": item.name, "is_folder": item.is_dir() } , category_path.iterdir())

def organise_note(note_name: str, category: str, folder_name: str):
    lower_category = category.lower()
    assert lower_category in [PROJECT_FOLDER, AREA_FOLDER, RESOURCE_FOLDER]

    brain_location = get_brain_location()
    note_path = brain_location / 'inbox' / note_name
    folder_path = brain_location / lower_category / folder_name

    shutil.move(str(note_path), str(folder_path))

    print (notes_collection.get())
    note = notes_collection.get(
        where={
            "$and": [
                {"name": note_name},
                {"category": "inbox"}
            ]
        }
    )

    new_metadata = note['metadatas'][0]
    new_metadata['category'] = lower_category
    new_metadata['folder'] = folder_name

    notes_collection.update(
        ids=note['ids'],
        metadatas=[new_metadata]
    )
    print (notes_collection.get())