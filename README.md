# Sean Burke Portfolio Website

A professional, full-featured portfolio website built with Django that showcases projects, skills, experience, and includes an integrated chatbot.

## Features

✨ **Project Showcase**
- Display individual projects with detailed information
- Project categories and filtering
- Links to GitHub repositories and live demos
- Beautiful project cards with responsive design

📊 **Skills & Experience**
- Comprehensive skills listing organized by category
- Experience timeline
- Resume display with downloadable options
- Proficiency levels for each skill

💬 **Interactive Chatbot**
- Embedded chatbot widget on every page
- Answers questions about projects, skills, and contact info
- Simple keyword-based responses (can be enhanced with NLP/AI)
- Floating widget design that doesn't obstruct content

🎨 **Professional Design**
- Responsive design that works on all devices
- Green color scheme matching the brand design
- Clean, modern interface with Bootstrap styling
- Smooth animations and transitions

📱 **Responsive Navigation**
- Easy-to-use navigation menu
- Mobile-friendly hamburger menu
- Quick access to all sections

## Project Structure

```
PortfolioProject3/
├── portfolio/                      # Django app
│   ├── migrations/                # Database migrations
│   ├── admin.py                   # Admin configuration
│   ├── models.py                  # Database models (Project, Skill, Experience)
│   ├── views.py                   # View functions
│   ├── urls.py                    # App URLs
│   └── templates/                 # App templates
├── portfolio_site/                # Django project settings
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Project URLs
│   └── wsgi.py
├── templates/                     # Project-wide templates
│   └── portfolio/                 # Portfolio app templates
│       ├── base.html             # Base template with navigation & chatbot
│       ├── home.html             # Home page
│       ├── about.html            # About page
│       ├── projects.html         # Projects listing
│       ├── project_detail.html   # Individual project details
│       ├── skills.html           # Skills page
│       ├── resume.html           # Resume page
│       └── contact.html          # Contact page
├── static/                        # Static files
│   ├── css/
│   │   └── style.css             # Main stylesheet
│   └── js/
│       └── chatbot.js            # Chatbot functionality
├── media/                         # User-uploaded files & profile picture
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database
├── setup_data.py                  # Script to populate initial data
├── run_server.bat                 # Batch file to start server
└── README.md                      # This file
```

## Database Models

### Project Model
- `title` - Project title
- `summary` - One-sentence summary
- `description` - Full project description
- `category` - Project category (e.g., "Web Development", "AI/ML")
- `business_problem` - Problem statement
- `tools_used` - Technologies used
- `key_features` - Major features
- `role_contribution` - Your role in the project
- `challenge` - Main challenges faced
- `lessons_learned` - Key learnings
- `image` - Project screenshot/image
- `github_link` - GitHub repository link
- `demo_link` - Live demo link
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

### Skill Model
- `name` - Skill name
- `category` - Skill category
- `proficiency` - Proficiency level (Beginner, Intermediate, Advanced, Expert)

### Experience Model
- `title` - Job title
- `company` - Company name
- `location` - Location
- `start_date` - Start date
- `end_date` - End date (optional for current positions)
- `description` - Job description
- `is_current` - Whether it's the current position

## Getting Started

### Prerequisites
- Python 3.8+ 
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd PortfolioProject3
   ```

2. **Activate the virtual environment:**
   ```bash
   # On Windows:
   .venv\Scripts\activate.bat
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **The project is pre-configured with:**
   - Database migrations applied
   - Sample projects, skills, and experience loaded
   - Admin user created (username: `admin`, password: `admin123`)
   - Static files collected

### Running the Development Server

**Option 1: Using the batch file (Windows)**
```bash
run_server.bat
```

**Option 2: Manual command**
```bash
python manage.py runserver
```

The server will start at `http://localhost:8000/`

### Accessing the Application

- **Website:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/
  - Username: `admin`
  - Password: `admin123`

## Pages & URLs

| Page | URL |
|------|-----|
| Home | `/` |
| About | `/about/` |
| Projects | `/projects/` |
| Project Detail | `/projects/<id>/` |
| Skills | `/skills/` |
| Resume | `/resume/` |
| Contact | `/contact/` |
| Admin | `/admin/` |

## Admin Panel Usage

The Django admin interface allows you to:

1. **Manage Projects**
   - Add new projects
   - Edit existing projects
   - Delete projects
   - Filter by category or date

2. **Manage Skills**
   - Add skills
   - Set proficiency levels
   - Organize by category

