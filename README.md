# 🔍 Smart Skill Mapper for Job Descriptions

A powerful AI-driven web application that helps job seekers analyze their resumes against job descriptions to:

- ✅ Identify missing skills
- 🛠 Generate personalized learning resources
- 🧠 Rewrite resume bullet points to match job requirements
- 🧪 Generate capstone project ideas based on skill gaps

Built using **Streamlit**, **OpenAI GPT**, and intelligent keyword-based parsing, this tool transforms how you prepare for job applications.

---

## 🚀 Key Features

### 📄 Resume & Job Description Analysis
- Upload your resume (PDF)
- Paste any job description
- Extracts and compares skills using a custom keyword taxonomy
- Computes a match score and lists matched vs. missing skills

### 📊 Skill Category Match Breakdown
- Visual bar chart of skill match percentage by category
- Understand which technical areas you are strong/weak in (e.g., Tools, ML, Soft Skills)

### 🧭 Skill Roadmap Generator
- Generates a roadmap for each missing skill
- Provides estimated learning time and direct course links (Coursera, YouTube, Docs)
- Helps you learn efficiently with a curated plan

### 🧪 AI-Powered Capstone Project Generator
- For every missing skill, GPT suggests a unique project
- Includes title, goal, tools, dataset ideas, and outcome
- Great for building your portfolio quickly

### 🧠 Resume Bullet Point Rewriter
- Paste an existing resume bullet
- Choose a missing skill and target role
- GPT rewrites your point to highlight that skill and improve relevance to the role

### 📈 Match Score Improvement Simulation
- Shows how learning 2–3 missing skills can boost your match score
- Helps you prioritize what to learn next

---

## 🧩 Tech Stack

| Component      | Tech / Library                     |
|----------------|------------------------------------|
| UI Framework   | [Streamlit](https://streamlit.io/) |
| Resume Parsing | [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) |
| Skill Matching | Custom keyword matching + taxonomy |
| Visualization  | [Plotly](https://plotly.com/python/) |
| AI Models      | [OpenAI GPT-3.5](https://openai.com/) |
| PDF Parsing    | `fitz`, `PyMuPDF`                  |
| Skill Taxonomy | JSON structure of 15+ skill categories |
| Hosting        | Localhost / Streamlit Cloud Ready  |

---

## 📸 Screenshots

| Upload + Score | Skill Breakdown | Roadmap + Projects | AI Resume Tool |
|----------------|-----------------|--------------------|----------------|
| ![upload](screenshots/upload.png) | ![skills](screenshots/skill_match.png) | ![roadmap](screenshots/roadmap.png) | ![resume](screenshots/rewrite.png) |

---

## 📁 File Structure



