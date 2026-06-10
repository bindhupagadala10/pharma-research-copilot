import streamlit as st

st.set_page_config(
    page_title="Pharma Research Copilot",
    layout="wide"
)

st.title("💊 Pharma Research Copilot")

st.markdown(
    "Ask questions about uploaded pharmaceutical documents."
)

with st.sidebar:
    st.header("📄 Documents")

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(
            f"{len(uploaded_files)} file(s) uploaded"
        )

    if uploaded_files:
        st.write("Uploaded files:")

        for file in uploaded_files:
            st.write(file.name)

question = st.text_input(
    "Ask a question"
)

if st.button("Get Answer"):

    st.subheader("Answer")

    st.info(
        "RAG response will appear here."
    )

    st.subheader("Sources")

    st.write(
        "Source documents will appear here."
    )