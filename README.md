# Shubham Lokewar — Developer Portfolio

A modern, responsive personal portfolio website built with Django and a custom frontend.

This portfolio showcases my skills, projects, education, experience, achievements, certificates, and provides a contact form for professional opportunities.

The project was designed and developed from scratch with a focus on clean structure, responsive design, reusable Django templates, theme support, and maintainable code.

---

## 🌐 Live Portfolio

> Add your live website URL here after deployment.

**Live Demo:** Coming Soon

**GitHub:**  
https://github.com/shubhamlokewar/Portfolio

---

## ✨ Features

### Portfolio

- Modern personal portfolio homepage
- Hero section with introduction and profile image
- About section
- Education section
- Skills organized by categories
- Projects showcase
- Work experience
- Achievements
- Certificates
- Gallery
- Contact section
- Professional footer

### UI / UX

- Responsive design
- Desktop, tablet and mobile layouts
- Mobile navigation menu
- Light / Dark theme
- Persistent theme preference
- Smooth scrolling
- Hover animations
- Interactive buttons
- Responsive project cards
- Responsive skill categories
- Clean typography
- Creative visual elements
- Accessible navigation and labels

### Contact

- Django-powered contact form
- Name validation
- Email validation
- Subject field
- Message field
- Form error handling
- Success messages
- CSRF protection

### Admin

The project includes a customized Django administration interface for managing portfolio content.

Portfolio information can be managed through Django Admin instead of hard-coding content into templates.

---

# 🛠️ Tech Stack

## Backend

- Python
- Django
- Django Templates
- Django ORM
- Django Forms
- Django Admin

## Frontend

- HTML5
- CSS3
- JavaScript
- Responsive CSS
- CSS Variables
- CSS Grid
- Flexbox
- Font Awesome

## Database

- SQLite (development)

The project uses Django's ORM, making it possible to switch to another database such as PostgreSQL for production with minimal architectural changes.

## Development Tools

- Git
- GitHub
- Python Virtual Environment
- VS Code
- Django Development Server

## Fonts & Icons

- Inter
- Playfair Display
- Font Awesome

---

# 🏗️ Project Architecture

The project follows a Django-based modular structure.

