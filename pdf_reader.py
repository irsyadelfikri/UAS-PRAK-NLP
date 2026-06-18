from pypdf import PdfReader

from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_text_from_uploaded_file(uploaded_file):
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    cv_text = extract_text_from_pdf("sample_cv.pdf")

    print(cv_text[:2000])