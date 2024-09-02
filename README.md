# Book Management API

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Documentation](#documentation)
- [License](#license)
- [Contact](#contact)

## Description
A web application built with Django to manage books, including CRUD operations and API documentation with Swagger. This project provides a Django-based API for managing books with endpoints for CRUD operations. It uses Django REST Framework (DRF) for API development and includes Swagger for API documentation.

## Features
- User management and authentication
- CRUD operations for books
- API documentation with Swagger
- Token-based authentication
- Pagination and rate limiting

## Installation

**1. Verify Python and Pip versions:**
python --version
pip --version

**2. Create and activate a virtual environment:**

python -m venv test_backend
source test_backend/bin/activate

**3. Install Django and other dependencies:**

pip install django
pip install --upgrade pip  # Optional
pip install django --break-system-packages

pip install djangorestframework
pip install djangorestframework-jwt
pip install djangorestframework-simplejwt
pip install drf-yasg
pip install setuptools

4. Verify the installation of Django:

django-admin --version
python -m django --version

## Usage

**1. Create a new Django project:**

django-admin startproject book_management
cd book_management

**2. Create a new application for the API:**
python manage.py startapp books

**3. Run server **
python manage.py runserver

**4. Create tokens for users (optional):**

use UI for create users http://127.0.0.1:8000/admin/ or

python manage.py shell

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username='admin_test')  # Replace with actual username
token, created = Token.objects.get_or_create(user=user)
print(token.key)

## Testing
Run unit testing using Django's test framework:
python manage.py test

## Documentation

**a. Swager documentation **

Access Swagger documentation at http://localhost:8000/swagger/

**b. Define the Endpoints**

For a book management system, you can define the following endpoints:

- `GET /api/books/`: Retrieve a list of all books (with pagination).
- `POST /api/books/`: Create a new book.
- `GET /api/books/{id}/`: Retrieve the details of a specific book.
- `PUT /api/books/{id}/`: Update a specific book.
- `DELETE /api/books/{id}/`: Delete a specific book.

**c. Authentication and Authorization**

You can use Django REST Framework (DRF) to handle authentication and authorization. DRF provides options for basic-based authentication, session-based authentication.

**d. Installation requirements**
Please use requirements.txt for check installation.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions, you can reach me at [heroeskq3@gmail.com](mailto:heroeskq3@gmail.com).
