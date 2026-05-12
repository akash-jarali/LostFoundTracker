# Lost & Found Tracker

A smart Django-based Lost & Found Management System designed for colleges, offices, and organizations to efficiently manage lost and found items.

## Live Demo

🔗 Live Website: https://akash004.pythonanywhere.com/

---

# Features

## Core Features

- Employee ID verification
- Report lost items
- Report found items
- Smart matching system
- Search and filter listings
- Item status tracking
- Employee management
- Analytics dashboard
- Responsive UI design

---

# Smart Matching System

The project includes a smart matching algorithm that compares:

- Item name
- Location
- Date proximity

### Matching Score Logic

| Criteria | Points |
|----------|--------|
| Same item name | 50 |
| Same location | 30 |
| Date within 7 days | 20 |

If total score is **60 or more**, the item is marked as **Matched**.

### Example

Lost Item:
- Black Wallet
- Cafeteria
- 2024-01-15

Found Item:
- Black Wallet
- Cafeteria
- 2024-01-16

Score:
- Name Match = 50
- Location Match = 30
- Date Match = 20

Total = 100 → Match Found

---

# Technology Stack

## Backend
- Python 3
- Django

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Font Awesome

## Database
- SQLite (Development)

## Deployment
- PythonAnywhere

---

# Project Structure

```bash
lost_found_tracker/
│
├── lost_found_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── tracker/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# Database Models

## Employee Model

```python
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
```

## Item Model

```python
class Item(models.Model):

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('matched', 'Matched'),
        ('closed', 'Closed'),
    ]

    TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    item_name = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/akash004/lost-found-tracker.git
cd lost-found-tracker
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Project

```bash
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

---

# Main Pages

| URL | Description |
|-----|-------------|
| `/` | Home Page |
| `/report/` | Report Item |
| `/listings/` | View Listings |
| `/employees/` | Employee Management |
| `/insights/` | Analytics Dashboard |
| `/admin/` | Django Admin Panel |

---

# Screenshots

## Home Page
Add screenshot here

## Report Item Page
Add screenshot here

## Listings Page
Add screenshot here

## Analytics Dashboard
Add screenshot here

---

# Future Improvements

- User authentication system
- Email notifications
- AI image matching
- REST API support
- PostgreSQL database
- QR code tracking
- Mobile application

---

# Testing Checklist

- Employee validation works
- Item reporting works
- Smart matching works
- Search filters work
- Status updates work
- Employee CRUD operations work
- Responsive design works

---

# Deployment

Project deployed using:

- PythonAnywhere
- Gunicorn
- Django WSGI

Live Link:
https://akash004.pythonanywhere.com/

---

# Learning Outcomes

This project helped in learning:

- Django full-stack development
- Database relationships
- Django ORM
- CRUD operations
- Bootstrap responsive design
- Smart matching algorithms
- Deployment process
- Form validation
- Web application architecture

---

# Author

## Akash

Student Developer passionate about Python and Django development.

---

# License

This project is licensed under the MIT License.
