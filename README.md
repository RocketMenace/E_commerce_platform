# Retail Network API

This project is a Django REST Framework (DRF) implementation of a hierarchical network model for an electronics retail chain. It includes endpoints for managing contacts, products, network nodes (retail networks), and users.


## Table of contents

1. [Features](#features)
2. [Technologies](#techonologies)
3. [Setup Instructions](#setup_instructions)
4. [API Documentation](#api_documentation)
5. [Testing](#testing)

## Features <a name="features"></a>

- **Hierarchical Network Model**: Represents a retail network with a hierarchical structure (Factory → Retail Network → Individual Entrepreneur).
- **CRUD Operations**: Create, read, update, and delete operations for contacts, products, network nodes, and users.
- **Authentication**: Token-based authentication for secure access to endpoints.
- **Filtering**: Filter network nodes by country (via related contacts).
- **Swagger Documentation**: Interactive API documentation using Swagger UI.


## Technologies <a name="techonologies"></a>

- **Backend**: Django, Django REST Framework (DRF)

- **Database**: PostgreSQL
- **Authentication**: DRF Token Authentication
- **API Documentation**: Swagger UI (drf-yasg)
- **Testing**: Pytest 


## Setup instructions <a name="setup_instructions"></a>

## Prerequisites
- Python 3.12.3
- Poetry
- Postgresql

## Installation
**1**. **Clone the repository**
```bash
   git clone https://github.com/RocketMenace/E_commerce_platform.git
```
**2**. **Set up a virtual environment**
```bash
   poetry shell
```
**3**. **Install dependencies from pyproject.toml**
```bash
   poetry install
```
**4**. **Set up the database**
- **For Postgresql:**
    - Update **DATABASES** in **settings.py**:

```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
- Run migrations
```python
   python3 manage.py migrate
```
**5**. **Create superuser**
```python
   python3 manage.py createsuperuser
```
**6**. **Run the development server**
```python
   python3 manage.py runserver
```
**7**. **Access the API**
- Swagger UI: http://127.0.0.1:8000/swagger/

- ReDoc: http://127.0.0.1:8000/redoc/

## API Documentation <a name="api_documentation"></a>
The API documentation is available via Swagger UI and ReDoc. You can access it at:

- Swagger UI: http://127.0.0.1:8000/swagger/

- ReDoc: http://127.0.0.1:8000/redoc/
## Testing <a name="testing"></a>
```python
   pytest
```
