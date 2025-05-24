import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    # Read the bytes only once
    uploaded_file.seek(0)  # reset file pointer just in case
    file_bytes = uploaded_file.read()

    if not file_bytes:
        raise ValueError("Uploaded resume file is empty.")

    file_stream = BytesIO(file_bytes)
    doc = fitz.open(stream=file_stream, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

