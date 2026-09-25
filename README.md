# Skill Gap Predictor

**AI-powered career readiness and skill-gap analysis tool that shows where you stand, identifies your highest-priority gaps, and gives you a practical learning roadmap.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?logo=vercel)](https://vercel.com/)

**Live Demo:** https://skill-gap-predictor.vercel.app/

## Overview

Choosing a career is easy. Knowing **what skills you actually need and what to learn next** is harder.

Skill Gap Predictor lets you select a target career, rate your current skills, and receive an interpretable career-readiness report. It highlights strengths, exposes important skill gaps, creates a personalized learning roadmap, and recommends projects that match those gaps.

> **Important:** The readiness score is an interpretable skill-alignment measure. It is **not** a probability of getting hired and has not been scientifically validated as an employment predictor.

## Key Features

- 🎯 **Career-specific assessment** — choose from 21 career paths.
- 📊 **Readiness score** — weighted skill alignment based on current vs. required levels.
- ⚠️ **Critical-skill analysis** — prevents a strong overall score from hiding major high-priority gaps.
- 💪 **Strength detection** — identifies skills where you already have strong alignment.
- 🔍 **Prioritized skill gaps** — shows what needs attention first.
- 🗺️ **Personalized roadmap** — turns identified gaps into learning and practice stages.
- 🚀 **Project recommendations** — ranks projects according to the learner's actual gaps.
- 🔄 **Career recommendation** — compares skill alignment across supported careers.
- 🧠 **Optional ML experiment** — includes a separate Random Forest experiment using the vocational skill/job-matching dataset.

## How It Works

```text
Choose a target career
        ↓
Load career skill requirements
        ↓
Rate your current skills (1–10)
        ↓
Calculate weighted skill alignment
        ↓
Identify strengths + critical gaps
        ↓
Generate personalized roadmap
        ↓
Recommend career-specific projects
```

## Supported Careers

The current career database includes 21 roles:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- AI Engineer
- Software Engineer
- Frontend Developer
- Backend Developer
- Full Stack Developer
- Mobile App Developer
- Data Engineer
- Cloud Engineer
- DevOps Engineer
- Cybersecurity Analyst
- Security Engineer
- UI/UX Designer
- Product Manager
- Business Analyst
- Digital Marketing Specialist
- Database Administrator
- QA Engineer
- Network Engineer

## Readiness Methodology

For each skill, the application calculates:

```text
alignment = min(current_level / required_level, 1) × 100
```

The overall score is a weighted average where:

```text
Critical skill   = 1.5× weight
Important skill  = 1.0× weight
```

Skill gaps are calculated as:

```text
gap = max(required_level - current_level, 0)
```

Readiness labels:

| Score / condition | Result |
|---|---|
| < 40 | Major Gap |
| 40–59 | Early Foundation |
| 60–74 | Developing |
| 75–89 | Near Ready |
| 90+ | Strong Alignment |
| Severe critical gaps | Critical Gaps |

## Personalized Project Intelligence

Project recommendations are based on four things:

```text
Target career
+ Current skill levels
+ Skill gaps
+ Skill importance
```

Instead of giving everyone the same generic project list, the system ranks projects by how strongly they address the learner's current gaps.

## ML Experiment

The repository also contains an **optional dataset-based ML experiment**. It is separate from the production readiness engine.

The experiment:

- cleans the vocational skill/job-matching dataset,
- engineers skill-gap features,
- encodes categorical features,
- trains a Random Forest classifier,
- evaluates accuracy, ROC-AUC, classification report, and confusion matrix.

This model should **not** be described as an employment predictor for the web application. The live application's readiness score is based on the project's transparent skill-alignment methodology.

Run the optional experiment with:

```bash
python -m src.preprocess
python -m src.train_model
```

## Tech Stack

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data / ML | pandas, NumPy, scikit-learn |
| Testing | pytest |
| Deployment | Vercel |
| Data | CSV-based career intelligence + source datasets |

## Project Structure

```text
Skill_Gap_Predictor/
├── app.py
├── README.md
├── DATASET_NOTES.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── career_intelligence.py
│   ├── career_recommender.py
│   ├── project_intelligence.py
│   ├── reality_check.py
│   ├── roadmap.py
│   ├── skill_intelligence.py
│   ├── skill_normalizer.py
│   ├── preprocess.py
│   └── train_model.py
├── static/
│   ├── css/
│   └── js/
├── templates/
└── tests/
```

## Run Locally

Use Python **3.11 or 3.12** for the most predictable environment.

### 1. Clone the repository

```bash
git clone https://github.com/wajeeha-asad/skill-gap-predictor.git
cd skill-gap-predictor
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open the local Flask address shown in the terminal.

### 5. Run tests

```bash
python -m pytest -q
```

## Data

The application uses `data/processed/career_intelligence.csv` as the authoritative career database.

The original source datasets are kept under `data/raw/`. See [`DATASET_NOTES.md`](DATASET_NOTES.md) for dataset context and processing notes.

The career database can be regenerated with:

```bash
python -m src.create_career_database
```

## Limitations

- Skill levels are self-assessed, so results depend on honest and reasonably calibrated input.
- Career requirements are curated project data rather than a live labor-market feed.
- The readiness score measures alignment with this project's defined skill profiles; it does not predict hiring outcomes.
- The optional Random Forest experiment solves a different dataset-based classification problem and is separate from the readiness engine.
- Project recommendations are rule/data driven rather than learned from historical hiring outcomes.

## What's Next

Possible future improvements include validated assessment questions, real job-posting data, stronger recommendation explainability, saved assessments, automated CI, accessibility testing, and broader career coverage.

## Portfolio Highlights

This project demonstrates:

- Python and Flask development
- Data preprocessing and exploratory analysis
- Machine learning model training and evaluation
- Feature engineering
- Weighted recommendation logic
- Skill normalization
- Personalized roadmap generation
- Career-specific project ranking
- Automated testing
- Separation of an experimental ML model from the production application

## Author

**Wajeeha Asad** — BS Computer Science student building practical AI/ML and software projects.

- GitHub: https://github.com/wajeeha-asad
- Project: https://github.com/wajeeha-asad/skill-gap-predictor
