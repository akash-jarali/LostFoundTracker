# Lost & Found Tracker

A comprehensive Django-based web application for managing lost and found items in an institutional environment. This project demonstrates full-stack development with a focus on usability, smart matching algorithms, and data analytics.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Smart Matching Logic](#smart-matching-logic)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionality
- **Employee Verification**: Secure reporting with employee ID validation
- **Item Reporting**: Easy form-based submission for lost and found items
- **Smart Matching**: Intelligent algorithm to suggest potential matches between lost and found items
- **Item Listings**: Comprehensive view with advanced filtering and search capabilities
- **Status Tracking**: Three-state system (Open, Matched, Closed) for item lifecycle management
- **Analytics Dashboard**: Insights into lost item patterns and recovery statistics

### User Interface
- **Responsive Design**: Bootstrap-based UI that works on all devices
- **Professional Styling**: Modern interface with Font Awesome icons and intuitive navigation
- **Interactive Elements**: Hover effects, badges, and confirmation dialogs
- **Search & Filter**: Real-time search and multi-criteria filtering

### Administrative Features
- **Employee Management**: Add, view, and remove employees from the system
- **Data Integrity**: Foreign key relationships and validation
- **Audit Trail**: Automatic timestamping of all records

## Technology Stack

- **Backend**: Python 3.12, Django 6.0
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, Font Awesome 6.4
- **JavaScript**: Bootstrap JS for interactive components
- **Deployment**: Gunicorn, Nginx (recommended for production)

## Project Structure

```
lost_found_tracker/
├── lost_found_tracker/          # Main Django project directory
│   ├── __init__.py
│   ├── settings.py             # Project settings and configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── tracker/                     # Main application
│   ├── migrations/             # Database migrations
│   ├── templates/tracker/      # HTML templates
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── __init__.py
│   ├── admin.py                # Django admin configuration
│   ├── apps.py
│   ├── models.py               # Database models
│   ├── tests.py
│   ├── urls.py                 # App-specific URL routing
│   └── views.py                # View functions
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Database Schema

### Employee Model
```python
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)  # Unique identifier
    name = models.CharField(max_length=100)                         # Full name
    department = models.CharField(max_length=100, blank=True)       # Department (optional)
```

### Item Model
```python
class Item(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),        # Item reported, no match found
        ('matched', 'Matched'),  # Potential match identified
        ('closed', 'Closed'),    # Item returned to owner
    ]
    TYPE_CHOICES = [
        ('lost', 'Lost'),        # Item reported as lost
        ('found', 'Found'),      # Item reported as found
    ]

    item_name = models.CharField(max_length=100)                    # Item name
    description = models.TextField()                                # Detailed description
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100)                    # Where lost/found
    date = models.DateField()                                      # Incident date
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Reporter
    created_at = models.DateTimeField(auto_now_add=True)          # Auto timestamp
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Clone the Repository
```bash
git clone https://github.com/yourusername/lost-found-tracker.git
cd lost-found-tracker
```

### Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Setup

### Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Add Sample Employees
```bash
python manage.py shell
```
```python
from tracker.models import Employee
Employee.objects.create(employee_id='12345', name='John Doe', department='IT')
Employee.objects.create(employee_id='67890', name='Jane Smith', department='HR')
```

## Usage

### Starting the Development Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

### Key Workflows

#### 1. Employee Management
- Navigate to "Employees" page
- Add new employees with unique IDs
- View and delete existing employees

#### 2. Reporting Items
- Go to "Report Item" page
- Enter valid Employee ID
- Fill in item details (name, description, type, location, date)
- Submit to trigger smart matching

#### 3. Viewing Listings
- Access "Listings" page
- Use search bar for text-based search
- Filter by item type and location
- Mark items as returned when resolved

#### 4. Analytics
- Visit "Insights" page
- View most commonly lost items
- Check frequent loss locations
- Monitor recovery statistics

## Smart Matching Logic

The application uses a weighted scoring system to suggest matches:

### Matching Criteria
1. **Item Name Similarity** (50 points): Exact match
2. **Location Match** (30 points): Same location
3. **Date Proximity** (20 points): Within 7 days

### Scoring Threshold
- Score ≥ 60: Status changes to "Matched"
- User receives notification of potential match
- Both items remain visible for confirmation

### Example
Lost: "Black Wallet" at "Cafeteria" on 2024-01-15
Found: "Black Wallet" at "Cafeteria" on 2024-01-16
Score: 50 (name) + 30 (location) + 20 (date) = 100 → Match suggested

## API Endpoints

While this is a traditional Django web application, here are the main URL patterns:

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | home | Landing page |
| `/report/` | report_item | Item reporting form |
| `/listings/` | listings | Item listings with filters |
| `/close/<id>/` | close_item | Mark item as returned |
| `/insights/` | insights | Analytics dashboard |
| `/employees/` | employees | Employee management |
| `/add_employee/` | add_employee | Add new employee |
| `/delete_employee/<id>/` | delete_employee | Remove employee |
| `/admin/` | Django Admin | Administrative interface |

## Testing

### Running Tests
```bash
python manage.py test
```

### Manual Testing Checklist
- [ ] Employee ID validation works
- [ ] Item reporting creates records
- [ ] Smart matching triggers correctly
- [ ] Filters and search function properly
- [ ] Status updates work
- [ ] Employee CRUD operations work
- [ ] Responsive design on mobile

## Deployment

### Production Setup
1. **Environment Variables**: Set `DEBUG=False`, `SECRET_KEY`, database credentials
2. **Static Files**: Run `python manage.py collectstatic`
3. **WSGI Server**: Use Gunicorn or uWSGI
4. **Web Server**: Configure Nginx for static files and proxy
5. **Database**: Switch to PostgreSQL/MySQL
6. **Security**: Enable HTTPS, configure CORS if needed

### Example Nginx Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/static/files/;
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write descriptive commit messages
- Add tests for new features
- Update documentation
- Ensure responsive design

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Learning Outcomes

This project demonstrates:
- Full-stack Django development
- Database design and relationships
- User interface design with Bootstrap
- Algorithm implementation (smart matching)
- Data analytics with Django ORM
- Production-ready deployment practices
- RESTful URL design
- Form validation and security
- Responsive web development

For questions or support, please open an issue on GitHub.