from qdrant_client import QdrantClient
from app.core.config import QDRANT_HOST, QDRANT_PORT

def get_qdrant_client() -> QdrantClient:
    return QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
