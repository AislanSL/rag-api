from app.core.config import COLLECTION_NAME
from app.core.qdrant_client import get_qdrant_client
from qdrant_client.models import Distance, VectorParams
from langchain.vectorstores import Qdrant as LCQdrant

def create_collection(embeddings):
    client = get_qdrant_client()
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=len(embeddings.embed_query("test")),
            distance=Distance.COSINE
        )
    )

def store_vectors(chunks, embeddings):
    return LCQdrant.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        host="localhost",
        port=6333
    )