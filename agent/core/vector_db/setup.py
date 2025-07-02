from agent.core.config import get_user_config
from pathlib import Path
import chromadb

def get_vector_store_path():
    brain_location = get_user_config()
    path = Path(brain_location['brain_location']) / 'vector-store'

    return path

client = chromadb.PersistentClient(path=str(get_vector_store_path()))