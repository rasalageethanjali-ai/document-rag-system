def build_rag_prompt(context: str, question: str) -> str:
    return f"""
You are a factual question-answering assistant.

RULES:
- Use ONLY the information in the CONTEXT.
- If the answer is not in the context, say:
  "The answer is not found in the provided documents."
- Do NOT use outside knowledge.
- Do NOT guess.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
