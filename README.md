
# Retail Network API

This project is a Django REST Framework (DRF) implementation of a hierarchical network model for an electronics retail chain. It includes endpoints for managing contacts, products, network nodes (retail networks), and users.


## Table of contents

1. [Features](#features)
2. [Technologies](#techonologies)
3. [Setup Instructions](#setup_instructions)
4. [API Documentation](#api_documentation)
5. [Endpoints](#endpoins)
6. [Authentication](#authentication)
7. [Testing](#testing)
8. [License](#license)
## Features <a name="features"></a>

- **Hierarchical Network Model**: Represents a retail network with a hierarchical structure (Factory → Retail Network → Individual Entrepreneur).
- **CRUD Operations**: Create, read, update, and delete operations for contacts, products, network nodes, and users.
- **Authentication**: Token-based authentication for secure access to endpoints.
- **Filtering**: Filter network nodes by country (via related contacts).
- **Swagger Documentation**: Interactive API documentation using Swagger UI.


## Technologies <a name="techonologies" </a>

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
