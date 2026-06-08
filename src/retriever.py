import chromadb
from embedder import generate_embedding


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

    return results


if __name__ == "__main__":

    query = "What is PD-1 inhibition?"

    results = search(query)

    print(results)