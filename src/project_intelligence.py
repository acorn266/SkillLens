from src.skill_normalizer import normalize_skill_name, skills_match

"""
Intelligent Career Project Recommendation Engine

This module recommends career-specific projects based on:

    - Selected career
    - User's largest skill gaps
    - Skill importance
    - Current skill levels

The goal is not simply to recommend projects for a career.

The goal is to recommend projects that help the learner
close their most important skill gaps.
"""


# ============================================================
# PROJECT INTELLIGENCE DATABASE
# ============================================================

PROJECT_INTELLIGENCE = {

    # ========================================================
    # DATA SCIENTIST
    # ========================================================

    "Data Scientist": [
        {
            "title": "Exploratory Data Analysis Project",
            "description": (
                "Analyze a real-world dataset, clean the data, "
                "identify patterns, visualize findings, and "
                "communicate meaningful insights."
            ),
            "skills": [
                "Python",
                "Statistics",
                "Data Visualization",
                "Data Cleaning",
                "Pandas"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "End-to-End Machine Learning System",
            "description": (
                "Build a complete machine learning solution from "
                "data preparation and feature engineering to model "
                "evaluation and prediction."
            ),
            "skills": [
                "Python",
                "Machine Learning",
                "Statistics",
                "Data Cleaning",
                "Data Visualization"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Professional Analytics & Prediction Platform",
            "description": (
                "Create a polished analytics application that "
                "combines data exploration, visualization and "
                "machine learning predictions."
            ),
            "skills": [
                "Python",
                "Machine Learning",
                "Data Visualization",
                "Pandas",
                "Communication"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # DATA ANALYST
    # ========================================================

    "Data Analyst": [
        {
            "title": "Business Sales Analytics Dashboard",
            "description": (
                "Analyze sales data and build an interactive "
                "dashboard that helps a business understand "
                "revenue, customers and product performance."
            ),
            "skills": [
                "SQL",
                "Excel",
                "Data Analysis",
                "Data Visualization",
                "Power BI"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Customer Analytics Project",
            "description": (
                "Analyze customer behavior, identify important "
                "patterns and translate the findings into "
                "business recommendations."
            ),
            "skills": [
                "SQL",
                "Statistics",
                "Python",
                "Data Visualization",
                "Communication"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Executive Business Intelligence Dashboard",
            "description": (
                "Build a professional BI dashboard with KPIs, "
                "interactive filtering and clear business insights."
            ),
            "skills": [
                "Power BI",
                "SQL",
                "Excel",
                "Data Visualization",
                "Communication"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # MACHINE LEARNING ENGINEER
    # ========================================================

    "Machine Learning Engineer": [
        {
            "title": "End-to-End ML Prediction API",
            "description": (
                "Build, evaluate and expose a machine learning "
                "model through a production-style API."
            ),
            "skills": [
                "Python",
                "Machine Learning",
                "APIs",
                "Model Deployment",
                "Git"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Production ML Pipeline",
            "description": (
                "Create a structured machine learning pipeline "
                "covering preprocessing, training, evaluation "
                "and reproducible prediction."
            ),
            "skills": [
                "Python",
                "Machine Learning",
                "Data Cleaning",
                "Git",
                "Model Deployment"
            ],
            "level": "Intermediate → Advanced"
        },
        {
            "title": "Deployed Machine Learning Application",
            "description": (
                "Turn a trained model into a usable application "
                "with an interface, API and deployment workflow."
            ),
            "skills": [
                "Machine Learning",
                "APIs",
                "Model Deployment",
                "Git",
                "Python"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # AI ENGINEER
    # ========================================================

    "AI Engineer": [
        {
            "title": "Image Classification AI System",
            "description": (
                "Build an AI system that classifies images using "
                "a deep learning model and exposes predictions "
                "through a practical application."
            ),
            "skills": [
                "Python",
                "Deep Learning",
                "TensorFlow/PyTorch",
                "Model Deployment",
                "APIs"
            ],
            "level": "Intermediate"
        },
        {
            "title": "AI-Powered Prediction API",
            "description": (
                "Develop an AI model, wrap it in an API and "
                "create a usable interface around the prediction system."
            ),
            "skills": [
                "Machine Learning",
                "Python",
                "APIs",
                "Model Deployment",
                "Git"
            ],
            "level": "Intermediate → Advanced"
        },
        {
            "title": "Complete AI Application",
            "description": (
                "Build a practical AI-powered application that "
                "combines a trained model, backend API and user interface."
            ),
            "skills": [
                "Deep Learning",
                "TensorFlow/PyTorch",
                "Python",
                "APIs",
                "Model Deployment"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # SOFTWARE ENGINEER
    # ========================================================

    "Software Engineer": [
        {
            "title": "Full-Stack Application",
            "description": (
                "Build a complete application with a frontend, "
                "backend, database and professional Git workflow."
            ),
            "skills": [
                "Programming",
                "APIs",
                "SQL",
                "Git",
                "Testing"
            ],
            "level": "Intermediate"
        },
        {
            "title": "REST API Platform",
            "description": (
                "Design and implement a backend API with "
                "authentication, database integration and testing."
            ),
            "skills": [
                "Programming",
                "APIs",
                "SQL",
                "Testing",
                "Git"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Production-Style Software System",
            "description": (
                "Create a larger software system with structured "
                "architecture, testing, documentation and deployment."
            ),
            "skills": [
                "Data Structures",
                "Algorithms",
                "Programming",
                "Testing",
                "Problem Solving"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # FRONTEND DEVELOPER
    # ========================================================

    "Frontend Developer": [
        {
            "title": "Responsive Portfolio Website",
            "description": (
                "Create a polished responsive website using "
                "semantic HTML, modern CSS and JavaScript."
            ),
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "Responsive Design",
                "UI/UX Fundamentals"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "React Analytics Dashboard",
            "description": (
                "Build an interactive dashboard using React, "
                "reusable components and real API data."
            ),
            "skills": [
                "React",
                "JavaScript",
                "APIs",
                "Git",
                "UI/UX Fundamentals"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Complete Interactive Web Application",
            "description": (
                "Build a production-style frontend application "
                "with reusable components, API integration and "
                "responsive design."
            ),
            "skills": [
                "React",
                "JavaScript",
                "APIs",
                "CSS",
                "Git"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # BACKEND DEVELOPER
    # ========================================================

    "Backend Developer": [
        {
            "title": "REST API",
            "description": (
                "Build a clean REST API with CRUD operations, "
                "database integration and structured endpoints."
            ),
            "skills": [
                "Programming",
                "APIs",
                "SQL",
                "Database Design",
                "Git"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Authentication-Based Web Backend",
            "description": (
                "Create a secure backend system with users, "
                "authentication, authorization and database operations."
            ),
            "skills": [
                "APIs",
                "Authentication",
                "SQL",
                "Database Design",
                "Testing"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Production Backend Platform",
            "description": (
                "Build a scalable backend service with testing, "
                "authentication, database architecture and deployment."
            ),
            "skills": [
                "Programming",
                "APIs",
                "Database Design",
                "Testing",
                "Cloud Deployment"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # FULL STACK DEVELOPER
    # ========================================================

    "Full Stack Developer": [
        {
            "title": "Full-Stack CRUD Application",
            "description": (
                "Build a complete application with frontend, "
                "backend, database and CRUD functionality."
            ),
            "skills": [
                "HTML/CSS",
                "JavaScript",
                "Backend Development",
                "SQL",
                "APIs"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Authentication-Based Web Application",
            "description": (
                "Create a complete web platform with authentication, "
                "database integration and protected application features."
            ),
            "skills": [
                "JavaScript",
                "React",
                "Backend Development",
                "SQL",
                "APIs"
            ],
            "level": "Intermediate → Advanced"
        },
        {
            "title": "Production-Style Full-Stack Platform",
            "description": (
                "Develop and deploy a complete web application "
                "with frontend, backend, database and professional "
                "development workflow."
            ),
            "skills": [
                "React",
                "Backend Development",
                "SQL",
                "APIs",
                "Deployment"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # MOBILE APP DEVELOPER
    # ========================================================

    "Mobile App Developer": [
        {
            "title": "Mobile Productivity Application",
            "description": (
                "Build a polished mobile productivity app with task management, "
                "local data persistence, responsive mobile UI and a clean user experience."
            ),
            "skills": [
                "Programming",
                "Mobile Development",
                "UI/UX Fundamentals",
                "Databases",
                "Git"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "API-Connected Mobile Application",
            "description": (
                "Create a mobile application that consumes a REST API, handles "
                "loading and error states, manages remote data and provides a reliable user experience."
            ),
            "skills": [
                "Programming",
                "Mobile Development",
                "APIs",
                "Git",
                "Testing"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Production Mobile App with Authentication",
            "description": (
                "Build a complete mobile product with authentication, API integration, "
                "secure user flows, persistent data and production-style testing."
            ),
            "skills": [
                "Mobile Development",
                "Programming",
                "APIs",
                "Authentication",
                "Testing"
            ],
            "level": "Intermediate → Advanced"
        }
    ],


    # ========================================================
    # DATA ENGINEER
    # ========================================================

    "Data Engineer": [
        {
            "title": "End-to-End ETL Pipeline",
            "description": (
                "Collect data from multiple sources, transform it "
                "and load it into a structured database."
            ),
            "skills": [
                "Python",
                "SQL",
                "ETL/ELT",
                "Databases",
                "Git"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Data Warehouse Project",
            "description": (
                "Design a data warehouse, create data models and "
                "build reliable pipelines for analytical workloads."
            ),
            "skills": [
                "SQL",
                "Data Warehousing",
                "Databases",
                "ETL/ELT",
                "Cloud Platforms"
            ],
            "level": "Intermediate → Advanced"
        },
        {
            "title": "Scalable Data Processing Pipeline",
            "description": (
                "Build a scalable data pipeline capable of processing "
                "larger datasets using distributed processing concepts."
            ),
            "skills": [
                "Apache Spark",
                "Python",
                "Data Warehousing",
                "Cloud Platforms",
                "ETL/ELT"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # CLOUD ENGINEER
    # ========================================================

    "Cloud Engineer": [
        {
            "title": "Cloud-Hosted Web Application",
            "description": (
                "Deploy an application to the cloud and configure "
                "the required compute, storage and networking components."
            ),
            "skills": [
                "Cloud Computing",
                "AWS/Azure/GCP",
                "Linux",
                "Networking",
                "Git"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Infrastructure as Code Project",
            "description": (
                "Provision cloud infrastructure using Terraform "
                "and document the architecture."
            ),
            "skills": [
                "Cloud Computing",
                "Terraform",
                "AWS/Azure/GCP",
                "Linux",
                "Git"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Scalable Cloud Architecture",
            "description": (
                "Design and deploy a scalable cloud architecture "
                "with networking, containers and infrastructure automation."
            ),
            "skills": [
                "AWS/Azure/GCP",
                "Terraform",
                "Docker",
                "Kubernetes",
                "Networking"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # DEVOPS ENGINEER
    # ========================================================

    "DevOps Engineer": [
        {
            "title": "Dockerized Application",
            "description": (
                "Containerize an application and create a reproducible "
                "development and deployment environment."
            ),
            "skills": [
                "Docker",
                "Linux",
                "Git",
                "Cloud Computing"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "CI/CD Pipeline",
            "description": (
                "Create an automated pipeline that tests, builds "
                "and deploys an application."
            ),
            "skills": [
                "CI/CD",
                "Git",
                "Docker",
                "Testing",
                "Cloud Computing"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Automated Cloud Deployment Platform",
            "description": (
                "Build an automated deployment workflow using "
                "containers, cloud infrastructure and infrastructure as code."
            ),
            "skills": [
                "Kubernetes",
                "Docker",
                "Terraform",
                "CI/CD",
                "Cloud Computing"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # CYBERSECURITY ANALYST
    # ========================================================

    "Cybersecurity Analyst": [
        {
            "title": "Security Monitoring Dashboard",
            "description": (
                "Build a controlled security monitoring environment "
                "that collects and visualizes security events."
            ),
            "skills": [
                "Networking",
                "Cybersecurity Fundamentals",
                "Security Monitoring",
                "Linux",
                "Threat Analysis"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Vulnerability Assessment Lab",
            "description": (
                "Create a legal, controlled lab for identifying "
                "and documenting common security weaknesses."
            ),
            "skills": [
                "Cybersecurity Fundamentals",
                "Networking",
                "Linux",
                "Threat Analysis",
                "Risk Assessment"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Incident Response Simulation",
            "description": (
                "Simulate a security incident in a controlled "
                "environment and document the investigation and response."
            ),
            "skills": [
                "Security Monitoring",
                "Incident Response",
                "Threat Analysis",
                "Linux",
                "Risk Assessment"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # SECURITY ENGINEER
    # ========================================================

    "Security Engineer": [
        {
            "title": "Secure Web Application",
            "description": (
                "Build a web application with authentication, "
                "secure configuration and basic security controls."
            ),
            "skills": [
                "Cybersecurity",
                "Authentication",
                "Networking",
                "Linux",
                "Python"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Cloud Security Architecture",
            "description": (
                "Design security controls for a cloud-based system "
                "including access control, network protection and monitoring."
            ),
            "skills": [
                "Cloud Security",
                "Networking",
                "Identity & Access Management",
                "Security Architecture",
                "Linux"
            ],
            "level": "Intermediate → Advanced"
        },
        {
            "title": "Enterprise Security Architecture",
            "description": (
                "Design an end-to-end security architecture covering "
                "networking, identity, firewalls and security monitoring."
            ),
            "skills": [
                "Security Architecture",
                "Networking",
                "Firewalls",
                "Cloud Security",
                "Cybersecurity"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # DATABASE ADMINISTRATOR
    # ========================================================

    "Database Administrator": [
        {
            "title": "Production Database Setup",
            "description": (
                "Design and configure a relational database with "
                "users, permissions, indexes and monitoring."
            ),
            "skills": [
                "SQL",
                "Database Management",
                "Linux",
                "Troubleshooting"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Database Backup & Recovery System",
            "description": (
                "Implement and test a reliable backup and recovery "
                "strategy for a production-style database."
            ),
            "skills": [
                "SQL",
                "Backup & Recovery",
                "Database Management",
                "Database Security"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Database Performance Optimization",
            "description": (
                "Investigate slow queries and improve database "
                "performance through indexing, query optimization "
                "and monitoring."
            ),
            "skills": [
                "SQL",
                "Performance Tuning",
                "Database Management",
                "Troubleshooting"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # NETWORK ENGINEER
    # ========================================================

    "Network Engineer": [
        {
            "title": "Small Enterprise Network Design",
            "description": (
                "Design a realistic enterprise network with "
                "routing, switching, addressing and security."
            ),
            "skills": [
                "Networking",
                "TCP/IP",
                "Routing & Switching",
                "Network Security"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Network Monitoring System",
            "description": (
                "Create a controlled monitoring environment for "
                "tracking network availability and performance."
            ),
            "skills": [
                "Networking",
                "Network Troubleshooting",
                "Linux",
                "Network Security"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Enterprise Network Troubleshooting Lab",
            "description": (
                "Build realistic network failure scenarios and "
                "systematically diagnose connectivity and security problems."
            ),
            "skills": [
                "Network Troubleshooting",
                "TCP/IP",
                "Routing & Switching",
                "Firewalls",
                "Linux"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # QA ENGINEER
    # ========================================================

    "QA Engineer": [
        {
            "title": "Web Application Testing Suite",
            "description": (
                "Create a structured test suite covering functional, "
                "regression and edge-case testing."
            ),
            "skills": [
                "Software Testing",
                "Problem Solving",
                "API Testing",
                "SQL"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Automated Browser Testing Framework",
            "description": (
                "Build automated browser tests using a modern "
                "automation framework and maintain reusable test cases."
            ),
            "skills": [
                "Test Automation",
                "Selenium",
                "Python/Java",
                "Git",
                "Software Testing"
            ],
            "level": "Intermediate"
        },
        {
            "title": "End-to-End QA Pipeline",
            "description": (
                "Integrate automated testing into a development "
                "workflow with API testing, database checks and CI."
            ),
            "skills": [
                "Test Automation",
                "API Testing",
                "Software Testing",
                "Git",
                "Problem Solving"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # UI/UX DESIGNER
    # ========================================================

    "UI/UX Designer": [
        {
            "title": "Mobile App Design System",
            "description": (
                "Design a complete mobile product including user "
                "flows, wireframes, visual design and reusable components."
            ),
            "skills": [
                "UI Design",
                "UX Design",
                "Figma",
                "Wireframing",
                "Design Systems"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Web Application UX Case Study",
            "description": (
                "Research users, identify problems, create wireframes "
                "and prototype a better product experience."
            ),
            "skills": [
                "UX Design",
                "User Research",
                "Wireframing",
                "Prototyping",
                "Communication"
            ],
            "level": "Intermediate"
        },
        {
            "title": "End-to-End Product Redesign",
            "description": (
                "Redesign an existing digital product from research "
                "through high-fidelity prototype and design system."
            ),
            "skills": [
                "User Research",
                "UX Design",
                "UI Design",
                "Prototyping",
                "Design Systems"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # PRODUCT MANAGER
    # ========================================================

    "Product Manager": [
        {
            "title": "Product Requirements Case Study",
            "description": (
                "Identify a user problem and create a structured "
                "product requirements document."
            ),
            "skills": [
                "Product Strategy",
                "Requirements Gathering",
                "Communication",
                "Prioritization"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Product Roadmap",
            "description": (
                "Develop a product strategy, prioritize features "
                "and create a realistic roadmap based on user needs."
            ),
            "skills": [
                "Product Strategy",
                "Prioritization",
                "Project Management",
                "Market Research",
                "Leadership"
            ],
            "level": "Intermediate"
        },
        {
            "title": "User Research & Feature Prioritization",
            "description": (
                "Conduct structured user research and turn findings "
                "into evidence-based product decisions."
            ),
            "skills": [
                "User Research",
                "Product Analytics",
                "Prioritization",
                "Communication",
                "Product Strategy"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # BUSINESS ANALYST
    # ========================================================

    "Business Analyst": [
        {
            "title": "Business Process Analysis",
            "description": (
                "Analyze an existing business process, identify "
                "problems and propose measurable improvements."
            ),
            "skills": [
                "Business Analysis",
                "Process Modeling",
                "Requirements Gathering",
                "Communication"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Requirements Documentation Case Study",
            "description": (
                "Gather stakeholder requirements and translate them "
                "into structured functional and business requirements."
            ),
            "skills": [
                "Requirements Gathering",
                "Business Analysis",
                "Communication",
                "Problem Solving"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Business Intelligence Analysis",
            "description": (
                "Combine business analysis with data to identify "
                "trends, KPIs and actionable recommendations."
            ),
            "skills": [
                "Data Analysis",
                "SQL",
                "Excel",
                "Business Analysis",
                "Communication"
            ],
            "level": "Advanced"
        }
    ],


    # ========================================================
    # DIGITAL MARKETING SPECIALIST
    # ========================================================

    "Digital Marketing Specialist": [
        {
            "title": "SEO & Content Strategy",
            "description": (
                "Analyze a website, identify search opportunities "
                "and create a structured content strategy."
            ),
            "skills": [
                "SEO",
                "Content Marketing",
                "Copywriting",
                "Marketing Analytics"
            ],
            "level": "Beginner → Intermediate"
        },
        {
            "title": "Digital Marketing Campaign",
            "description": (
                "Plan and analyze a multi-channel marketing campaign "
                "using realistic audience and performance data."
            ),
            "skills": [
                "Digital Marketing",
                "Social Media Marketing",
                "Content Marketing",
                "Marketing Analytics"
            ],
            "level": "Intermediate"
        },
        {
            "title": "Marketing Analytics Dashboard",
            "description": (
                "Build a dashboard that tracks campaign performance, "
                "traffic, conversions and marketing KPIs."
            ),
            "skills": [
                "Google Analytics",
                "Marketing Analytics",
                "Data Analysis",
                "Digital Marketing"
            ],
            "level": "Advanced"
        }
    ]
}


# ============================================================
# PROJECT RECOMMENDATION ENGINE
# ============================================================


def get_project_intelligence(career):
    """Return all project templates available for a career."""

    return PROJECT_INTELLIGENCE.get(career, [])


def _normalize_skill_name(skill_name):
    """Use the central skill normalizer for project matching."""
    return normalize_skill_name(skill_name)


def _skills_match(project_skill, user_skill):
    """Match equivalent skill names using canonical normalization."""
    return skills_match(project_skill, user_skill)

def _skill_lookup(skill_results):
    """Index learner skill results by canonical skill name."""
    lookup = {}

    for skill in skill_results or []:
        canonical = normalize_skill_name(skill.get("skill", ""))
        if canonical:
            lookup[canonical.casefold()] = skill

    return lookup

def calculate_project_relevance(project, skill_results):
    """Score a project according to the learner's normalized skill gaps."""

    skill_lookup = _skill_lookup(skill_results)
    matched_gap_details = []
    seen_skills = set()

    for project_skill in project.get("skills", []):
        canonical = normalize_skill_name(project_skill)
        canonical_key = canonical.casefold()

        if not canonical or canonical_key in seen_skills:
            continue

        seen_skills.add(canonical_key)
        learner_skill = skill_lookup.get(canonical_key)

        if not learner_skill:
            continue

        current = int(learner_skill.get("current_level", 0))
        required = int(learner_skill.get("required_level", 0))
        gap = max(required - current, 0)

        # Projects should earn relevance from actual unmet requirements,
        # not merely from skills the learner already satisfies.
        if gap <= 0:
            continue

        importance = learner_skill.get("importance", "Important")
        weight = 1.5 if str(importance).lower() == "critical" else 1.0
        contribution = gap * 10 * weight

        matched_gap_details.append({
            "skill": learner_skill.get("skill", project_skill),
            "canonical_skill": canonical,
            "current_level": current,
            "required_level": required,
            "gap": gap,
            "importance": importance,
            "contribution": round(contribution, 1),
        })

    matched_gap_details.sort(
        key=lambda item: (
            0 if str(item["importance"]).lower() == "critical" else 1,
            -item["gap"],
            -item["contribution"],
        )
    )

    score = sum(
        item["contribution"]
        for item in matched_gap_details
    )

    coverage_count = len(matched_gap_details)

    if coverage_count >= 4:
        score += 30
    elif coverage_count == 3:
        score += 20
    elif coverage_count == 2:
        score += 10

    critical_count = sum(
        1
        for item in matched_gap_details
        if str(item["importance"]).lower() == "critical"
    )

    score += critical_count * 10

    return round(score, 1), matched_gap_details

def _build_why_recommended(project, matched_gap_details):
    """Create a concise explanation tied to the learner's actual gaps."""

    if not matched_gap_details:
        return (
            "This is a career-relevant project that can strengthen your "
            "practical experience and portfolio."
        )

    critical = [
        item for item in matched_gap_details
        if item["importance"].lower() == "critical"
    ]

    top_skills = [
        item["skill"]
        for item in matched_gap_details[:3]
    ]

    if critical:
        if len(top_skills) == 1:
            return (
                f"This project directly targets your {top_skills[0]} gap, "
                "which is currently a Critical skill for your target career."
            )

        return (
            "This project targets several of your highest-priority gaps, "
            f"including critical skills such as {', '.join(item['skill'] for item in critical[:2])}."
        )

    if len(top_skills) == 1:
        return (
            f"This project gives you practical experience with your "
            f"{top_skills[0]} gap."
        )

    return (
        "This project targets several of your current skill gaps, "
        f"especially {', '.join(top_skills)}."
    )


def _build_gap_summary(matched_gap_details):
    """Create a short human-readable gap summary for the UI."""

    if not matched_gap_details:
        return "Career-relevant project"

    critical_count = sum(
        1
        for item in matched_gap_details
        if item["importance"].lower() == "critical"
    )

    if critical_count and len(matched_gap_details) > 1:
        return (
            f"Targets {len(matched_gap_details)} skill gaps, "
            f"including {critical_count} Critical skill"
            f"{'s' if critical_count != 1 else ''}."
        )

    if critical_count == 1:
        return "Targets 1 Critical skill gap."

    return f"Targets {len(matched_gap_details)} skill gap{'s' if len(matched_gap_details) != 1 else ''}."


def _project_sort_key(project):
    """Sort projects by learner relevance, then by gap coverage."""

    return (
        project.get("relevance_score", 0),
        len(project.get("matched_gap_details", [])),
    )


def recommend_projects(career, skill_results, limit=3):
    """Recommend the most relevant career-specific projects.

    Each returned project includes both general project information and
    learner-specific intelligence:

        - relevance_score
        - matched_skills
        - matched_gap_details
        - gap_coverage
        - why_recommended

    If no project directly matches an unmet skill, career-specific projects
    are still returned so the roadmap never becomes empty merely because of
    a naming mismatch.
    """

    try:
        limit = max(int(limit), 1)
    except (TypeError, ValueError):
        limit = 3

    projects = get_project_intelligence(career)

    if not projects:
        return []

    recommendations = []

    for project in projects:
        relevance_score, matched_gap_details = calculate_project_relevance(
            project,
            skill_results,
        )

        project_copy = project.copy()
        project_copy["skills"] = list(project.get("skills", []))
        project_copy["relevance_score"] = relevance_score
        project_copy["matched_gap_details"] = matched_gap_details
        project_copy["matched_skills"] = [
            item["skill"]
            for item in matched_gap_details
        ]
        project_copy["gap_coverage"] = _build_gap_summary(
            matched_gap_details
        )
        project_copy["why_recommended"] = _build_why_recommended(
            project,
            matched_gap_details,
        )
        project_copy["career_relevance"] = (
            f"Relevant to your {career} career goal."
        )

        recommendations.append(project_copy)

    recommendations.sort(
        key=_project_sort_key,
        reverse=True,
    )

    highest_score = max(
        (project.get("relevance_score", 0) for project in recommendations),
        default=0,
    )

    for project in recommendations:
        project["relevance_percent"] = round(
            (project["relevance_score"] / highest_score) * 100, 1
        ) if highest_score > 0 else 0.0

    # If every project scores zero, keep the original career-specific order.
    # Otherwise return the projects ranked by the learner's actual gaps.
    if all(project["relevance_score"] == 0 for project in recommendations):
        return recommendations[:limit]

    return recommendations[:limit]
