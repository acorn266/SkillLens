from src.skill_normalizer import normalize_skill_name

"""
Skill Intelligence Database

Provides career-independent intelligence for individual skills.

The career database answers:
    "How important is this skill for this career?"

This module answers:
    "What does this skill mean?"
    "What should the learner study?"
    "How can the learner practice it?"
"""

SKILL_INTELLIGENCE = {

    # =========================================================
    # DATA / AI
    # =========================================================

    "Python": {
        "category": "Programming",
        "description": (
            "A general-purpose programming language widely used "
            "for data analysis, automation, backend development "
            "and artificial intelligence."
        ),
        "beginner": [
            "Variables and data types",
            "Conditions and loops",
            "Functions",
            "Lists, dictionaries and sets",
            "Basic file handling"
        ],
        "intermediate": [
            "Object-oriented programming",
            "Exception handling",
            "Modules and packages",
            "Working with APIs",
            "Pandas and NumPy"
        ],
        "advanced": [
            "Software architecture",
            "Performance optimization",
            "Testing and maintainability",
            "Asynchronous programming",
            "Production-grade applications"
        ],
        "practice": (
            "Build a Python project that solves a real problem "
            "instead of only completing tutorials."
        )
    },

    "SQL": {
        "category": "Data",
        "description": (
            "A language used to store, retrieve, transform and "
            "analyze structured data in relational databases."
        ),
        "beginner": [
            "SELECT",
            "WHERE",
            "ORDER BY",
            "GROUP BY",
            "Basic filtering"
        ],
        "intermediate": [
            "JOINs",
            "Subqueries",
            "CASE statements",
            "Common table expressions",
            "Window functions"
        ],
        "advanced": [
            "Query optimization",
            "Database indexing",
            "Data modeling",
            "Complex analytical queries",
            "Production database design"
        ],
        "practice": (
            "Take a real dataset and answer business questions "
            "using progressively more complex SQL queries."
        )
    },

    "Statistics": {
        "category": "Mathematics & Data",
        "description": (
            "The mathematical foundation used to understand data, "
            "uncertainty, relationships and model behavior."
        ),
        "beginner": [
            "Mean, median and mode",
            "Variance and standard deviation",
            "Percentages",
            "Distributions",
            "Basic probability"
        ],
        "intermediate": [
            "Correlation",
            "Regression",
            "Hypothesis testing",
            "Confidence intervals",
            "Sampling"
        ],
        "advanced": [
            "Statistical modeling",
            "Experimental design",
            "Bayesian reasoning",
            "Model evaluation",
            "Uncertainty analysis"
        ],
        "practice": (
            "Analyze a real dataset and explain what the statistical "
            "results actually mean."
        )
    },

    "Machine Learning": {
        "category": "Artificial Intelligence",
        "description": (
            "The field of building systems that learn patterns "
            "from data to make predictions or decisions."
        ),
        "beginner": [
            "Supervised vs unsupervised learning",
            "Training and testing",
            "Features and targets",
            "Basic regression",
            "Basic classification"
        ],
        "intermediate": [
            "Feature engineering",
            "Cross-validation",
            "Random forests",
            "Gradient boosting",
            "Hyperparameter tuning"
        ],
        "advanced": [
            "Model optimization",
            "Model interpretability",
            "Imbalanced learning",
            "Production ML",
            "Experiment tracking"
        ],
        "practice": (
            "Build an end-to-end prediction system using a real dataset."
        )
    },

    "Deep Learning": {
        "category": "Artificial Intelligence",
        "description": (
            "A machine learning approach based on neural networks "
            "with multiple layers."
        ),
        "beginner": [
            "Neural network concepts",
            "Activation functions",
            "Loss functions",
            "Training loops",
            "Basic tensors"
        ],
        "intermediate": [
            "CNNs",
            "Transfer learning",
            "Regularization",
            "Optimization",
            "Model evaluation"
        ],
        "advanced": [
            "Architecture design",
            "Model optimization",
            "Distributed training",
            "Production inference",
            "Advanced neural architectures"
        ],
        "practice": (
            "Build an image or text classification project using "
            "a neural network."
        )
    },

    "TensorFlow/PyTorch": {
        "category": "AI Frameworks",
        "description": (
            "Deep learning frameworks used to build, train and "
            "deploy neural-network-based models."
        ),
        "beginner": [
            "Tensors",
            "Datasets",
            "Models",
            "Loss functions",
            "Training"
        ],
        "intermediate": [
            "Custom neural networks",
            "GPU training",
            "Transfer learning",
            "Model evaluation",
            "Saving and loading models"
        ],
        "advanced": [
            "Production inference",
            "Optimization",
            "Distributed training",
            "Model serving",
            "Deployment pipelines"
        ],
        "practice": (
            "Train and deploy a small deep learning model."
        )
    },

    "Pandas": {
        "category": "Data Analysis",
        "description": (
            "A Python library used for data manipulation, cleaning "
            "and analysis."
        ),
        "beginner": [
            "DataFrames",
            "Reading CSV files",
            "Selecting columns",
            "Filtering rows",
            "Basic statistics"
        ],
        "intermediate": [
            "GroupBy",
            "Merge and join",
            "Missing values",
            "Feature creation",
            "Data transformation"
        ],
        "advanced": [
            "Efficient pipelines",
            "Large dataset optimization",
            "Complex transformations",
            "Reusable preprocessing workflows"
        ],
        "practice": (
            "Clean and analyze a messy real-world CSV dataset."
        )
    },

    "Data Cleaning": {
        "category": "Data Analysis",
        "description": (
            "The process of identifying and correcting inaccurate, "
            "missing, duplicated or inconsistent data."
        ),
        "beginner": [
            "Missing values",
            "Duplicates",
            "Incorrect data types",
            "Basic validation"
        ],
        "intermediate": [
            "Outlier handling",
            "Data standardization",
            "Categorical encoding",
            "Feature transformation"
        ],
        "advanced": [
            "Automated data validation",
            "Data quality pipelines",
            "Large-scale preprocessing",
            "Data integrity monitoring"
        ],
        "practice": (
            "Find a messy dataset and document every cleaning decision."
        )
    },

    "Data Visualization": {
        "category": "Data Analysis",
        "description": (
            "The practice of communicating patterns and insights "
            "through charts, dashboards and visual storytelling."
        ),
        "beginner": [
            "Bar charts",
            "Line charts",
            "Histograms",
            "Scatter plots"
        ],
        "intermediate": [
            "Dashboard design",
            "Interactive charts",
            "Choosing appropriate visualizations",
            "Data storytelling"
        ],
        "advanced": [
            "Executive dashboards",
            "Advanced visual analytics",
            "Insight-driven storytelling",
            "Visualization design systems"
        ],
        "practice": (
            "Create a dashboard that answers five meaningful questions "
            "about a real dataset."
        )
    },

    "Power BI": {
        "category": "Business Intelligence",
        "description": (
            "A business intelligence platform used to transform data "
            "into interactive reports and dashboards."
        ),
        "beginner": [
            "Importing data",
            "Basic charts",
            "Filters",
            "Reports"
        ],
        "intermediate": [
            "Data modeling",
            "Relationships",
            "DAX",
            "Interactive dashboards"
        ],
        "advanced": [
            "Advanced DAX",
            "Performance optimization",
            "Enterprise dashboards",
            "Data governance"
        ],
        "practice": (
            "Build a professional business dashboard from a real dataset."
        )
    },

    "Excel": {
        "category": "Data Analysis",
        "description": (
            "A spreadsheet tool widely used for analysis, reporting "
            "and business decision-making."
        ),
        "beginner": [
            "Formulas",
            "Sorting and filtering",
            "Basic charts",
            "Formatting"
        ],
        "intermediate": [
            "Pivot tables",
            "Lookup functions",
            "Conditional logic",
            "Data cleaning"
        ],
        "advanced": [
            "Advanced formulas",
            "Power Query",
            "Data modeling",
            "Automated reporting"
        ],
        "practice": (
            "Create an interactive business reporting workbook."
        )
    },

    # =========================================================
    # SOFTWARE DEVELOPMENT
    # =========================================================

    "Programming": {
        "category": "Software Development",
        "description": (
            "The ability to design and implement software using "
            "a programming language."
        ),
        "beginner": [
            "Variables",
            "Conditions",
            "Loops",
            "Functions"
        ],
        "intermediate": [
            "Object-oriented programming",
            "Error handling",
            "Modules",
            "Testing"
        ],
        "advanced": [
            "Software architecture",
            "Design patterns",
            "Performance",
            "Maintainability"
        ],
        "practice": (
            "Build a complete application rather than isolated coding exercises."
        )
    },

    "Data Structures": {
        "category": "Computer Science",
        "description": (
            "Methods for organizing and storing data efficiently "
            "inside computer programs."
        ),
        "beginner": [
            "Arrays",
            "Lists",
            "Stacks",
            "Queues"
        ],
        "intermediate": [
            "Linked lists",
            "Hash tables",
            "Trees",
            "Heaps"
        ],
        "advanced": [
            "Graphs",
            "Advanced trees",
            "Complexity trade-offs",
            "Efficient data design"
        ],
        "practice": (
            "Implement common data structures from scratch "
            "and solve problems using them."
        )
    },

    "Algorithms": {
        "category": "Computer Science",
        "description": (
            "Step-by-step procedures used to solve computational problems."
        ),
        "beginner": [
            "Searching",
            "Sorting",
            "Basic recursion"
        ],
        "intermediate": [
            "Binary search",
            "Divide and conquer",
            "Greedy algorithms",
            "Dynamic programming"
        ],
        "advanced": [
            "Graph algorithms",
            "Optimization",
            "Algorithm analysis",
            "Complexity trade-offs"
        ],
        "practice": (
            "Solve programming problems and explain the complexity "
            "of every solution."
        )
    },

    "Git": {
        "category": "Developer Tools",
        "description": (
            "A version control system used to track code changes "
            "and collaborate on software projects."
        ),
        "beginner": [
            "Repositories",
            "Commits",
            "Branches",
            "Push and pull"
        ],
        "intermediate": [
            "Merge conflicts",
            "Pull requests",
            "Branch strategies",
            "Git history"
        ],
        "advanced": [
            "Advanced workflows",
            "Release management",
            "CI/CD integration",
            "Team collaboration"
        ],
        "practice": (
            "Manage every project using Git and maintain a professional repository."
        )
    },

    "APIs": {
        "category": "Backend Development",
        "description": (
            "Interfaces that allow software systems to communicate "
            "with each other."
        ),
        "beginner": [
            "HTTP",
            "GET and POST",
            "JSON",
            "Status codes"
        ],
        "intermediate": [
            "REST APIs",
            "Authentication",
            "API validation",
            "Error handling"
        ],
        "advanced": [
            "API architecture",
            "Rate limiting",
            "Security",
            "Scalability"
        ],
        "practice": (
            "Build an API and connect it to a frontend application."
        )
    },

    "Testing": {
        "category": "Software Quality",
        "description": (
            "The process of verifying that software behaves correctly "
            "and reliably."
        ),
        "beginner": [
            "Test cases",
            "Assertions",
            "Expected vs actual results"
        ],
        "intermediate": [
            "Unit testing",
            "Integration testing",
            "Mocking",
            "Test coverage"
        ],
        "advanced": [
            "Test automation",
            "Continuous testing",
            "Performance testing",
            "Quality strategy"
        ],
        "practice": (
            "Write automated tests for one of your existing projects."
        )
    },

    "Problem Solving": {
        "category": "Professional Skill",
        "description": (
            "The ability to understand problems, break them down "
            "and develop effective solutions."
        ),
        "beginner": [
            "Problem decomposition",
            "Logical reasoning",
            "Simple debugging"
        ],
        "intermediate": [
            "Root cause analysis",
            "Trade-offs",
            "Structured decision making"
        ],
        "advanced": [
            "Complex system reasoning",
            "Optimization",
            "Strategic technical decisions"
        ],
        "practice": (
            "Solve real problems and document how you reached your solution."
        )
    },

    # =========================================================
    # WEB
    # =========================================================

    "HTML": {
        "category": "Frontend Development",
        "description": (
            "The markup language used to structure content on the web."
        ),
        "beginner": [
            "Semantic elements",
            "Forms",
            "Links",
            "Images"
        ],
        "intermediate": [
            "Accessible markup",
            "SEO-friendly structure",
            "Complex forms",
            "Reusable structures"
        ],
        "advanced": [
            "Web accessibility",
            "Performance-aware markup",
            "Semantic architecture"
        ],
        "practice": (
            "Build a complete responsive multi-page website."
        )
    },

    "CSS": {
        "category": "Frontend Development",
        "description": (
            "The styling language used to control the appearance "
            "and layout of websites."
        ),
        "beginner": [
            "Selectors",
            "Box model",
            "Colors",
            "Typography"
        ],
        "intermediate": [
            "Flexbox",
            "Grid",
            "Responsive design",
            "Animations"
        ],
        "advanced": [
            "Design systems",
            "Advanced responsive layouts",
            "Performance",
            "Maintainable CSS architecture"
        ],
        "practice": (
            "Recreate a professional website from a design reference."
        )
    },

    "JavaScript": {
        "category": "Frontend Development",
        "description": (
            "A programming language used to create interactive "
            "and dynamic web applications."
        ),
        "beginner": [
            "Variables",
            "Functions",
            "Arrays",
            "Objects"
        ],
        "intermediate": [
            "DOM manipulation",
            "Async programming",
            "Fetch API",
            "Modules"
        ],
        "advanced": [
            "Application architecture",
            "Performance",
            "State management",
            "Advanced asynchronous programming"
        ],
        "practice": (
            "Build an interactive web application using a public API."
        )
    },

    "React": {
        "category": "Frontend Development",
        "description": (
            "A JavaScript library used to build component-based user interfaces."
        ),
        "beginner": [
            "Components",
            "Props",
            "JSX",
            "Basic state"
        ],
        "intermediate": [
            "Hooks",
            "Routing",
            "API integration",
            "Reusable components"
        ],
        "advanced": [
            "Application architecture",
            "Performance optimization",
            "Advanced state management",
            "Production deployment"
        ],
        "practice": (
            "Build a complete dashboard or SaaS-style frontend."
        )
    },

    # =========================================================
    # CLOUD / DEVOPS
    # =========================================================

    "Linux": {
        "category": "Systems",
        "description": (
            "An operating system environment widely used for servers, "
            "cloud infrastructure and development."
        ),
        "beginner": [
            "Terminal commands",
            "Files and directories",
            "Permissions",
            "Processes"
        ],
        "intermediate": [
            "Shell scripting",
            "Networking commands",
            "Services",
            "Package management"
        ],
        "advanced": [
            "System administration",
            "Performance",
            "Security hardening",
            "Automation"
        ],
        "practice": (
            "Set up a Linux environment and administer a small server."
        )
    },

    "Docker": {
        "category": "DevOps",
        "description": (
            "A platform used to package applications and their "
            "dependencies into portable containers."
        ),
        "beginner": [
            "Images",
            "Containers",
            "Docker commands",
            "Dockerfiles"
        ],
        "intermediate": [
            "Docker Compose",
            "Networking",
            "Volumes",
            "Environment variables"
        ],
        "advanced": [
            "Production containerization",
            "Security",
            "Optimization",
            "Container orchestration"
        ],
        "practice": (
            "Containerize one of your applications and run it locally."
        )
    },

    "Kubernetes": {
        "category": "Cloud & DevOps",
        "description": (
            "A platform for deploying, scaling and managing containerized applications."
        ),
        "beginner": [
            "Pods",
            "Deployments",
            "Services",
            "Namespaces"
        ],
        "intermediate": [
            "ConfigMaps",
            "Secrets",
            "Ingress",
            "Scaling"
        ],
        "advanced": [
            "Cluster architecture",
            "Production operations",
            "Security",
            "Observability"
        ],
        "practice": (
            "Deploy a containerized application to a Kubernetes cluster."
        )
    },

    "Terraform": {
        "category": "Infrastructure as Code",
        "description": (
            "A tool used to define and manage infrastructure through code."
        ),
        "beginner": [
            "Providers",
            "Resources",
            "Variables",
            "Outputs"
        ],
        "intermediate": [
            "Modules",
            "State",
            "Remote state",
            "Environment management"
        ],
        "advanced": [
            "Infrastructure architecture",
            "Reusable modules",
            "Security",
            "Production workflows"
        ],
        "practice": (
            "Use Terraform to provision a small cloud environment."
        )
    },

    "Cloud Computing": {
        "category": "Cloud",
        "description": (
            "The use of remote computing, storage and networking "
            "resources delivered through cloud platforms."
        ),
        "beginner": [
            "Cloud concepts",
            "Virtual machines",
            "Storage",
            "Networking"
        ],
        "intermediate": [
            "Identity",
            "Databases",
            "Load balancing",
            "Monitoring"
        ],
        "advanced": [
            "Cloud architecture",
            "Scalability",
            "Reliability",
            "Cost optimization"
        ],
        "practice": (
            "Deploy a small application to a cloud platform."
        )
    },

    "AWS/Azure/GCP": {
        "category": "Cloud Platforms",
        "description": (
            "Major cloud platforms providing compute, storage, networking "
            "and managed application services."
        ),
        "beginner": [
            "Compute",
            "Storage",
            "Networking",
            "Identity"
        ],
        "intermediate": [
            "Managed databases",
            "Load balancing",
            "Monitoring",
            "Serverless services"
        ],
        "advanced": [
            "Cloud architecture",
            "High availability",
            "Security",
            "Cost optimization"
        ],
        "practice": (
            "Deploy a real application using one major cloud provider."
        )
    },

    "CI/CD": {
        "category": "DevOps",
        "description": (
            "Practices and automation pipelines used to continuously "
            "test, build and deploy software."
        ),
        "beginner": [
            "Build pipelines",
            "Automated tests",
            "Deployment basics"
        ],
        "intermediate": [
            "GitHub Actions",
            "Pipeline environments",
            "Deployment automation"
        ],
        "advanced": [
            "Production pipelines",
            "Security scanning",
            "Release strategies",
            "Deployment reliability"
        ],
        "practice": (
            "Create a pipeline that tests and deploys one of your projects."
        )
    },

    "Monitoring": {
        "category": "DevOps",
        "description": (
            "The practice of observing application and infrastructure "
            "health through metrics, logs and alerts."
        ),
        "beginner": [
            "Logs",
            "Metrics",
            "Basic alerts"
        ],
        "intermediate": [
            "Dashboards",
            "Service monitoring",
            "Alert rules"
        ],
        "advanced": [
            "Observability",
            "Distributed tracing",
            "Reliability metrics",
            "Incident analysis"
        ],
        "practice": (
            "Monitor an application and create alerts for failures."
        )
    },

    # =========================================================
    # CYBERSECURITY
    # =========================================================

    "Networking": {
        "category": "Networking",
        "description": (
            "Understanding how computers and systems communicate "
            "over networks."
        ),
        "beginner": [
            "IP addresses",
            "Ports",
            "DNS",
            "Basic protocols"
        ],
        "intermediate": [
            "Routing",
            "Subnets",
            "TCP/IP",
            "Network troubleshooting"
        ],
        "advanced": [
            "Network architecture",
            "Network security",
            "Performance",
            "Enterprise networking"
        ],
        "practice": (
            "Design and document a small network and troubleshoot "
            "intentional connectivity problems."
        )
    },

    "Cybersecurity Fundamentals": {
        "category": "Cybersecurity",
        "description": (
            "Core concepts required to protect systems, networks "
            "and information from security threats."
        ),
        "beginner": [
            "CIA triad",
            "Threats",
            "Vulnerabilities",
            "Authentication"
        ],
        "intermediate": [
            "Risk management",
            "Security controls",
            "Attack techniques",
            "Defensive strategies"
        ],
        "advanced": [
            "Security architecture",
            "Threat modeling",
            "Security strategy",
            "Incident management"
        ],
        "practice": (
            "Perform a security assessment of a deliberately vulnerable "
            "practice environment."
        )
    },

    "Security Monitoring": {
        "category": "Cybersecurity",
        "description": (
            "The process of monitoring systems and networks for "
            "suspicious or malicious activity."
        ),
        "beginner": [
            "Logs",
            "Events",
            "Alerts",
            "Basic indicators"
        ],
        "intermediate": [
            "SIEM concepts",
            "Event correlation",
            "Detection rules",
            "Investigation"
        ],
        "advanced": [
            "Detection engineering",
            "Threat hunting",
            "Advanced correlation",
            "Security operations"
        ],
        "practice": (
            "Analyze sample security logs and identify suspicious activity."
        )
    },

    "Incident Response": {
        "category": "Cybersecurity",
        "description": (
            "The structured process used to identify, contain and "
            "recover from security incidents."
        ),
        "beginner": [
            "Incident lifecycle",
            "Identification",
            "Containment",
            "Recovery"
        ],
        "intermediate": [
            "Evidence collection",
            "Timeline analysis",
            "Incident documentation"
        ],
        "advanced": [
            "Incident coordination",
            "Forensics",
            "Advanced investigation",
            "Post-incident improvement"
        ],
        "practice": (
            "Work through a simulated security incident and write an "
            "incident response report."
        )
    },

    "Firewalls": {
        "category": "Network Security",
        "description": (
            "Security controls that regulate network traffic according "
            "to defined rules."
        ),
        "beginner": [
            "Ports",
            "Protocols",
            "Allow/deny rules"
        ],
        "intermediate": [
            "Network segmentation",
            "NAT",
            "Firewall policies"
        ],
        "advanced": [
            "Enterprise firewall architecture",
            "Advanced filtering",
            "Security monitoring"
        ],
        "practice": (
            "Create firewall rules in a legal practice environment "
            "and test permitted and blocked traffic."
        )
    },

    # =========================================================
    # DESIGN / PRODUCT
    # =========================================================

    "UI Design": {
        "category": "Design",
        "description": (
            "The design of visual interfaces that are clear, consistent "
            "and usable."
        ),
        "beginner": [
            "Typography",
            "Color",
            "Spacing",
            "Layout"
        ],
        "intermediate": [
            "Visual hierarchy",
            "Component design",
            "Responsive layouts"
        ],
        "advanced": [
            "Design systems",
            "Accessibility",
            "Complex product interfaces"
        ],
        "practice": (
            "Redesign an existing application interface and explain your decisions."
        )
    },

    "UX Design": {
        "category": "User Experience",
        "description": (
            "The process of designing products around users' needs, "
            "behaviors and goals."
        ),
        "beginner": [
            "User needs",
            "Personas",
            "User journeys"
        ],
        "intermediate": [
            "Information architecture",
            "Usability",
            "Interaction design"
        ],
        "advanced": [
            "Complex product flows",
            "UX strategy",
            "Design research"
        ],
        "practice": (
            "Choose a real-world problem and design the complete user journey."
        )
    },

    "Figma": {
        "category": "Design Tool",
        "description": (
            "A collaborative design tool commonly used for interface "
            "design, wireframing and prototyping."
        ),
        "beginner": [
            "Frames",
            "Shapes",
            "Text",
            "Components"
        ],
        "intermediate": [
            "Auto layout",
            "Variants",
            "Prototypes",
            "Design systems"
        ],
        "advanced": [
            "Complex component systems",
            "Advanced prototyping",
            "Design handoff"
        ],
        "practice": (
            "Design a complete multi-screen application in Figma."
        )
    },

    "User Research": {
        "category": "UX / Product",
        "description": (
            "The process of understanding users, their problems, "
            "behaviors and needs."
        ),
        "beginner": [
            "Interviews",
            "Surveys",
            "Observation"
        ],
        "intermediate": [
            "Usability testing",
            "Research synthesis",
            "User personas"
        ],
        "advanced": [
            "Research strategy",
            "Mixed-method research",
            "Evidence-driven product decisions"
        ],
        "practice": (
            "Interview several users about a real problem and summarize "
            "the patterns you discover."
        )
    },

    "Communication": {
        "category": "Professional Skill",
        "description": (
            "The ability to clearly explain ideas, decisions, findings "
            "and recommendations to different audiences."
        ),
        "beginner": [
            "Clear writing",
            "Structured explanations",
            "Active listening"
        ],
        "intermediate": [
            "Presentations",
            "Technical communication",
            "Stakeholder communication"
        ],
        "advanced": [
            "Executive communication",
            "Persuasion",
            "Complex technical storytelling"
        ],
        "practice": (
            "Present one of your projects and explain the problem, "
            "solution, decisions and results."
        )
    },

    # =========================================================
    # BUSINESS
    # =========================================================

    "Business Analysis": {
        "category": "Business",
        "description": (
            "The practice of understanding business problems and "
            "translating them into actionable requirements and solutions."
        ),
        "beginner": [
            "Business problems",
            "Stakeholders",
            "Basic process analysis"
        ],
        "intermediate": [
            "Requirements",
            "Process improvement",
            "Data analysis"
        ],
        "advanced": [
            "Strategic analysis",
            "Complex business transformation",
            "Decision support"
        ],
        "practice": (
            "Analyze a real business process and propose measurable improvements."
        )
    },

    "Requirements Gathering": {
        "category": "Business Analysis",
        "description": (
            "The process of discovering, documenting and validating "
            "what a product or system needs to accomplish."
        ),
        "beginner": [
            "Stakeholder identification",
            "Interviews",
            "Basic requirements"
        ],
        "intermediate": [
            "User stories",
            "Acceptance criteria",
            "Requirement prioritization"
        ],
        "advanced": [
            "Complex stakeholder management",
            "Requirement validation",
            "Change management"
        ],
        "practice": (
            "Create a requirements document for a fictional software product."
        )
    },

    "Product Strategy": {
        "category": "Product Management",
        "description": (
            "The process of defining a product's direction, target users "
            "and path toward measurable business outcomes."
        ),
        "beginner": [
            "Product goals",
            "Target users",
            "Value proposition"
        ],
        "intermediate": [
            "Roadmaps",
            "Product metrics",
            "Competitive analysis"
        ],
        "advanced": [
            "Portfolio strategy",
            "Growth strategy",
            "Long-term product planning"
        ],
        "practice": (
            "Create a product strategy and roadmap for a real-world problem."
        )
    },

    "Project Management": {
        "category": "Management",
        "description": (
            "The process of planning, coordinating and delivering "
            "projects within defined constraints."
        ),
        "beginner": [
            "Tasks",
            "Milestones",
            "Deadlines"
        ],
        "intermediate": [
            "Risk management",
            "Agile methods",
            "Stakeholder management"
        ],
        "advanced": [
            "Portfolio management",
            "Complex dependencies",
            "Strategic delivery"
        ],
        "practice": (
            "Plan and manage one of your own software or data projects "
            "using milestones and deadlines."
        )
    },

    # =========================================================
    # MARKETING
    # =========================================================

    "Digital Marketing": {
        "category": "Marketing",
        "description": (
            "The use of digital channels and data to attract, engage "
            "and convert audiences."
        ),
        "beginner": [
            "Digital channels",
            "Audience research",
            "Basic campaigns"
        ],
        "intermediate": [
            "Campaign optimization",
            "Conversion funnels",
            "Analytics"
        ],
        "advanced": [
            "Growth strategy",
            "Attribution",
            "Performance optimization"
        ],
        "practice": (
            "Create and analyze a mock digital marketing campaign."
        )
    },

    "SEO": {
        "category": "Digital Marketing",
        "description": (
            "The practice of improving website visibility in search engines."
        ),
        "beginner": [
            "Keywords",
            "Search intent",
            "On-page SEO"
        ],
        "intermediate": [
            "Technical SEO",
            "Content strategy",
            "Backlinks"
        ],
        "advanced": [
            "SEO strategy",
            "Large-site optimization",
            "Search performance analysis"
        ],
        "practice": (
            "Perform an SEO audit of a website and create an improvement plan."
        )
    },

    "Content Marketing": {
        "category": "Marketing",
        "description": (
            "Creating useful content to attract, educate and retain a target audience."
        ),
        "beginner": [
            "Content types",
            "Audience research",
            "Content planning"
        ],
        "intermediate": [
            "Content strategy",
            "Distribution",
            "Performance analysis"
        ],
        "advanced": [
            "Content systems",
            "Growth strategy",
            "Content optimization"
        ],
        "practice": (
            "Build a one-month content strategy for a fictional brand."
        )
    },

    "Copywriting": {
        "category": "Marketing",
        "description": (
            "Writing persuasive text designed to communicate value "
            "and encourage a specific action."
        ),
        "beginner": [
            "Headlines",
            "Value propositions",
            "Calls to action"
        ],
        "intermediate": [
            "Landing pages",
            "Email copy",
            "Conversion-focused writing"
        ],
        "advanced": [
            "Brand voice",
            "Conversion optimization",
            "Strategic messaging"
        ],
        "practice": (
            "Write a landing page and several advertising variations "
            "for the same product."
        )
    },

    # =========================================================
    # DATABASE / GENERAL
    # =========================================================

    "Database Management": {
        "category": "Database",
        "description": (
            "The administration and organization of database systems "
            "to ensure availability, performance and reliability."
        ),
        "beginner": [
            "Tables",
            "Relationships",
            "CRUD operations"
        ],
        "intermediate": [
            "Indexes",
            "Transactions",
            "Permissions"
        ],
        "advanced": [
            "Database architecture",
            "High availability",
            "Performance optimization"
        ],
        "practice": (
            "Design and administer a relational database for a complete application."
        )
    },

    "Database Security": {
        "category": "Database Security",
        "description": (
            "Protecting databases from unauthorized access, data loss "
            "and security threats."
        ),
        "beginner": [
            "Users",
            "Roles",
            "Permissions"
        ],
        "intermediate": [
            "Access controls",
            "Encryption",
            "Auditing"
        ],
        "advanced": [
            "Security architecture",
            "Compliance",
            "Advanced auditing"
        ],
        "practice": (
            "Secure a sample database using roles, permissions and auditing."
        )
    },

    "Backup & Recovery": {
        "category": "Database Administration",
        "description": (
            "Techniques used to protect data and restore systems "
            "after failures or data loss."
        ),
        "beginner": [
            "Backup types",
            "Restore basics",
            "Backup schedules"
        ],
        "intermediate": [
            "Recovery procedures",
            "Point-in-time recovery",
            "Backup validation"
        ],
        "advanced": [
            "Disaster recovery",
            "High availability",
            "Recovery planning"
        ],
        "practice": (
            "Create and test a complete backup and restoration procedure."
        )
    },

    "Troubleshooting": {
        "category": "Technical Skill",
        "description": (
            "The ability to systematically diagnose and resolve technical problems."
        ),
        "beginner": [
            "Problem identification",
            "Basic logs",
            "Reproduction"
        ],
        "intermediate": [
            "Root cause analysis",
            "Debugging",
            "Systematic investigation"
        ],
        "advanced": [
            "Complex incidents",
            "Performance diagnosis",
            "Cross-system troubleshooting"
        ],
        "practice": (
            "Intentionally introduce problems into a project and diagnose them."
        )
    }
}


