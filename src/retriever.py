import chromadb
from src.embedder import generate_embedding


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="pharma_docs"
)


def search(query, n_results=5):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved_docs = []

    for doc, meta, dist in zip(
        documents,
        metadatas,
        distances
    ):

        retrieved_docs.append(
            {
                "document": doc,
                "filename": meta["filename"],
                "category": meta["category"],
                "distance": dist
            }
        )

    return retrieved_docs


if __name__ == "__main__":

    query = "What is PD-1 inhibition?"

    results = search(query)

    for i, result in enumerate(results, start=1):

        print("\n" + "=" * 70)

        print(f"Result {i}")

        print("Source:", result["filename"])
        print("Category:", result["category"])
        print("Distance:", round(result["distance"], 4))

        print("\nDocument Preview:\n")

        print(result["document"][:700])

        print("\n" + "=" * 70)