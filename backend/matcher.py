def extract_skills(text, taxonomy):
    found_skills = set()
    for category in taxonomy:
        for skill in taxonomy[category]:
            if skill.lower() in text:
                found_skills.add(skill)
    return found_skills

def match_skills(resume_skills, jd_skills):
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)
    score = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0.0
    return matched, missing, score
