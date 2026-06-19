from rag.retriever import retrieve_context

results = retrieve_context(
    "What services does HBT provide?"
)

print(results)