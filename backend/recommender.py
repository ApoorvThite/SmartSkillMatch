import json

skill_resources = {
    "Tableau": "https://www.coursera.org/learn/data-visualization-tableau",
    "Power BI": "https://www.coursera.org/learn/power-bi",
    "Scikit-learn": "https://scikit-learn.org/stable/tutorial/index.html",
    "TensorFlow": "https://www.tensorflow.org/tutorials",
    "Git": "https://www.codecademy.com/learn/learn-git",
    "Docker": "https://docker-curriculum.com/",
    "AWS": "https://aws.amazon.com/training/",
    "Google Cloud": "https://www.cloudskillsboost.google/"
}

def recommend(missing_skills):
    return {skill: skill_resources.get(skill, "Search on Coursera or YouTube") for skill in missing_skills}

def load_skill_roadmap():
    with open("skill_courses.json") as f:
        return json.load(f)

def roadmap_for_skills(missing_skills):
    roadmap = load_skill_roadmap()
    return {
        skill: roadmap.get(skill, {
            "course": "Search on YouTube/Coursera",
            "time_estimate": "N/A",
            "type": "Unknown"
        }) for skill in missing_skills
    }

