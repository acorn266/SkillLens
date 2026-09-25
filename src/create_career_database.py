"""Create the authoritative career intelligence database.

Run from the project root with:
    python src/create_career_database.py

The generated ``career_intelligence.csv`` is the single source of truth
for career requirements.
"""

from pathlib import Path
import sys

# Allow the script to work both as ``python -m src.create_career_database``
# and as ``python src/create_career_database.py`` from the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.skill_intelligence import get_skill_intelligence
from src.skill_normalizer import normalize_skill_name


BASE_DIR = PROJECT_ROOT
OUTPUT_DIR = BASE_DIR / "data" / "processed"


CAREER_PROFILES = {
    "Data Scientist": [
        ("Python", 9, "Critical"),
        ("SQL", 8, "Critical"),
        ("Statistics", 9, "Critical"),
        ("Machine Learning", 9, "Critical"),
        ("Data Visualization", 7, "Important"),
        ("Pandas", 8, "Important"),
        ("Data Cleaning", 8, "Important"),
        ("Communication", 7, "Important"),
    ],
    "Data Analyst": [
        ("SQL", 9, "Critical"),
        ("Excel", 8, "Critical"),
        ("Python", 7, "Important"),
        ("Statistics", 8, "Critical"),
        ("Data Visualization", 8, "Critical"),
        ("Power BI", 8, "Critical"),
        ("Data Cleaning", 8, "Important"),
        ("Communication", 7, "Important"),
    ],
    "Machine Learning Engineer": [
        ("Python", 9, "Critical"),
        ("Machine Learning", 9, "Critical"),
        ("Statistics", 8, "Critical"),
        ("Data Structures", 8, "Important"),
        ("SQL", 7, "Important"),
        ("TensorFlow/PyTorch", 8, "Critical"),
        ("Git", 7, "Important"),
        ("Model Deployment", 8, "Critical"),
    ],
    "AI Engineer": [
        ("Python", 9, "Critical"),
        ("Machine Learning", 9, "Critical"),
        ("Deep Learning", 9, "Critical"),
        ("Statistics", 8, "Important"),
        ("TensorFlow/PyTorch", 8, "Critical"),
        ("APIs", 7, "Important"),
        ("Git", 7, "Important"),
        ("Model Deployment", 8, "Critical"),
    ],
    "Software Engineer": [
        ("Programming", 9, "Critical"),
        ("Data Structures", 8, "Critical"),
        ("Algorithms", 8, "Critical"),
        ("Git", 8, "Important"),
        ("SQL", 7, "Important"),
        ("APIs", 8, "Important"),
        ("Testing", 8, "Important"),
        ("Problem Solving", 9, "Critical"),
    ],
    "Frontend Developer": [
        ("HTML", 9, "Critical"),
        ("CSS", 9, "Critical"),
        ("JavaScript", 9, "Critical"),
        ("React", 8, "Critical"),
        ("Responsive Design", 8, "Important"),
        ("Git", 7, "Important"),
        ("APIs", 7, "Important"),
        ("UI/UX Fundamentals", 7, "Important"),
    ],
    "Backend Developer": [
        ("Programming", 9, "Critical"),
        ("APIs", 9, "Critical"),
        ("SQL", 8, "Critical"),
        ("Database Design", 8, "Critical"),
        ("Git", 8, "Important"),
        ("Authentication", 7, "Important"),
        ("Testing", 8, "Important"),
        ("Cloud Deployment", 7, "Important"),
    ],
    "Full Stack Developer": [
        ("HTML/CSS", 8, "Important"),
        ("JavaScript", 9, "Critical"),
        ("React", 8, "Critical"),
        ("Backend Development", 8, "Critical"),
        ("SQL", 8, "Critical"),
        ("APIs", 9, "Critical"),
        ("Git", 8, "Important"),
        ("Deployment", 7, "Important"),
    ],
    "Mobile App Developer": [
        ("Programming", 9, "Critical"),
        ("Mobile Development", 9, "Critical"),
        ("UI Development", 8, "Important"),
        ("APIs", 8, "Critical"),
        ("Git", 8, "Important"),
        ("Databases", 7, "Important"),
        ("Testing", 8, "Important"),
        ("App Deployment", 7, "Important"),
    ],
    "Data Engineer": [
        ("Python", 8, "Critical"),
        ("SQL", 9, "Critical"),
        ("Data Warehousing", 9, "Critical"),
        ("ETL/ELT", 9, "Critical"),
        ("Apache Spark", 8, "Important"),
        ("Cloud Platforms", 8, "Important"),
        ("Databases", 9, "Critical"),
        ("Git", 7, "Important"),
    ],
    "Cloud Engineer": [
        ("Cloud Computing", 9, "Critical"),
        ("Linux", 8, "Critical"),
        ("Networking", 8, "Critical"),
        ("AWS/Azure/GCP", 9, "Critical"),
        ("Docker", 8, "Important"),
        ("Kubernetes", 7, "Important"),
        ("Terraform", 7, "Important"),
        ("Git", 7, "Important"),
    ],
    "DevOps Engineer": [
        ("Linux", 9, "Critical"),
        ("Cloud Computing", 9, "Critical"),
        ("Docker", 9, "Critical"),
        ("Kubernetes", 8, "Critical"),
        ("CI/CD", 9, "Critical"),
        ("Git", 9, "Critical"),
        ("Terraform", 8, "Important"),
        ("Monitoring", 7, "Important"),
    ],
    "Cybersecurity Analyst": [
        ("Networking", 9, "Critical"),
        ("Cybersecurity Fundamentals", 9, "Critical"),
        ("Linux", 8, "Critical"),
        ("Security Monitoring", 8, "Critical"),
        ("Threat Analysis", 8, "Critical"),
        ("Python", 7, "Important"),
        ("Incident Response", 8, "Critical"),
        ("Risk Assessment", 8, "Important"),
    ],
    "Security Engineer": [
        ("Cybersecurity", 9, "Critical"),
        ("Networking", 9, "Critical"),
        ("Linux", 9, "Critical"),
        ("Cloud Security", 8, "Critical"),
        ("Firewalls", 8, "Critical"),
        ("Identity & Access Management", 8, "Important"),
        ("Python", 7, "Important"),
        ("Security Architecture", 9, "Critical"),
    ],
    "UI/UX Designer": [
        ("UI Design", 9, "Critical"),
        ("UX Design", 9, "Critical"),
        ("Figma", 9, "Critical"),
        ("User Research", 8, "Critical"),
        ("Wireframing", 8, "Critical"),
        ("Prototyping", 9, "Critical"),
        ("Design Systems", 8, "Important"),
        ("Communication", 7, "Important"),
    ],
    "Product Manager": [
        ("Product Strategy", 9, "Critical"),
        ("Market Research", 8, "Critical"),
        ("User Research", 8, "Important"),
        ("Product Analytics", 8, "Important"),
        ("Communication", 9, "Critical"),
        ("Project Management", 8, "Critical"),
        ("Prioritization", 9, "Critical"),
        ("Leadership", 8, "Important"),
    ],
    "Business Analyst": [
        ("Business Analysis", 9, "Critical"),
        ("SQL", 7, "Important"),
        ("Excel", 8, "Critical"),
        ("Data Analysis", 8, "Critical"),
        ("Requirements Gathering", 9, "Critical"),
        ("Process Modeling", 8, "Important"),
        ("Communication", 9, "Critical"),
        ("Problem Solving", 8, "Critical"),
    ],
    "Digital Marketing Specialist": [
        ("Digital Marketing", 9, "Critical"),
        ("SEO", 8, "Critical"),
        ("Content Marketing", 8, "Critical"),
        ("Social Media Marketing", 9, "Critical"),
        ("Google Analytics", 8, "Important"),
        ("Email Marketing", 7, "Important"),
        ("Copywriting", 8, "Important"),
        ("Marketing Analytics", 8, "Important"),
    ],
    "Database Administrator": [
        ("SQL", 10, "Critical"),
        ("Database Management", 9, "Critical"),
        ("Database Security", 8, "Critical"),
        ("Backup & Recovery", 9, "Critical"),
        ("Linux", 7, "Important"),
        ("Performance Tuning", 8, "Critical"),
        ("Cloud Databases", 7, "Important"),
        ("Troubleshooting", 9, "Critical"),
    ],
    "QA Engineer": [
        ("Software Testing", 9, "Critical"),
        ("Test Automation", 9, "Critical"),
        ("Python/Java", 7, "Important"),
        ("API Testing", 8, "Critical"),
        ("SQL", 7, "Important"),
        ("Selenium", 8, "Important"),
        ("Git", 7, "Important"),
        ("Problem Solving", 8, "Critical"),
    ],
    "Network Engineer": [
        ("Networking", 10, "Critical"),
        ("TCP/IP", 9, "Critical"),
        ("Routing & Switching", 9, "Critical"),
        ("Network Security", 8, "Critical"),
        ("Linux", 7, "Important"),
        ("Firewalls", 8, "Important"),
        ("Network Troubleshooting", 9, "Critical"),
        ("Cloud Networking", 7, "Important"),
    ],
}


