from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Skill, Experience
import json
from datetime import datetime

# Portfolio information (hardcoded for now)
PORTFOLIO_INFO = {
    'name': 'Sean Burke',
    'title': 'MS Business Analytics Candidate & Data Analyst',
    'location': 'Waco, TX 76706',
    'email': 'sean_burke1@baylor.edu',
    'phone': '210-501-8313',
    'linkedin': 'https://www.linkedin.com/in/sean-burke53/',
    'profile_picture': 'profile_picture.jpg',
    'bio': 'MS in Business Analytics candidate with strong experience in data analysis, reporting, visualization, and statistical problem solving. Skilled in SQL, Python, R, Excel, and Tableau, with experience cleaning, validating, and analyzing data to generate accurate, actionable insights.',
    'about_short': 'Data analyst with expertise in analytics, visualization, and business intelligence.',
}

def home(request):
    """Home page view"""
    projects = Project.objects.all()[:6]  # Get latest 6 projects
    context = {
        'portfolio_info': PORTFOLIO_INFO,
        'featured_projects': projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page view"""
    context = {
        'portfolio_info': PORTFOLIO_INFO,
    }
    return render(request, 'portfolio/about.html', context)

def projects_list(request):
    """Projects listing page"""
    projects = Project.objects.all()
    context = {
        'portfolio_info': PORTFOLIO_INFO,
        'projects': projects,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, pk):
    """Individual project detail page"""
    project = get_object_or_404(Project, pk=pk)
    # Get related projects
    related_projects = Project.objects.exclude(pk=pk)[:3]
    context = {
        'portfolio_info': PORTFOLIO_INFO,
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def skills(request):
    """Skills page"""
    skills = Skill.objects.all()
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'portfolio_info': PORTFOLIO_INFO,
        'skills': skills,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/skills.html', context)

def resume(request):
    """Resume page"""
    experiences = Experience.objects.all()
    context = {
        'portfolio_info': PORTFOLIO_INFO,
        'experiences': experiences,
    }
    return render(request, 'portfolio/resume.html', context)

def contact(request):
    """Contact page"""
    context = {
        'portfolio_info': PORTFOLIO_INFO,
    }
    return render(request, 'portfolio/contact.html', context)

def chatbot(request):
    """Chatbot API endpoint"""
    from django.http import JsonResponse
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        # Simple chatbot responses - can be extended with NLP/AI
        responses = {
            'hello': 'Hello! I\'m here to help answer questions about Sean\'s portfolio. How can I assist you?',
            'projects': 'Sean has worked on several projects including chatbot development, n8n workflows, LangChain agents, and machine learning models.',
            'skills': 'Sean is skilled in Python, SQL, R, Excel, Tableau, and more. Visit the skills page for a complete list!',
            'contact': 'You can reach Sean at sean_burke1@baylor.edu or 210-501-8313.',
            'experience': 'Sean is currently a Student Worker at Baylor University and previously worked as a Data Processor.',
        }
        
        # Default response
        bot_response = 'I\'m not sure how to answer that. Feel free to ask about projects, skills, contact info, or experience!'
        
        # Simple keyword matching
        user_lower = user_message.lower()
        for key, response in responses.items():
            if key in user_lower:
                bot_response = response
                break
        
        return JsonResponse({'response': bot_response})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
