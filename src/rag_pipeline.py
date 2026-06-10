from src.retriever import search
from src.llm import generate_answer


def answer_question(question):

    results = search(question)

    context = "\n\n".join(
        [
            r["document"]
            for r in results
        ]
    )

    prompt = f"""
You are a pharmaceutical research assistant.

Instructions:
- Use ONLY the provided context.
- Do NOT make up information.
- If the answer is not found in the context, say:
  "The information was not found."
- Summarize clearly.
- Mention important findings.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    sources = list(
        set(
            result["filename"]
            for result in results
        )
   )

    return answer, sources  