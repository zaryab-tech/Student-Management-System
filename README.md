# Student Management System:

## Project Overview
This project is a web application that allows users to perform CRUD (Create, Read, Update, Delete)
operations on student records. It incorporates AJAX for seamless data retrieval and manipulation without
page reloads and includes authentication modules to ensure secure access.

## Architecture
The application is built using the Django framework. The architecture consists of:
- Frontend: HTML, CSS, JavaScript (jQuery for AJAX)
- Backend: Python with Django
- Database: SQLite (default for Django, can be replaced with MySQL, PostgreSQL, MongoDB)

### Directory Structure

student_management/
├── enroll/
│   ├── migrations/
│   ├── templates/
│   │   └── enroll/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── form.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── student_management/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py


## Functionalities:

1. CRUD Operations: 
   - Create: Add new student details.
   - Read: View a list of existing student records and individual student details.
   - Update: Edit and update student information.
   - Delete: Remove student records from the database.
2. AJAX Integration: 
   - Perform CRUD operations asynchronously without reloading the entire web page.
3. Authentication Module: 
   - User registration, login, and logout functionalities.

##Setup Instructions:
1- Create a virtual environment and activate it:

 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2- Install the required packages:

 pip install -r requirements.txt

3- Apply migrations:

 python manage.py migrate

4- Create a superuser:

 python manage.py createsuperuser

5- Run the development server:

 python manage.py runserver


###Usage Instructions:

1- Open your web browser and navigate to http://127.0.0.1:8000/.
2- On web browser for registation navigate to http://127.0.0.1:8000/register
3- On web browser for Login navigate http://127.0.0.1:8000/login (only for admin user)
4- Use the admin interface at http://127.0.0.1:8000/admin/ for additional management.