```text
Portfolio/
│
├── apps/
│   │
│   ├── core/
│   │   ├── migrations/
│   │   ├── models/
│   │   ├── admin.py
│   │   ├── admin_site.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── portfolio/
│   │   ├── migrations/
│   │   ├── models/
│   │   │   ├── achievements.py
│   │   │   ├── certificates.py
│   │   │   ├── education.py
│   │   │   ├── experience.py
│   │   │   ├── gallery.py
│   │   │   ├── projects.py
│   │   │   └── skills.py
│   │   ├── admin.py
│   │   └── admin_site.py
│   │
│   └── contact/
│       ├── migrations/
│       ├── models/
│       ├── forms.py
│       ├── urls.py
│       ├── admin.py
│       └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── contact.html
│   │
│   └── home/
│       ├── hero.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── experience.html
│       └── contact_cta.html
│
├── static/
│   ├── css/
│   │   ├── main.css
│   │   ├── variables.css
│   │   ├── reset.css
│   │   ├── navbar.css
│   │   ├── hero.css
│   │   ├── about.css
│   │   ├── skills.css
│   │   ├── projects.css
│   │   ├── experience.css
│   │   ├── contact.css
│   │   ├── footer.css
│   │   ├── responsive.css
│   │   ├── animations.css
│   │   ├── creative-theme.css
│   │   └── components.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── navbar.js
│   │   └── theme.js
│   │
│   └── admin/
│       └── css/
│           └── custom_admin.css
│
├── manage.py
├── requirements.txt
├── .gitignore
└── .env.example

🧩 How The Portfolio Was Built

The portfolio was developed using Django as the main application framework and a custom HTML/CSS/JavaScript frontend.

The development was divided into several layers.

1. Django Project Setup

The project starts with a Django configuration package:

config/

This contains the main Django settings and URL configuration.

The project is started using:

python manage.py runserver
2. Modular Django Apps

Instead of keeping everything inside one application, the project separates functionality into different Django apps.

Core

The core application handles the main portfolio pages and website-level functionality.

Portfolio

The portfolio application contains the main portfolio data models.

Examples include:

Skills
Projects
Experience
Education
Achievements
Certificates
Gallery
Contact

The contact application handles the contact page and contact form.

This separation makes the project easier to maintain and extend.

🗄️ Data Modeling

Portfolio content is stored using Django models rather than being hard-coded directly into the HTML.

The portfolio contains separate model modules for different content types.

For example:

models/
├── achievements.py
├── certificates.py
├── education.py
├── experience.py
├── gallery.py
├── projects.py
└── skills.py

This allows portfolio information to be managed through Django Admin.

🎨 Frontend Architecture

The frontend is built using reusable Django templates.

A base template provides the common website structure:

base.html

The base template contains:

Navbar
Main content area
Footer
Global CSS
JavaScript
Theme initialization

The homepage then extends the base template.

home.html

The homepage is divided into reusable sections:

hero.html
about.html
skills.html
projects.html
experience.html
contact_cta.html

This prevents the homepage from becoming one large HTML file.

🎨 CSS Architecture

The CSS is separated by responsibility.

Design System
variables.css

Contains:

Colors
Typography
Spacing
Border radius
Shadows
Transitions
Global Styles
main.css

Contains:

Global layout
Containers
Sections
Typography
Global theme behavior
Component Styles

Each major section has its own stylesheet:

navbar.css
hero.css
about.css
skills.css
projects.css
experience.css
contact.css
footer.css

This makes it easier to modify one section without affecting the entire website.

🌙 Light & Dark Theme

The portfolio includes a custom light/dark theme system.

The current theme is stored on the HTML element:

<html data-theme="dark">

or:

<html data-theme="light">

CSS variables automatically change according to the selected theme.

For example:

:root {
    --color-bg: #ffffff;
    --color-text: #111827;
}

html[data-theme="dark"] {
    --color-bg: #0b0f14;
    --color-text: #f8fafc;
}

The selected theme is stored in:

localStorage

so the user's preference remains available when they return to the website.

📱 Responsive Design

The portfolio was designed to work across different screen sizes.

Desktop

Full navigation and multi-column layouts are used.

Tablet

Layouts are reduced and navigation switches to a more compact structure.

Mobile

The navigation becomes a hamburger menu.

The CSS uses:

CSS Grid
Flexbox
Media queries
Fluid typography
Flexible containers

The main responsive breakpoints include approximately:

900px
700px
600px
480px
🧭 Navigation

The navigation system contains:

Home
About
Skills
Projects
Experience
Contact

On smaller screens, the navigation becomes a mobile menu.

JavaScript controls:

Menu opening
Menu closing
Active state
Escape-key closing
Outside-click closing
Responsive reset
📬 Contact System

The contact page uses Django Forms.

The form contains:

Name
Email
Subject
Message

Django handles:

Form validation
CSRF protection
Error messages
Successful submission messages

The form is styled using the portfolio's theme variables so it works in both light and dark modes.

🛡️ Security

The project follows standard Django security practices.

Examples include:

CSRF protection
Environment variables
.env excluded from Git
Django form validation
Django ORM
Secret configuration separated from source code

Sensitive configuration should be stored in:

.env

and never committed to GitHub.

⚙️ Installation
Clone the repository
git clone https://github.com/shubhamlokewar/Portfolio.git

Move into the project:

cd Portfolio
Create a virtual environment

Windows:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

If PowerShell activation is unavailable, you can use:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Configure environment variables

Create a .env file based on:

.env.example

Add the required Django configuration and other environment-specific values.

Run migrations
python manage.py migrate
Create an admin user
python manage.py createsuperuser
Start the development server
python manage.py runserver

Then open:

http://127.0.0.1:8000/
🧑‍💻 Django Admin

The portfolio content can be managed through Django Admin.

After creating a superuser, open:

http://127.0.0.1:8000/admin/

From the admin interface you can manage portfolio information such as:

Projects
Skills
Experience
Education
Achievements
Certificates
Gallery
Social links
Profile information
🔧 Development Workflow

The project was developed iteratively.

The general workflow was:

Plan
  ↓
Django architecture
  ↓
Database models
  ↓
Admin interface
  ↓
Templates
  ↓
CSS design system
  ↓
Responsive design
  ↓
JavaScript interactions
  ↓
Light/Dark theme
  ↓
Testing & bug fixing
  ↓
Git version control
  ↓
GitHub

Each major part was tested and refined before moving to the next part.

📦 Dependencies

The project's Python dependencies are stored in:

requirements.txt

Install them with:

pip install -r requirements.txt
🧪 Testing Checklist

Before deployment, the following areas should be tested:

 Homepage loads correctly
 Navigation works
 Mobile menu works
 Tablet layout works
 Light theme works
 Dark theme works
 Theme preference persists
 Projects display correctly
 Skills display correctly
 Achievements display correctly
 Contact form validates correctly
 Resume download works
 Social links work
 Images load correctly
 Admin interface works
 No sensitive .env data is committed
🚀 Future Improvements

Possible future improvements include:

Production deployment
PostgreSQL database
Automated testing
CI/CD pipeline
Project case studies
GitHub API integration
Performance optimization
SEO improvements
Custom 404 page

These features can be added as the project evolves.

👨‍💻 About Me

Hi, I'm Shubham Lokewar.

I'm interested in building practical software solutions using development, data, and technology.

My current focus includes:

Python Development
Django
Data Analytics
SQL
Data Processing
Web Development

I'm continuously learning and improving my technical skills by building practical projects.

📫 Connect With Me
GitHub: https://github.com/shubhamlokewar
LinkedIn: https://www.linkedin.com/in/shubhamlokewar
Dev.to: https://dev.to/shubhamlokewar
📄 License

This project is a personal portfolio website.

The source code is publicly available for learning and reference. Please do not copy the portfolio design or personal content and present it as your own work.

⭐ If you find this project useful

Feel free to explore the repository and follow my development journey.

Built with Python, Django, HTML, CSS and JavaScript.

© Shubham Lokewar