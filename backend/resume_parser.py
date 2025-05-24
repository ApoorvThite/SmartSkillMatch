from utils.pdf_parser import extract_text_from_pdf
from backend.matcher import extract_skills

def parse_resume(file, taxonomy):
    text = extract_text_from_pdf(file)
    return extract_skills(text, taxonomy)
