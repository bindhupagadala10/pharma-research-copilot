import streamlit as st
from src.rag_pipeline import answer_question

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Pharma Research Copilot",
    page_icon="💊",
    layout="wide"
)

# ====================================
# SESSION STATE
# ====================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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

        st.success(
            f"{file_count} file(s) uploaded"
        )

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

        st.success(
            "✅ PDFs Ready"
        )

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
# RAG EXECUTION
# ====================================

if search_clicked:

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching pharmaceutical documents..."
        ):

            try:

                answer, sources = answer_question(
                    question
                )

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                col1, col2 = st.columns(
                    [3, 1]
                )

                with col1:

                    st.subheader(
                        "🧠 Answer"
                    )

                    st.write(
                        answer
                    )

                    st.download_button(
                        label="📥 Download Answer",
                        data=answer,
                        file_name="answer.txt",
                        mime="text/plain"
                    )

                with col2:

                    st.subheader(
                        "📊 Retrieval"
                    )

                    unique_sources = list(
                        set(sources)
                    )

                    st.metric(
                        "Sources",
                        len(unique_sources)
                    )

                    st.metric(
                        "Question Length",
                        len(question.split())
                    )

                st.divider()

                st.subheader(
                    "📚 Sources"
                )

                for source in unique_sources:

                    st.write(
                        f"📄 {source}"
                    )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# ====================================
# CHAT HISTORY
# ====================================

if st.session_state.chat_history:

    st.divider()

    st.subheader(
        "💬 Previous Questions"
    )

    for i, item in enumerate(
        reversed(
            st.session_state.chat_history
        ),
        start=1
    ):

        with st.expander(
            f"Question {i}: {item['question']}"
        ):

            st.write(
                item["answer"]
            )