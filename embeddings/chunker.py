import os
import json

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

INPUT_FOLDER = "data/processed"
OUTPUT_FILE = "data/chunks.json"

all_chunks = []

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Read all processed text files
for filename in os.listdir(INPUT_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        chunks = splitter.split_text(text)

        for chunk_number, chunk in enumerate(chunks):

            all_chunks.append(
                {
                    "source": filename,
                    "chunk_id": chunk_number,
                    "content": chunk
                }
            )

# Save chunks
with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_chunks,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Created {len(all_chunks)} chunks"
)