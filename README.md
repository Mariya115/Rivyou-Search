# Rivyou Product Search Platform

## Overview

Rivyou Product Search Platform is a Django REST Framework-based backend application that provides secure JWT authentication and an intelligent product search system. The platform is designed to rank products based on relevance, ensuring that actual products from a searched category appear before accessories or loosely related items.

---

## Features

### Authentication

* User Registration
* User Login
* User Logout
* JWT-based Authentication
* Password Hashing and Validation

### Product Search

* Relevance-based Search Ranking
* Category Match Priority
* Tag Match Support
* Name and Description Search
* Case-insensitive Search
* Partial Matching Support

### Product Management

* Get Product by ID
* Get Products by Category
* Admin Management via Django Admin Panel
* CSV Data Import

---

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite (Development)
* PostgreSQL (Production Ready)

---

## Project Structure

```text
rivyou-search/
│
├── accounts/
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── search.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── import_products.py
│
├── core/
├── manage.py
├── requirements.txt
└── products_data.csv
```

---

## Search Ranking Logic

The search system uses a three-tier relevance ranking algorithm:

### Tier 1 – Category Match (Highest Priority)

Products whose category matches the search query.

Example:

* Search: smartphone
* Category: Smartphones

Score: 0.90 – 1.00

### Tier 2 – Tag Match

Products whose tags contain the search keyword.

Example:

* Tag: smartphone

Score: 0.65 – 0.85

### Tier 3 – Name/Description Match

Products whose name or description contains the search keyword.

Score: 0.35 – 0.60

Results are sorted by relevance score in descending order.

---

## API Endpoints

### Register User

```http
POST /api/auth/register/
```

Request:

```json
{
  "username": "mariya",
  "email": "mariya@gmail.com",
  "password": "Password123"
}
```

---

### Login

```http
POST /api/auth/login/
```

Request:

```json
{
  "username": "mariya",
  "password": "Password123"
}
```

---

### Logout

```http
POST /api/auth/logout/
```

Headers:

```text
Authorization: Bearer <token>
```

---

### Search Products

```http
GET /api/products/search/?q=smartphone
```

Headers:

```text
Authorization: Bearer <token>
```

---

### Product Detail

```http
GET /api/products/<product_id>/
```

---

### Products by Category

```http
GET /api/products/category/<category>/
```

Example:

```http
GET /api/products/category/Smartphones/
```

---

## Import Product Data

Run:

```bash
python manage.py import_products products_data.csv
```

This command imports all products from the CSV dataset into the database.

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Mariya115/Rivyou-Search.git
cd Rivyou-Search
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

---

## Admin Panel

Create Superuser:

```bash
python manage.py createsuperuser
```

Access:

```text
http://127.0.0.1:8000/admin/
```

---

## Future Enhancements

* PostgreSQL Integration
* Search History Tracking
* Fuzzy Search Support
* Redis Caching
* Pagination
* Unit Test Coverage
* Docker Deployment

---

## Author

Mariya Momin

Backend Developer Intern Assignment – Rivyou Product Search Platform
