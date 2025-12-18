# Django Flight Routes System

This project is a Django web application developed as part of a machine test.
It models airports and flight routes in a tree-like structure and provides
features to analyze routes based on direction and duration.

---

## Features

- Create Airports
- Create Airport Routes (Left / Right) with duration
- Display airport routes in a tree-like structure
- Find the Nth Left or Right airport from a given airport
- Find the longest route based on duration
- Find the shortest route between two airports
- Form validations with clear error messages
- Clean separation of models, forms, views, and services
- Unit tests for core business logic

---

## Tech Stack

- Python 3
- Django
- SQLite
- HTML (Django Templates)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/john1808/flight_routes_project.git
cd flight_routes_project
```

##  Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```


## Install dependencies
``` bash
pip install django
```

# Run migrations
```bash
python manage.py migrate

```

# Start the development server
```bash
python manage.py runserver

```


## Application Endpoints

- GET `/add-airport/` → Add a new airport
- GET, POST `/add-route/` → Add airport routes and display tree structure
- GET, POST `/nth-node/` → Search Nth left/right airport
- GET `/longest-node/` → Display longest route based on duration
- GET, POST `/shortest-path/` → Calculate shortest route between two airports
