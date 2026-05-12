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
<img width="1883" height="867" alt="Screenshot 2026-05-12 195124" src="https://github.com/user-attachments/assets/ffffd27c-7368-4443-a502-d5423b54e1e2" />


## Report Item Page
<img width="1887" height="857" alt="repo1" src="https://github.com/user-attachments/assets/c83649df-19ec-469b-a0c8-8bde3eafe5a2" />

<img width="1887" height="875" alt="repo2" src="https://github.com/user-attachments/assets/03bddd80-1e60-4872-9859-e1c9346e7dfc" />

## Listings Page
<img width="1883" height="587" alt="lft1" src="https://github.com/user-attachments/assets/73e48229-0252-497e-9d19-5831207627f8" />
<img width="1876" height="485" alt="lft2" src="https://github.com/user-attachments/assets/ab625c91-4887-4a05-91eb-62831a61feb5" />


## Analytics Dashboard
<img width="1874" height="792" alt="Screenshot 2026-05-12 195754" src="https://github.com/user-attachments/assets/c9285d03-2445-4f57-a200-2d4951e47ee8" />

## Employee Details
<img width="1889" height="899" alt="Screenshot 2026-05-12 195920" src="https://github.com/user-attachments/assets/08cddae8-557d-4310-a33f-8b35e7244074" />


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
