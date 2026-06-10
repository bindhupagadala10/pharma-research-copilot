from src.pdf_loader import load_multiple_pdfs
from src.chunker import chunk_documents
from src.embedder import generate_embedding

import chromadb


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="pharma_docs"
)


research_docs = load_multiple_pdfs(
    "data/research_papers",
    "research_papers"
)

drug_docs = load_multiple_pdfs(
    "data/drug_labels",
    "drug_labels"
)

trial_docs = load_multiple_pdfs(
    "data/clinical_trials",
    "clinical_trials"
)

documents = research_docs + drug_docs + trial_docs

chunks = chunk_documents(documents)

print("Chunks:", len(chunks))


for i, chunk in enumerate(chunks):

    embedding = generate_embedding(
        chunk["chunk"]
    )

    collection.add(
        ids=[str(i)],
        documents=[chunk["chunk"]],
        embeddings=[embedding.tolist()],
        metadatas=[
            {
                "filename": chunk["filename"],
                "category": chunk["category"]
            }
        ]
    )

print("Vector database built successfully")

print(
    f"Total vectors stored: {collection.count()}"
)