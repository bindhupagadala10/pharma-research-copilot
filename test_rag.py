from src.rag_pipeline import answer_question

question = input(
    "Ask a question: "
)

answer, sources = answer_question(
    question
)

question = input("Ask a question: ").strip()

if not question:

    print("Please enter a question.")
    exit()

print("\nANSWER\n")
print(answer)

print("\nSOURCES\n")

for source in sources:
    print(source["filename"])