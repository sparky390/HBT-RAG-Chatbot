from rag.retriever import retrieve_context
from llm.ollama_client import generate_response

def ask_question(question):

    results = retrieve_context(
        question,
        top_k=3
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
You are an AI Knowledge Assistant for HBT.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
say:

"I could not find relevant information in the knowledge base."
"""

    return generate_response(prompt)