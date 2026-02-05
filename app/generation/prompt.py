def build_rag_prompt(context: str, question: str) -> str:
    """
    Build a strict RAG prompt.
    The model must answer ONLY from the provided context.
    """

    return f"""
You are a factual question-answering assistant.

RULES:
- Use ONLY the information provided in the CONTEXT.
- If the answer is not present in the context, say:
  "The answer is not found in the provided documents."
- Do NOT use outside knowledge.
- Do NOT guess.
- Be concise and accurate.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