def get_skill_intelligence(skill_name):
    """
    Return intelligence information for a skill.

    Uses a generic fallback when a skill has not yet been added
    to the intelligence database.
    """

    canonical_name = normalize_skill_name(skill_name)

    if canonical_name in SKILL_INTELLIGENCE:
        return SKILL_INTELLIGENCE[canonical_name]

    # Case-insensitive fallback for database entries whose capitalization
    # differs from the canonical skill name.
    for known_skill, intelligence in SKILL_INTELLIGENCE.items():
        if known_skill.casefold() == canonical_name.casefold():
            return intelligence

    return {
        "category": "Professional Skill",
        "description": (
            f"{skill_name} is a skill associated with the selected career."
        ),
        "beginner": [
            f"Understand the fundamentals of {skill_name}",
            f"Learn the core terminology of {skill_name}",
            f"Complete beginner exercises in {skill_name}"
        ],
        "intermediate": [
            f"Apply {skill_name} to practical problems",
            f"Build a project involving {skill_name}",
            f"Learn commonly used professional workflows"
        ],
        "advanced": [
            f"Work on advanced {skill_name} problems",
            f"Build production-quality solutions",
            f"Develop professional-level expertise"
        ],
        "practice": (
            f"Build a practical project that demonstrates your "
            f"ability to use {skill_name}."
        )
    }