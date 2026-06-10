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