import json
import chromadb

from sentence_transformers import (
    SentenceTransformer
)

# Load chunks
with open(
    "data/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks")

# Embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="hbt_knowledge"
)

# Store chunks
for index, chunk in enumerate(chunks):

    embedding = model.encode(
        chunk["content"]
    ).tolist()

    collection.add(
        ids=[str(index)],
        documents=[
            chunk["content"]
        ],
        embeddings=[
            embedding
        ],
        metadatas=[
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"]
            }
        ]
    )

print(
    f"Stored {len(chunks)} chunks in ChromaDB"
)