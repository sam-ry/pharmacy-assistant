# extract_text.py
import fitz

def pdf_text(pdf_path):
    text=''
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text