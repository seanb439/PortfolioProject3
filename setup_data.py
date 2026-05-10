import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio.models import Project, Skill, Experience
from datetime import datetime, date

# Create superuser
username = 'admin'
password = 'admin123'
email = 'admin@portfolio.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully!")
    print(f"Login at http://localhost:8000/admin with username: {username}, password: {password}")
else:
    print(f"Superuser '{username}' already exists!")

# Clear existing projects (optional)
# Project.objects.all().delete()

# Add sample projects
projects_data = [
    {
        'title': 'Portfolio Website (Django)',
        'summary': 'A professional portfolio website built with Django, featuring projects, skills, resume, and an integrated chatbot.',
        'description': 'A full-stack Django web application showcasing projects, skills, and professional experience. Includes responsive design, project filtering, and an AI chatbot widget.',
        'category': 'Web Development',
        'business_problem': 'Need a professional, modern portfolio website to showcase projects and skills to potential employers and clients.',
        'tools_used': 'Django, Python, Bootstrap, HTML/CSS, JavaScript',
        'key_features': 'Project showcase, Skills listing, Resume display, Contact information, Embedded chatbot, Responsive design',
        'role_contribution': 'Full-stack developer - designed and implemented the entire application from database models to frontend templates.',
        'challenge': 'Creating a responsive, visually appealing design while ensuring all functionality works smoothly across different devices.',
        'lessons_learned': 'Gained experience with Django MTV architecture, template inheritance, static file management, and API integration.',
    },
    {
        'title': 'Chatbot Project',
        'summary': 'An intelligent chatbot system that can answer questions about portfolio content and provide information to visitors.',
        'description': 'An AI-powered chatbot that helps website visitors by providing information about projects, skills, and contact details through natural conversation.',
        'category': 'AI/Machine Learning',
        'business_problem': 'Website visitors need quick access to information without having to browse entire pages.',
        'tools_used': 'Python, Natural Language Processing, Django',
        'key_features': 'Keyword-based responses, Learning capabilities, Integration with portfolio system',
        'role_contribution': 'Developed the chatbot logic and integrated it into the Django application.',
        'challenge': 'Implementing natural language understanding while keeping the system efficient and responsive.',
        'lessons_learned': 'Learned about NLP basics, chatbot architecture, and user interaction design.',
    },
    {
        'title': 'n8n Agent Workflow Project',
        'summary': 'An automation workflow built with n8n that streamlines data processing and integration between multiple applications.',
        'description': 'An intelligent workflow automation system using n8n to connect and automate processes between different applications.',
        'category': 'Automation',
        'business_problem': 'Repetitive manual processes were consuming significant time and were prone to errors.',
        'tools_used': 'n8n, API Integration, Workflow Automation',
        'key_features': 'Multi-step automation, Error handling, Data transformation',
        'role_contribution': 'Designed and built the workflow architecture, configured integrations.',
        'challenge': 'Understanding complex API documentation and building reliable error handling.',
        'lessons_learned': 'Mastered n8n platform, API integration patterns, and workflow optimization.',
    },
    {
        'title': 'LangChain Agent Project',
        'summary': 'An advanced AI agent system using LangChain that leverages language models for intelligent task automation.',
        'description': 'A sophisticated agent system built with LangChain that uses language models to autonomously handle complex tasks.',
        'category': 'AI/Machine Learning',
        'business_problem': 'Need for intelligent systems that can understand context and make decisions autonomously.',
        'tools_used': 'LangChain, Python, OpenAI/Language Models',
        'key_features': 'Intelligent decision making, Context awareness, Tool integration',
        'role_contribution': 'Developed the agent logic and trained the system on domain-specific tasks.',
        'challenge': 'Fine-tuning agent behavior and ensuring consistent, accurate responses.',
        'lessons_learned': 'Deep understanding of LangChain framework, prompt engineering, and agent architectures.',
    },
    {
        'title': 'Data Analytics Dashboard',
        'summary': 'An interactive Tableau dashboard providing business intelligence and KPI tracking for data-driven decision making.',
        'description': 'A comprehensive analytics dashboard built in Tableau that visualizes key business metrics and enables data exploration.',
        'category': 'Data Analytics',
        'business_problem': 'Stakeholders needed visibility into key metrics and trends for informed business decisions.',
        'tools_used': 'Tableau, SQL, Python, Excel',
        'key_features': 'Real-time KPI tracking, Interactive filters, Trend analysis, Drill-down capabilities',
        'role_contribution': 'Designed the dashboard layout, created visualizations, connected data sources, and trained users.',
        'challenge': 'Balancing visual appeal with functionality and handling large datasets efficiently.',
        'lessons_learned': 'Advanced Tableau techniques, data storytelling, and stakeholder communication.',
    },
    {
        'title': 'Machine Learning Model',
        'summary': 'A predictive machine learning model using scikit-learn for classification and pattern recognition.',
        'description': 'A machine learning model developed with scikit-learn that achieves high accuracy in predictive tasks.',
        'category': 'Machine Learning',
        'business_problem': 'Need to predict outcomes and identify patterns in large datasets.',
        'tools_used': 'Python, scikit-learn, Pandas, NumPy',
        'key_features': 'Feature engineering, Model optimization, Cross-validation, Performance metrics',
        'role_contribution': 'Data preprocessing, feature engineering, model development, and evaluation.',
        'challenge': 'Handling imbalanced data and optimizing model performance.',
        'lessons_learned': 'Machine learning workflow, hyperparameter tuning, and model evaluation techniques.',
    }
]

