import chromadb
from chromadb.config import Settings

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "sql_metadata"

def retrieve_context(query: str, top_k: int = 5) -> str:
    chroma_client = chromadb.Client(
        Settings(
            persist_directory=CHROMA_PATH,
            is_persistent=True
        )
    )

    collection = chroma_client.get_collection(
        name=COLLECTION_NAME
    )

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    documents = results["documents"][0] if results["documents"] else []
    return "\n\n".join(documents)
