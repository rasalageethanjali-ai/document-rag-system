from app.generation.prompt import build_rag_prompt


class LLM:
    """
    Placeholder LLM interface.
    This is intentionally simple and controlled.
    """

    def __init__(self):
        pass

    def generate(self, context: str, question: str) -> str:
        prompt = build_rag_prompt(context, question)

        # ⚠️ Placeholder response
        # In real usage, this will be replaced with an actual LLM call
        return f"[LLM OUTPUT]\n{prompt}"
