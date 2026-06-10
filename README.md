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

# Django Learning Journey - Day 3

## Objective

Learn how Django works with databases using Models, Migrations, ORM, and the Django Admin Panel.

---

# Topics Covered

- Django Models
- SQLite Database
- Migrations
- Django ORM
- QuerySets
- Admin Panel
- Superuser Creation
- Dynamic Data Rendering
- Admin Customization

---

# Concepts Learned

## 1. Models

Created the first Django model:

```python
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

Purpose:

- Defines database structure using Python classes.
- Django automatically converts models into database tables.

---

## 2. Migrations

Generated migration files:

```bash
python manage.py makemigrations
```

Purpose:

- Creates a blueprint of database changes.

Applied migrations:

```bash
python manage.py migrate
```

Purpose:

- Applies migration changes to the database.

---

## Migration Workflow

```text
Model
  ↓
makemigrations
  ↓
Migration File
  ↓
migrate
  ↓
Database Table
```

---

# Database

Default SQLite database used:

```text
db.sqlite3
```

Patient table created automatically from the model.

---

# Django Admin Panel

Registered Patient model:

```python
from django.contrib import admin
from .models import Patient

admin.site.register(Patient)
```

Created superuser:

```bash
python manage.py createsuperuser
```

Accessed:

```text
http://127.0.0.1:8000/admin/
```

Added patient records through the admin interface.

---

# ORM Queries

Imported model:

```python
from core.models import Patient
```

---

## Get All Patients

```python
Patient.objects.all()
```

SQL Equivalent:

```sql
SELECT * FROM patient;
```

---

## Count Patients

```python
Patient.objects.count()
```

SQL Equivalent:

```sql
SELECT COUNT(*) FROM patient;
```

---

## First Patient

```python
Patient.objects.first()
```

SQL Equivalent:

```sql
SELECT * FROM patient
LIMIT 1;
```

---

## Filter Patients

```python
Patient.objects.filter(age=25)
```

SQL Equivalent:

```sql
SELECT *
FROM patient
WHERE age = 25;
```

---

## Greater Than

```python
Patient.objects.filter(age__gt=25)
```

---

## Greater Than or Equal

```python
Patient.objects.filter(age__gte=25)
```

---

## Less Than

```python
Patient.objects.filter(age__lt=25)
```

---

## Contains

```python
Patient.objects.filter(name__icontains="jo")
```

---

# Dynamic Data Rendering

## View

```python
from django.shortcuts import render
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()

    return render(
        request,
        "patients.html",
        {"patients": patients}
    )
```

---

## Template

```html
{% for patient in patients %}
    <li>
        {{ patient.name }}
        {{ patient.age }}
        {{ patient.disease }}
    </li>
{% endfor %}
```

---

# Data Flow

```text
Database
   ↓
Model
   ↓
ORM Query
   ↓
View
   ↓
Template
   ↓
Browser
```

---

# Admin Customization

## list_display

```python
list_display = (
    "name",
    "age",
    "disease"
)
```

Purpose:

- Shows model fields in table format.

---

## search_fields

```python
search_fields = (
    "name",
    "disease"
)
```

Purpose:

- Enables search functionality in admin panel.

---

## list_filter

```python
list_filter = (
    "age",
)
```

Purpose:

- Adds filtering options in admin panel.

---

# Features Built

## Patient Model

Stores:

- Name
- Age
- Disease

---

## Patient Admin Panel

Supports:

- Add Patient
- Edit Patient
- Delete Patient
- Search Patient
- Filter Patient

---

## Patient Records Page

Displays patient records dynamically from database.

---

# Key Learnings

- Models define database structure.
- Migrations manage schema changes.
- ORM converts Python queries into SQL.
- Admin Panel provides instant management UI.
- Views can send database data to templates.
- Templates can display dynamic content.
- Django dramatically reduces backend development time.

---

# Skills Acquired

✅ Create Models

✅ Create Database Tables

✅ Generate and Apply Migrations

✅ Use SQLite Database

✅ Create Superuser

✅ Use Django Admin

✅ Perform ORM Queries

✅ Filter Data

✅ Display Dynamic Data

✅ Customize Admin Panel

---

# Day 3 Outcome

Successfully built a database-driven Hospital Management application with:

- Patient Model
- SQLite Database
- Django Admin Panel
- ORM Queries
- Dynamic Patient List Page
- Search and Filter Functionality

---

# Next Step

## Day 4 - Advanced Django Admin

Topics:

- Admin Configuration
- Ordering
- Read-only Fields
- Fieldsets
- Advanced Search
- Productivity Features

Goal:

Master Django Admin customization and build professional admin dashboards.