for project_data in projects_data:
    if not Project.objects.filter(title=project_data['title']).exists():
        Project.objects.create(**project_data)
        print(f"Project '{project_data['title']}' created!")
    else:
        print(f"Project '{project_data['title']}' already exists!")

# Add skills
skills_data = [
    # Programming & Data Tools
    ('Python', 'Programming & Data Tools', 'Advanced'),
    ('SQL', 'Programming & Data Tools', 'Advanced'),
    ('R', 'Programming & Data Tools', 'Advanced'),
    ('Excel', 'Programming & Data Tools', 'Expert'),
    ('Tableau', 'Programming & Data Tools', 'Advanced'),
    # Analytics
    ('Data Cleaning', 'Analytics', 'Expert'),
    ('Exploratory Data Analysis', 'Analytics', 'Advanced'),
    ('Statistical Modeling', 'Analytics', 'Advanced'),
    ('Predictive Modeling', 'Analytics', 'Intermediate'),
    ('Forecasting', 'Analytics', 'Intermediate'),
    # Visualization
    ('Dashboard Design', 'Visualization', 'Advanced'),
    ('ggplot2', 'Visualization', 'Advanced'),
    ('Power BI', 'Visualization', 'Intermediate'),
    # Cloud & Tools
    ('AWS Cloud', 'Cloud & Tools', 'Intermediate'),
    ('Git/GitHub', 'Cloud & Tools', 'Intermediate'),
    ('Django', 'Cloud & Tools', 'Intermediate'),
    # Soft Skills
    ('Business Communication', 'Soft Skills', 'Advanced'),
    ('Problem Solving', 'Soft Skills', 'Expert'),
    ('Project Management', 'Soft Skills', 'Intermediate'),
]

for skill_name, category, proficiency in skills_data:
    if not Skill.objects.filter(name=skill_name).exists():
        Skill.objects.create(name=skill_name, category=category, proficiency=proficiency)
        print(f"Skill '{skill_name}' created!")
    else:
        print(f"Skill '{skill_name}' already exists!")

# Add experience
experience_data = [
    {
        'title': 'Student Worker – Data Processor',
        'company': 'Baylor University',
        'location': 'Waco, Texas',
        'start_date': date(2025, 8, 1),
        'end_date': None,
        'description': 'Review and process incoming domestic high school transcripts, accurately entering applicant academic data into institutional systems. Review and validate data captured through image recognition/OCR technology. Strengthening reporting discipline, organizational skills, and attention to detail in a fast-paced operational environment.',
        'is_current': True,
    }
]

for exp_data in experience_data:
    # Check if experience already exists (by title and company)
    if not Experience.objects.filter(title=exp_data['title'], company=exp_data['company']).exists():
        Experience.objects.create(**exp_data)
        print(f"Experience '{exp_data['title']}' created!")
    else:
        print(f"Experience '{exp_data['title']}' already exists!")

print("\nDatabase setup complete!")
print("To access the admin panel, visit: http://localhost:8000/admin")
