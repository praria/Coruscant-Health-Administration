App's core functionality:
managing patient records, scheduluding appointments
faciliate telehealth consultations, handle medical billing

users: patient, doctor, administrator, emergency services

Patient:
Performs his daily routines with a device attached to his body, Registers himself with the acknowledgment from the administrator, Uploads the data collected by the device into the database, Views his health readings, Views the suggestions prescribed by the doctor

Doctor:
Registers himself with the acknowledgment from the administrator, Views the patient record uploaded, Monitors if the patient's condition is improving or not, Prescribes solution to the patient by writing a report, Enter orders for services (pet scan, ct scan, ...)

Department: 
Receives orders: For example, patient XX needs a CT Scan, Executes orders, Uploads results of the orders.

Administrator: 
Stores patient and doctor details while registering, Creates the database tables, Upgrades the application, Monitors the application.

Emergency Services:
Inputs each new patient quickly and efficiently.

Interactivity: 
Web Page:
Allows the doctor and patient to register with the system, Allows the doctor and patient to interact
Database: 
Maintains a record of patient registration, Maintains a record of the doctor's registration, Maintains a record of the patient data and doctor feedback
Document Management:
Patients and doctors can upload documents, They need to be encrypted and stored respecting the last security standard


Django Project step by step

stage 1: Project Setup
************************

1. set up virtual environment 
-- python3 -m venv medical_venv 
-- source medical_venv/bin/activate
2. Install Django 
-- pip install django
3. start a django project
-- django_admin startproject coruscant_health_administration . 
4. run the develpment server
python3 manage.py runserver 

stage 2: App Structure and Core (business logic) Models
********************************************************

- creates a central core app
- a flexible user system with roles
- a clean data structure for medical operations
- admin dashboard to manage it all

1. create the core app 
- python manage.py startapp core

2. After changing models.py (e.g adding a field)
python3 manage.py makemigrations (it plans changes -- creates instructions)
python3 manage.py migrate (execute changes -- updates the database)

Stage 3: User Authentication and registration
*********************************************
1. update urls.py in project "coruscant_health_administration"
2. create templates directory inside core app -- mkdir -p core/templates/auth
3. create base.html file for layout reusability -- touch core/templates/base.html
4. create the login page -- touch core/templates/auth/login.html 
5. create a superuser -- python3 manage.py createsuperuser (username/ password: superuser/ superuser0310)
6. admin username/password: admin1/ administration1
6. patience's username/ password: user2/ patience2, user3/ patience3
7. doctor's username/ password: doctor2/ medical2, doctor3/ medical3
8. emergency's username/password: emergency1/department1, emmergency2/ department2

stage 4: 
pip install django-widget-tweaks




