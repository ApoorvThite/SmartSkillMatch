import streamlit as st
import json

from backend.resume_parser import parse_resume
from backend.jd_parser import parse_job_description
from backend.matcher import match_skills
from backend.recommender import recommend
from backend.recommender import roadmap_for_skills
from backend.coach import generate_ai_coach_response
from utils.pdf_parser import extract_text_from_pdf

# Title
st.set_page_config(page_title="Smart Skill Mapper")
st.title("🔍 Smart Skill Mapper for Job Descriptions")

# Load skill taxonomy
with open("skills_taxonomy.json") as f:
    taxonomy = json.load(f)

# Upload resume
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

# Paste JD
jd_text = st.text_area("🧾 Paste the Job Description Below")

# Analyze
if resume_file and jd_text:
    with st.spinner("Analyzing resume and job description..."):
        resume_skills = parse_resume(resume_file, taxonomy)
        jd_skills = parse_job_description(jd_text, taxonomy)
        matched, missing, score = match_skills(resume_skills, jd_skills)

        st.subheader("✅ Results")
        st.metric("Match Score", f"{score}%")

        st.success(f"Matched Skills ({len(matched)}): {', '.join(sorted(matched))}")
        st.warning(f"Missing Skills ({len(missing)}): {', '.join(sorted(missing))}")

        st.subheader("📚 Recommended Resources")
        resources = recommend(missing)
        for skill, link in resources.items():
            st.markdown(f"- [{skill}]({link})")

        st.subheader("🛣️ Skill Roadmap with Learning Plans")
        roadmap = roadmap_for_skills(missing)

        for skill, info in roadmap.items():
            st.markdown(f"**{skill}**")
            st.markdown(f"- Type: {info['type']}")
            st.markdown(f"- Estimated Time: {info['time_estimate']}")
            st.markdown(f"- [Course Link]({info['course']})")

        if st.button("🧠 Get Personalized Career Advice"):
            with st.spinner("Calling AI Career Coach..."):
                resume_text = extract_text_from_pdf(resume_file)  # or use extracted text
                ai_output = generate_ai_coach_response(resume_text, jd_text, list(missing))
                st.markdown("### 🧠 AI Coach Advice")
                st.markdown(ai_output)

elif not resume_file:
    st.info("Please upload your resume to get started.")

