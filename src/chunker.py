
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = []

    for doc in documents:

        split_texts = splitter.split_text(doc["text"])

        for text in split_texts:

            chunks.append(
                {
                    "chunk": text,
                    "filename": doc["filename"],
                    "category": doc["category"]
                }
            )

    return chunks

from pdf_loader import load_multiple_pdfs


if __name__ == "__main__":

    research_docs = load_multiple_pdfs(
        "data/research_papers",
        "research_papers"
    )

    chunks = chunk_documents(research_docs)

    print(f"Total chunks: {len(chunks)}")

    print("\nFirst chunk:\n")

    print(chunks[0]["chunk"][:500])