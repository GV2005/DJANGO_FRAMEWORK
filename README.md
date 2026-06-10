# Django Learning Journey - Day 1

## Objective
Learn Django fundamentals by creating the first Django project, understanding the project structure, creating an app, configuring URLs, and building basic pages.

---

## Topics Covered

- Django Installation
- Creating a Django Project
- Understanding Project Structure
- Creating a Django App
- Registering Apps in Django
- URL Routing
- Function-Based Views
- Returning HTTP Responses
- Running the Development Server

---

## Project Structure

```text
hospital_project/
│
├── manage.py
│
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│
└── hospital_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
```

---

## Commands Learned

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Django

```bash
pip install django
```

### Verify Installation

```bash
django-admin --version
```

### Create Django Project

```bash
django-admin startproject hospital_project
```

### Create Django App

```bash
python manage.py startapp core
```

### Run Development Server

```bash
python manage.py runserver
```

---

## Django Files Learned

### manage.py

Used to execute Django commands.

Examples:

```bash
python manage.py runserver
python manage.py startapp core
python manage.py migrate
```

### settings.py

Contains project configuration such as:

- Installed Apps
- Database Settings
- Security Settings
- Static Files

### urls.py

Handles URL routing.

Example:

```python
path('', home)
```

### views.py

Contains application logic.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Hospital Management System")
```

---

## Pages Created

### Home Page

URL:

```text
/
```

Output:

```text
Welcome to Hospital Management System
```

### About Page

URL:

```text
/about/
```

Output:

```text
Welcome to the About Page of the Hospital
```

### Contact Page

URL:

```text
/contact/
```

Output:

```text
Contact us at abc@gmail.com
```

---

## Request Flow in Django

```text
Browser Request
       ↓
urls.py
       ↓
views.py
       ↓
HttpResponse
       ↓
Browser
```

---

## Key Learnings

- A Django Project can contain multiple Apps.
- URLs are mapped in urls.py.
- Views contain application logic.
- HttpResponse sends data back to the browser.
- manage.py is used to execute Django commands.
- Django follows a structured and scalable architecture.

---

## Day 1 Outcome

Successfully:

- Installed Django 6.0.6
- Created first Django project
- Created first Django app
- Configured URL routing
- Built Home, About, and Contact pages
- Understood Django request flow

---

## Next Step

Day 2: Templates, HTML Pages, Template Inheritance, and Building a Multi-Page Hospital Website.

# Django Learning Journey - Day 2

## Objective

Learn how Django renders HTML pages using templates, build a multi-page website, implement template inheritance, and create reusable layouts using a base template.

---

# Topics Covered

- Django Templates
- render() Function
- HTML Templates
- Multiple Pages
- URL Routing
- Template Inheritance
- Base Template
- Named URLs
- Navigation Bar
- Basic Styling

---

# Concepts Learned

## 1. render()

Before:

```python
return HttpResponse("Welcome")
```

Returns plain text directly to the browser.

After:

```python
return render(request, "home.html")
```

Loads an HTML template and sends the rendered page to the browser.

---

## 2. Templates

Created HTML pages inside:

```text
core/
└── templates/
```

Templates Created:

```text
home.html
about.html
services.html
contact.html
doctors.html
base.html
```

---

## 3. Multiple Page Routing

Configured routes for:

```text
/
about/
services/
contact/
doctors/
```

Example:

```python
path('about/', about, name='about')
```

---

## 4. Template Inheritance

Created a common layout using:

```html
base.html
```

Child templates inherit from it:

```html
{% extends 'base.html' %}
```

Content is inserted using:

```html
{% block content %}
{% endblock %}
```

Benefits:

- Avoid duplicate HTML code
- Easier maintenance
- Consistent website layout

---

## 5. Named URLs

Instead of:

```html
<a href="/about/">
```

Used:

```html
<a href="{% url 'about' %}">
```

Advantages:

- Dynamic URL generation
- Easier maintenance
- No hardcoded links

---

# Project Structure

```text
hospital_project/

├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── services.html
│   │   ├── contact.html
│   │   └── doctors.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── hospital_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# Pages Created

## Home Page

```text
/
```

Displays hospital welcome page.

---

## About Page

```text
/about/
```

Displays information about the hospital.

---

## Services Page

```text
/services/
```

Displays healthcare services.

---

## Contact Page

```text
/contact/
```

Displays hospital contact details.

---

## Doctors Page

```text
/doctors/
```

Displays available doctors.

---

# Navigation Bar

Implemented reusable navigation links:

```html
Home
About
Services
Contact
Doctors
```

Available automatically on every page through template inheritance.

---

# Request Flow

```text
Browser Request
        ↓
urls.py
        ↓
views.py
        ↓
render()
        ↓
HTML Template
        ↓
Browser
```

---

# Key Learnings

- Templates are used to create web pages.
- render() loads HTML templates.
- Template inheritance prevents code duplication.
- base.html acts as the website layout.
- Named URLs are better than hardcoded URLs.
- Navigation bars can be reused across all pages.
- Django templates help separate UI from logic.

---

# Skills Acquired

✅ Create HTML templates

✅ Use render()

✅ Configure multiple routes

✅ Create reusable layouts

✅ Implement template inheritance

✅ Use named URLs

✅ Build a multi-page Django website

✅ Create a shared navigation bar

---

# Day 2 Outcome

Successfully built a complete multi-page Hospital Management website with:

- Home Page
- About Page
- Services Page
- Contact Page
- Doctors Page

using Django Templates and Template Inheritance.

---

# Next Step

## Day 3 - Models, ORM and Database

Topics:

- Models
- SQLite Database
- Migrations
- ORM Queries
- Creating Patient Model
- Creating Doctor Model
- Database Operations

Goal:

Create real database tables and start storing healthcare data using Django ORM.