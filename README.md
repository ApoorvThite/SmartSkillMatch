# 🔍 Smart Skill Mapper for Job Descriptions

**An AI-powered resume analyzer and career assistant** that helps you evaluate your skill match with any job description, uncover missing skills, get tailored learning paths, and improve your resume using GPT.


## 🎯 Why I Built This

As a Data Science student actively applying for data science and ML roles, I often found myself:
- Manually comparing job descriptions with my resume,
- Unsure which skills I lacked or should prioritize learning,
- Rewriting bullet points repeatedly for different roles.

That frustration led me to build **Smart Skill Mapper** — a tool that does all this automatically and intelligently. It's designed to help **any job seeker** answer:

> “Do I match this job description?”  
> “What should I learn next?”  
> “How can I rewrite my resume to stand out?”

---

## 💡 What It Does

- 📄 Analyzes your resume and job description
- ✅ Identifies matched and missing skills (keyword-based)
- 📊 Visualizes skill match by category
- 📚 Suggests learning resources with time estimates
- 🧪 Generates GPT-powered capstone project ideas
- ✍️ Rewrites resume bullet points to align with job roles
- 📈 Simulates match score improvement from learning new skills

This project bridges the gap between *job intent* and *job readiness* — turning a static resume into a dynamic career plan.

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

| Upload + Score | Skill Breakdown | Roadmap + Projects | AI Resume Tool | Capstone Project Ideas |
|----------------|-----------------|--------------------|----------------| -----------------------|
| ![upload](screenshots/upload.png) | ![skills](screenshots/skill_match.png) | ![roadmap](screenshots/roadmap.png) | ![resume](screenshots/rewrite.png) | ![project](screenshots/project.png)

---

## 📁 File Structure
```bash
SmartSkillMapper/
│
├── app.py # Main Streamlit app
├── requirements.txt
├── skills_taxonomy.json # Keyword taxonomy by category
│
├── backend/
│ ├── matcher.py # Skill matching + match score logic
│ ├── recommender.py # Course and roadmap generator
│ ├── resume_parser.py # Extract text from resume PDF
│ ├── coach.py # GPT-based personalized career advice
│ ├── projects.py # GPT capstone project generator
│ └── resume_rewriter.py # GPT bullet point rewriter
│
├── utils/
│ └── pdf_parser.py # PDF parsing helper
│
└── screenshots/ # Screenshots for documentation
```

---

## 🛠️ Getting Started

### 📦 Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/SmartSkillMapper.git
cd SmartSkillMapper

# Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Step 3: Install Dependencies

pip install -r requirements.txt


Step 4: Add Your OpenAI API Key
Create .streamlit/secrets.toml and add:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


Step 5: Run the App

streamlit run app.py
```

🌟 Future Enhancements:

 ✅ Skill mastery tracking (checkboxes per skill)

 🔄 Versioned resume tracking & diff viewer

 💬 Integrated GPT chat for Q&A ("What should I learn next?")

 📤 Export resume with rewritten bullet points

 🔍 Compare two resumes side by side

 🌐 Real-time job feed via LinkedIn API or Hugging Face job datasets
 
--------------------------------------------------------------------------------
 
 🙌 Credits & Acknowledgments:
 
OpenAI GPT-3.5

Streamlit

PyMuPDF

Plotly

Coursera, YouTube, Microsoft Learn

---------------------------------------------------------------------------------

👋 Connect with the Developer:

👨‍💻 Apoorv Thite
🎓 Penn State University — Applied Data Science + Economics
🔗 https://linkedin.com/in/apoorvthite21
📬 https://github.com/ApoorvThite
