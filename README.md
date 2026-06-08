# Pharma Research Copilot

## Overview

Pharma Research Copilot is a Retrieval-Augmented Generation (RAG) application designed to help researchers query pharmaceutical documents using natural language.

The system retrieves relevant information from research papers, drug labels, and clinical trial documents and generates evidence-backed answers with source citations.

---

## Features

* PDF document ingestion
* Automatic text chunking
* Semantic embeddings using Sentence Transformers
* Vector search using ChromaDB
* Retrieval-Augmented Generation (RAG)
* Streamlit-based user interface
* Source attribution and citations

---

## Project Architecture

PDF Documents
→ PDF Loader
→ Chunking
→ Embeddings
→ ChromaDB Vector Store
→ Retriever
→ LLM
→ Answer + Citations

---

## Dataset

### Research Papers

* Cancer Stem Cells
* Hallmarks of Cancer
* Precision Oncology
* Immunotherapy Response
* Additional oncology literature

### Drug Labels

* KEYTRUDA
* OPDIVO
* REVLIMID
* TAXOL

### Clinical Trials

* Oncology Trial Protocols
* FDA Industry Guidance

---

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Sentence Transformers
* PyPDF

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Build the Vector Database

```bash
python src/build_vector_db.py
```

---

## Run the Application

```bash
streamlit run app/streamlit_app.py
```

---

## Sample Questions

* What is PD-1 inhibition?
* What adverse reactions are associated with KEYTRUDA?
* Explain cancer stem cells.
* What is precision oncology?
* What clinical trial endpoints are commonly used in oncology?

---

## Contributors

* Bindhu Pagadala
* Project Team

```
```
