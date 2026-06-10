import streamlit as st

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Pharma Research Copilot",
    page_icon="💊",
    layout="wide"
)

# ====================================
# HEADER
# ====================================

st.title("💊 Pharma Research Copilot")
st.markdown(
    """
    Ask questions about research papers, clinical trials,
    and drug labels using Retrieval-Augmented Generation (RAG).
    """
)

st.divider()

# ====================================
# SIDEBAR
# ====================================

with st.sidebar:

    st.header("📄 Document Manager")

    uploaded_files = st.file_uploader(
        "Upload Pharmaceutical PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        file_count = len(uploaded_files)

        total_size = sum(
            file.size for file in uploaded_files
        )

        st.success(f"{file_count} file(s) uploaded")

        st.subheader("Uploaded Documents")

        for file in uploaded_files:
            st.write(f"📄 {file.name}")

        st.divider()

        st.subheader("Dataset Summary")

        st.metric(
            "Documents",
            file_count
        )

        st.metric(
            "Total Size",
            f"{round(total_size / (1024 * 1024), 2)} MB"
        )

        st.divider()

        st.subheader("Processing Status")

        st.success("✅ PDFs Ready")

    else:

        st.info(
            "Upload one or more PDF documents."
        )

# ====================================
# QUESTION SECTION
# ====================================

st.subheader("🔍 Ask a Question")

question = st.text_area(
    label="",
    placeholder="Example: What adverse events were reported for Metformin?",
    height=120
)

# ====================================
# SEARCH BUTTON
# ====================================

search_clicked = st.button(
    "🚀 Generate Answer",
    use_container_width=True
)

# ====================================
# ANSWER SECTION
# ====================================

if search_clicked:

    if not uploaded_files:

        st.warning(
            "Please upload at least one PDF."
        )

    elif not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching pharmaceutical documents..."
        ):

            col1, col2 = st.columns([3, 1])

            with col1:

                st.subheader("🧠 Answer")

                st.info(
                    """
                    RAG-generated answer will appear here.

                    Later this section will receive:
                    - Retrieved chunks
                    - LLM response
                    - Grounded answer
                    """
                )

            with col2:

                st.subheader("📊 Retrieval")

                st.metric(
                    "Documents",
                    len(uploaded_files)
                )

                st.metric(
                    "Chunks Retrieved",
                    "0"
                )

            st.divider()

            st.subheader("📚 Sources")

            st.info(
                """
                Source citations will appear here.

                Example:
                - Metformin_Label.pdf
                - Diabetes_Study_2023.pdf
                """
            )