import streamlit as st

from workflow import graph
from pdf_reader import extract_text_from_uploaded_file


st.set_page_config(
    page_title="CV Reviewer AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 CV Reviewer AI")
st.write("Analisis CV menggunakan LangChain, LangGraph, dan Ollama")

uploaded_file = st.file_uploader(
    "Upload CV PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Analisis CV"):

        with st.spinner("Menganalisis CV..."):

            cv_text = extract_text_from_uploaded_file(
                uploaded_file
            )

            result = graph.invoke(
                {
                    "cv_text": cv_text
                }
            )

        st.success("Analisis selesai!")

        st.header("📝 Summary")
        st.write(result["summary"])

        st.header("🏗 Struktur CV")
        st.write(result["structure_analysis"])

        st.header("📊 ATS Analysis")
        st.write(result["ats_analysis"])

        st.header("💡 Feedback")
        st.write(result["final_feedback"])