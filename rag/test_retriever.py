from rag.retriever import retrieve_context

results = retrieve_context(
    "What services does HBT provide?"
)

for i, doc in enumerate(results["documents"][0], 1):
    print(f"\n--- Result {i} ---")
    print(doc[:500])