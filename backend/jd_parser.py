from backend.matcher import extract_skills

def parse_job_description(text, taxonomy):
    return extract_skills(text.lower(), taxonomy)