3. **Manage Experience**
   - Add work experience
   - Update employment history
   - Mark current positions

### How to Add a Project

1. Go to `http://localhost:8000/admin/`
2. Click on "Projects" under the Portfolio section
3. Click "Add Project"
4. Fill in all fields:
   - Title
   - Summary (one-liner)
   - Description
   - Category
   - Business Problem
   - Tools Used
   - Key Features
   - Your Role/Contribution
   - Challenge
   - Lessons Learned
   - Image (optional)
   - GitHub Link (optional)
   - Demo Link (optional)
5. Click "Save"

## Chatbot Integration

The chatbot widget is automatically included on all pages and features:

- **Floating widget:** Located in the bottom-right corner
- **Toggle functionality:** Click the header to expand/collapse
- **Keyword-based responses:** Currently uses simple keyword matching
- **Extensible:** Can be enhanced with NLP libraries like spaCy or NLTK

### Current Chatbot Keywords
- "hello" - Greeting response
- "projects" - Information about projects
- "skills" - Information about skills
- "contact" - Contact information
- "experience" - Work experience information

### Enhancing the Chatbot

To add more sophisticated AI capabilities:

1. **Install NLP libraries:**
   ```bash
   pip install spacy nltk scikit-learn
   ```

2. **Update the `chatbot()` view in `views.py`** with more advanced processing

3. **Integrate with AI APIs:**
   - OpenAI GPT
   - Google Dialogflow
   - Microsoft Bot Framework

## Customization

### Changing Colors

Edit `static/css/style.css` to modify the color scheme:
```css
:root {
    --primary-green: #1d4a2e;      /* Main green */
    --light-green: #2d5f3f;        /* Lighter green */
    --accent-gold: #d4af37;        /* Gold accent */
    --text-dark: #333;
    --text-light: #666;
    --border-color: #ddd;
}
```

### Updating Personal Information

Edit `portfolio/views.py` and update the `PORTFOLIO_INFO` dictionary:
```python
PORTFOLIO_INFO = {
    'name': 'Your Name',
    'title': 'Your Title',
    'location': 'Your Location',
    'email': 'your.email@example.com',
    'phone': 'Your Phone',
    'linkedin': 'Your LinkedIn URL',
    'profile_picture': 'your_profile_picture.jpg',
    # ...
}
```

### Adding New Pages

1. **Create a template** in `templates/portfolio/`
2. **Create a view function** in `portfolio/views.py`
3. **Add a URL pattern** in `portfolio/urls.py`
4. **Update navigation** in `templates/portfolio/base.html`

## Deployment

### Prepare for Production

1. **Update settings:**
   - Set `DEBUG = False` in `portfolio_site/settings.py`
   - Update `ALLOWED_HOSTS` with your domain
   - Use environment variables for `SECRET_KEY`

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

### Deploy to Render (Recommended)

1. Push code to GitHub
2. Create account on [Render.com](https://render.com)
3. Create new Web Service
4. Connect GitHub repository
5. Set environment variables
6. Deploy

### Other Hosting Options
- Heroku
- PythonAnywhere
- AWS (EC2, Elastic Beanstalk)
- DigitalOcean
- HostGator/Bluehost (with cPanel)

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python manage.py runserver 8001
```

### Database Errors
Reset the database:
```bash
# Remove db.sqlite3 and migrations (except __init__.py)
# Then run:
python manage.py makemigrations
python manage.py migrate
python setup_data.py
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear
```

### Admin Panel Not Accessible
Create a new superuser:
```bash
python manage.py createsuperuser
```

## Technologies Used

- **Backend:** Django 6.0
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework:** Bootstrap 5
- **Database:** SQLite3 (can be upgraded to PostgreSQL)
- **Icons:** Font Awesome
- **Image Handling:** Pillow

## Required Python Packages

- Django==6.0.4
- Pillow==10.x
- python-docx==0.8.11
- (See requirements.txt for full list)

## Contributing

To modify and improve the website:

1. Create a new branch for features
2. Make your changes
3. Test thoroughly
4. Create a pull request

## License

This project is personal and proprietary.

## Contact

For questions about this portfolio or to discuss opportunities:
- Email: sean_burke1@baylor.edu
- Phone: 210-501-8313
- LinkedIn: https://www.linkedin.com/in/sean-burke53/

---

Built with ❤️ using Django | Deployed at [Your Domain]
