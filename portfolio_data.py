# data/portfolio_data.py

PERSONAL_INFO = {
    "name": "Mohammed Danish Khan",
    "headline": "Data Scientist | Machine Learning Engineer | AI Specialist",
    "location": "Navi Mumbai, India",
    "email": "Danish.k1709@gmail.com",
    "phone": "+91 8169387986",
    "github": "https://github.com/danishkhan-codes",
    "linkedin": "https://www.linkedin.com/in/mohammed-danish-khan-071899284/",
    "intro": (
        "Computer Engineering graduate with a strong foundation in Data Analytics, Python, SQL, "
        "Power BI, and Machine Learning. Experienced in data cleaning, exploratory data analysis (EDA), "
        "dashboard development, data visualization, and building end-to-end data-driven projects."
    )
}

STATS = [
    {"value": "2+", "label": "ML Projects", "icon": "🔬"},
    {"value": "12+", "label": "Core Tools", "icon": "⚙️"},
    {"value": "8.0", "label": "B.E. CGPA", "icon": "🎓"},
    {"value": "1 yr", "label": "Leadership", "icon": "👔"}
]

ABOUT_ME = {
    "university": "Smt. Indira Gandhi College of Engineering",
    "affiliation": "University of Mumbai",
    "cgpa": "8.0 / 10.0",
    "duration": "Nov 2022 – May 2026",
    "specialization": "Computer Science & Engineering (Artificial Intelligence & Machine Learning)",
    "summary": (
        "Computer Engineering graduate with a strong foundation in Data Analytics, Python, SQL, Power BI, "
        "and Machine Learning. Experienced in data cleaning, exploratory data analysis (EDA), dashboard "
        "development, data visualization, and building end-to-end data-driven projects."
    ),
    "strengths": [
        "Statistical Modeling",
        "Predictive Analytics",
        "Machine Learning",
        "Data Engineering",
        "Database Architecture",
        "Dashboard Design",
        "Leadership & Teamwork",
        "Technical Communication"
    ]
}

SKILLS = {
    "Languages & Databases": [
        {"name": "Python", "level": 92, "icon": "🐍"},
        {"name": "SQL", "level": 88, "icon": "🗄️"},
        {"name": "MySQL", "level": 85, "icon": "🐬"},
        {"name": "PostgreSQL", "level": 80, "icon": "🐘"}
    ],
    "Libraries & Frameworks": [
        {"name": "Pandas", "level": 92, "icon": "🐼"},
        {"name": "NumPy", "level": 88, "icon": "🔢"},
        {"name": "SciPy", "level": 80, "icon": "🔬"},
        {"name": "Scikit-Learn", "level": 88, "icon": "🤖"},
        {"name": "Streamlit", "level": 90, "icon": "🎈"},
        {"name": "Snowflake", "level": 75, "icon": "❄️"}
    ],
    "Data Visualization": [
        {"name": "Power BI (DAX)", "level": 85, "icon": "📊"},
        {"name": "Tableau", "level": 80, "icon": "🎯"},
        {"name": "Matplotlib", "level": 85, "icon": "📉"},
        {"name": "Seaborn", "level": 85, "icon": "📈"}
    ],
    "Developer Tools & Cloud": [
        {"name": "Git", "level": 85, "icon": "🌿"},
        {"name": "GitHub", "level": 88, "icon": "🐙"},
        {"name": "Excel (Pivot, Macros)", "level": 85, "icon": "📅"}
    ]
}

PROJECTS = [
    {
        "id": "cricverse",
        "title": "CricVerse – AI-Powered Cricket Analytics Platform",
        "technologies": ["Python", "SQL", "Streamlit", "Pandas", "NumPy", "TensorFlow", "Matplotlib", "XGBoost", "Scikit-Learn"],
        "description": "Developed an AI-powered cricket analytics platform to predict match outcomes, analyze player performance, and generate data-driven insights using Python and machine learning.",
        "features": [
            "Performed data cleaning, preprocessing, exploratory data analysis (EDA), and feature engineering on historical cricket datasets to build predictive models.",
            "Designed interactive dashboards and a Streamlit web application to visualize team statistics, player performance, and match analytics."
        ],
        "image": "assets/project_images/cricverse.jpg",
        "metrics_label": "Model Performance",
        "metrics_data": {
            "Match Outcome Accuracy": 84,
            "Players Modeled": 1200,
            "EDA Plots Generated": 45
        }
    },
    {
        "id": "expense_tracker",
        "title": "Expense Tracker with Data Analysis",
        "technologies": ["Python", "SQL", "Streamlit", "Pandas", "NumPy", "Matplotlib"],
        "description": "Developed a financial analytics application to clean transactional records, analyze personal spending habits, and forecast expense trends.",
        "features": [
            "Performed data cleaning and analysis using Pandas to identify spending patterns and generate meaningful financial insights.",
            "Created interactive visualizations with Matplotlib to present expense trends and category-wise spending analysis."
        ],
        "image": "assets/project_images/expense_tracker.jpg",
        "metrics_label": "Data Processing",
        "metrics_data": {
            "Monthly Expenses Categorized": 500,
            "Savings Optimization Rate": 15,
            "Dashboard Filters": 12
        }
    }
]

EXPERIENCE = [
    {
        "role": "Technical Secretary",
        "organization": "Student Council",
        "location": "Navi Mumbai, India",
        "duration": "August 2025 – July 2026",
        "institution": "Smt. Indira Gandhi College of Engineering, Mumbai University",
        "responsibilities": [
            "Led the planning and execution of technical events, including hackathons, coding competitions, workshops, and seminars.",
            "Coordinated an inter-college technical fest by managing event planning, logistics, scheduling, and cross-functional teams.",
            "Collaborated with faculty, sponsors, judges, and industry professionals to organize technical events and hackathons.",
            "Managed budgets, registrations, event timelines, and resource allocation to ensure successful event execution.",
            "Led a team of student volunteers, demonstrating leadership, communication, and problem-solving skills."
        ],
        "skills": ["Event Coordination", "Budget Planning", "Leadership", "Problem Solving"]
    },
    {
        "role": "Technical Core Team Member",
        "organization": "Google Developer Students Club (GDSC)",
        "location": "Navi Mumbai, India",
        "duration": "August 2023 – July 2024",
        "institution": "GDSC Chapter",
        "responsibilities": [
            "Managed collaborative Git/GitHub workflows and contributed to technical event execution.",
            "Conducted workshops on open-source contribution, Git workflows, and software engineering best practices."
        ],
        "skills": ["Git & GitHub", "Technical Event execution", "Open-Source Support"]
    }
]

EDUCATION = [
    {
        "degree": "B.E. Computer Science & Engineering",
        "specialization": "Artificial Intelligence & Machine Learning",
        "duration": "Nov 2022 – May 2026",
        "location": "Navi Mumbai, India",
        "institution": "Smt. Indira Gandhi College of Engineering, University of Mumbai",
        "cgpa": "8.0 / 10.0",
        "bullets": []
    }
]

