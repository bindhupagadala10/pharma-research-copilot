from pypdf import PdfReader
import os


def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return {
        "filename": os.path.basename(pdf_path),
        "text": text
    }


def load_multiple_pdfs(folder_path, category):
    documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            full_path = os.path.join(folder_path, file)

            doc = load_pdf(full_path)

            doc["category"] = category

            documents.append(doc)

    return documents


if __name__ == "__main__":

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

    all_docs = research_docs + drug_docs + trial_docs

    print(f"\nTotal documents loaded: {len(all_docs)}\n")

    for doc in all_docs:

        print("=" * 60)
        print("File:", doc["filename"])
        print("Category:", doc["category"])
        print("Characters:", len(doc["text"]))
        print("=" * 60)