# Employee Management API (Django + JWT)

## Overview
This project is a **Django-based Employee Management System** that provides secure REST APIs for managing employees in a company.  
It demonstrates **CRUD operations**, **RESTful design**, **JWT-based authentication**, **filtering**, **pagination**, and **automated testing**.

A simple frontend UI is included for demonstration, while API security is demonstrated using **Postman**.

---

## Features
- Create, read, update, and delete employees
- JWT token-based authentication
- PostgreSQL database integration
- Filtering by department and role
- Pagination (10 employees per page)
- Automated API tests
- Clean and modular Django project structure

---

## Tech Stack
- Python 3.14
- Django 4.x
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- Bootstrap (frontend UI)
- Postman (API testing)

---

## Project Setup

### 1. Clone the Repository
    git clone <repository-url>
    cd habotconnect-employee-api

### 2 Create & Activate Virtual Environment
    python -m venv venv
    venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Configure PostgreSQL
    Update database settings in core/settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'employee_db',
            'USER': 'postgres',
            'PASSWORD': '123456789',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
### Run the Application
1. Apply Migrations
    python manage.py migrate

2. Create Superuser
    python manage.py createsuperuser

3. Start Development Server
    python manage.py runserver

Application URL:

http://127.0.0.1:8000/

### Authentication (JWT)
Obtain Token
POST

/api/token/
Request Body (JSON):

{
  "username": "admin",
  "password": "admin@123"
}
Response:

{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}

### Using Token For all protected API endpoints:
Authorization Type: Bearer Token
Value: <JWT_ACCESS_TOKEN>
Requests without token return:
401 Unauthorized
API Endpoints
### Create Employee
POST

/api/employees/
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "Engineering",
  "role": "Developer"
}
Response: 201 Created

### List Employees (Pagination & Filtering)
GET

/api/employees/?page=1&department=HR&role=Manager
Response: 200 OK

Retrieve Employee
GET

/api/employees/{id}/
Response: 200 OK
If not found: 404 Not Found

### Update Employee
PUT

/api/employees/{id}/
{
  "name": "John Updated",
  "email": "john@example.com",
  "department": "HR",
  "role": "Manager"
}
Response: 200 OK

### Delete Employee
DELETE

/api/employees/{id}/
Response: 204 No Content

### Frontend UI
    Accessible at: http://127.0.0.1:8000/
    Features:
    Add employee (modal dialog)
    Edit employee
    Delete employee
    Filter by department & role
    Pagination
Note: API authentication is demonstrated using Postman as per backend-focused requirements.

### Testing
Run automated API tests:
    python manage.py test
Tests cover:
    Employee creation
    Duplicate email validation
    Listing employees
    Retrieve by ID
    Update employee
    Delete employee
    Proper HTTP status codes