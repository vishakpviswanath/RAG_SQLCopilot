import json
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
import os

load_dotenv()

DATA_PATH = "data/sql_metadata_docs.json"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "sql_metadata"


def main():
    print("📁 Current working directory:", os.getcwd())

    chroma_client = chromadb.Client(
        Settings(
            persist_directory=CHROMA_PATH,
            is_persistent=True
        )
    )

    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    with open(DATA_PATH, "r") as f:
        docs = json.load(f)

    documents, metadatas, ids = [], [], []

    for doc in docs:
        documents.append(doc["content"])
        metadatas.append({
            "table": doc["table"],
            "type": doc["type"],
            "doc_id": doc["doc_id"]
        })
        ids.append(doc["doc_id"])

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print("✅ Documents added to collection")
    print("📦 Collections:", chroma_client.list_collections())
    print("📂 Chroma DB exists:", os.path.exists(CHROMA_PATH))


if __name__ == "__main__":
    main()
