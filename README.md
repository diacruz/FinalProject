# Final Project- Pediatric Healthcare Management

The Pediatric System is a Django-based web application for managing pediatric patient records.

Requirements
Python 3.6 or higher
Django 3.0 or higher
SQLite (or any other compatible database)
Git (optional)
Installation
Clone the repository to your local machine:
bash
Copy code
git clone <repository_url>
Or download the zip file and extract it to your desired location.
Navigate to the project directory:
bash
Copy code
cd PediatricSystem
Create a virtual environment (optional but recommended):
bash
Copy code
python3 -m venv myenv
Activate the virtual environment:
On Windows:
bash
Copy code
myenv\Scripts\activate
On macOS and Linux:
bash
Copy code
source myenv/bin/activate
Install the project dependencies:
bash
Copy code
pip install -r requirements.txt
Apply the database migrations:
bash
Copy code
python manage.py migrate
Usage
Start the development server:
bash
Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000
Use the provided functionalities to manage pediatric patient records.
Testing
To run the tests, use the following command:

bash
Copy code
python manage.py test
