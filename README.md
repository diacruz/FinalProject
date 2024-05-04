# Pediatric Healthcare System

## Overview

The Pediatric System is a Django-based web application designed to manage pediatric patient records, appointments, and medical information.

## Requirements

- Python 3.x
- Django 3.x
- SQLite (for development)
- Other Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd PediatricSystem
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://localhost:8000/`.

## Database 
1. Python manage.py check
2. Python manage.py makemigrations
3. Python manage.py migrate

## Running Test Examples
1. ./manage.py test pedarch.tests.PatientModelTests       

## Install Reddis for Mac
1. pip install redis

## Run Reddis
1. redis-server

## License

This project is licensed under the [MIT License](LICENSE).
