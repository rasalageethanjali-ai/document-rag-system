from app.generation.prompt import build_rag_prompt


class LLM:
    def generate(self, context: str, question: str) -> str:
        prompt = build_rag_prompt(context, question)
        return f"[LLM OUTPUT]\n{prompt}"
