import re
import streamlit as st

from workflow import graph
from pdf_reader import extract_text_from_uploaded_file


st.set_page_config(
    page_title="CV Reviewer AI",
    page_icon="📄",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.title("📄 CV Reviewer AI")

    st.markdown("""
### Teknologi

- LangChain
- LangGraph
- LangSmith
- Ollama
- Streamlit
""")

    st.markdown("---")

    st.markdown("""
### 🔄 Workflow

📄 Upload CV

⬇️

📑 Extract Text

⬇️

🏗️ Structure Analysis

⬇️

🎯 ATS Analysis

⬇️

📝 Candidate Summary

⬇️

💡 Final Feedback
""")

# =========================
# MAIN PAGE
# =========================

st.title("📄 CV Reviewer AI")
st.caption("Analisis CV menggunakan LangChain, LangGraph, LangSmith, dan Ollama")

uploaded_file = st.file_uploader(
    "Upload CV PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("CV berhasil diupload")

    if st.button("🚀 Analisis CV"):

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

        # =========================
        # ATS SCORE CARD
        # =========================

        ats_text = result["ats_analysis"]

        score_match = re.search(
            r"ATS SCORE:\s*(\d+)",
            ats_text
        )

        if score_match:
            score = int(score_match.group(1))

            st.metric(
                label="🎯 ATS Score",
                value=f"{score}/100"
            )

            st.progress(score / 100)

        st.divider()

        # =========================
        # TABS
        # =========================

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📝 Summary",
                "🏗 Struktur CV",
                "📊 ATS Analysis",
                "💡 Feedback"
            ]
        )

        with tab1:
            st.write(result["summary"])

        with tab2:
            st.write(result["structure_analysis"])

        with tab3:
            st.write(result["ats_analysis"])

        with tab4:
            st.write(result["final_feedback"])