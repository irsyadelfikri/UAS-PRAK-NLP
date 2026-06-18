from pdf_reader import extract_text_from_pdf
from workflow import graph

cv_text = extract_text_from_pdf("sample_cv.pdf")

result = graph.invoke(
    {
        "cv_text": cv_text
    }
)

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print(result["summary"])

print("\n" + "=" * 50)
print("STRUKTUR")
print("=" * 50)

print(result["structure_analysis"])

print("\n" + "=" * 50)
print("ATS")
print("=" * 50)

print(result["ats_analysis"])

print("\n" + "=" * 50)
print("FEEDBACK")
print("=" * 50)

print(result["final_feedback"])