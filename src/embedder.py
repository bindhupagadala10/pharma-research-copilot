from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text):
    return model.encode(text)


if __name__ == "__main__":

    sample_text = """
    Pembrolizumab is a PD-1 inhibitor used
    in cancer immunotherapy.
    """

    embedding = generate_embedding(sample_text)

    print(type(embedding))
    print("Length:", len(embedding))
    print("First 10 values:")
    print(embedding[:10])