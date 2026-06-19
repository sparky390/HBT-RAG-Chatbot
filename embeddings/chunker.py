import os
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter

INPUT_FOLDER = "data/processed"
OUTPUT_FILE = "data/chunks.json"

all_chunks = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n## ",
        "\n### ",
        "\n#### ",
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)

for filename in sorted(os.listdir(INPUT_FOLDER)):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(INPUT_FOLDER, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    if len(text.split()) < 20:
        print(f"  ⚠ Skipping (too short): {filename}")
        continue

    chunks = splitter.split_text(text)

    for chunk_number, chunk in enumerate(chunks):
        if len(chunk.split()) < 10:
            continue
        all_chunks.append({
            "source": filename,
            "chunk_id": chunk_number,
            "content": chunk.strip(),
        })

    print(f"  ✓ {len(chunks):>3} chunks ← {filename}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=4, ensure_ascii=False)

print(f"\nTotal chunks: {len(all_chunks)} → {OUTPUT_FILE}")