CAREER_METADATA = {
    "Data Scientist": ("Data & AI", "Uses statistics, programming, and machine learning to turn data into predictions and decisions."),
    "Data Analyst": ("Data & Analytics", "Analyzes business and operational data to uncover trends, insights, and actionable recommendations."),
    "Machine Learning Engineer": ("Data & AI", "Builds, evaluates, and deploys machine learning systems that operate reliably in real applications."),
    "AI Engineer": ("Data & AI", "Builds AI-powered applications by combining machine learning, deep learning, APIs, and deployment practices."),
    "Software Engineer": ("Software Development", "Designs, builds, tests, and maintains reliable software systems."),
    "Frontend Developer": ("Software Development", "Builds accessible, responsive, and interactive user interfaces for the web."),
    "Backend Developer": ("Software Development", "Builds server-side systems, APIs, databases, and application services."),
    "Full Stack Developer": ("Software Development", "Develops complete web applications across frontend, backend, data, and deployment layers."),
    "Mobile App Developer": ("Software Development", "Builds and ships mobile applications with strong user experience and reliable backend integration."),
    "Data Engineer": ("Data & Analytics", "Designs data pipelines, storage systems, and processing workflows that make data usable at scale."),
    "Cloud Engineer": ("Cloud & Infrastructure", "Designs, deploys, and operates scalable cloud infrastructure and services."),
    "DevOps Engineer": ("Cloud & Infrastructure", "Automates software delivery and infrastructure operations using cloud, containers, CI/CD, and monitoring."),
    "Cybersecurity Analyst": ("Cybersecurity", "Monitors systems and investigates threats, incidents, and security risks."),
    "Security Engineer": ("Cybersecurity", "Designs and implements technical controls that protect systems, networks, and cloud environments."),
    "UI/UX Designer": ("Design", "Researches user needs and designs usable interfaces, flows, prototypes, and visual systems."),
    "Product Manager": ("Product & Management", "Guides product strategy, prioritization, discovery, and cross-functional execution."),
    "Business Analyst": ("Business & Analytics", "Translates business problems into requirements, analysis, and practical solutions."),
    "Digital Marketing Specialist": ("Marketing", "Plans and measures digital campaigns across search, content, social, email, and analytics."),
    "Database Administrator": ("Data & Infrastructure", "Maintains secure, reliable, performant database systems and recovery processes."),
    "QA Engineer": ("Software Quality", "Validates software quality through test design, automation, API testing, and systematic problem solving."),
    "Network Engineer": ("Networking & Infrastructure", "Designs, configures, secures, and troubleshoots computer networks."),
}


def build_rows():
    rows = []

    for career, skills in CAREER_PROFILES.items():
        category, description = CAREER_METADATA[career]

        for skill, required_level, importance in skills:
            canonical_skill = normalize_skill_name(skill)
            intelligence = get_skill_intelligence(canonical_skill)

            rows.append({
                "Career": career,
                "Career_Category": category,
                "Career_Description": description,
                "Skill": skill,
                "Skill_Category": intelligence.get("category", "Professional Skill"),
                "Required_Level": int(required_level),
                "Importance": importance,
            })

    return rows


def create_database():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(build_rows())

    master_path = OUTPUT_DIR / "career_intelligence.csv"
    df.to_csv(master_path, index=False)

    print("Career intelligence database created successfully!")
    print(f"Careers: {df['Career'].nunique()}")
    print(f"Skill requirements: {len(df)}")
    print(f"Unique skills: {df['Skill'].nunique()}")
    print(f"Saved master database to: {master_path}")


if __name__ == "__main__":
    create_database()
