🏨 Coruscant Health Administration
It is a full-featured, secure, and scalable medical management system built with Django and Tailwind CSS. 
It enables hospitals and clinics to efficiently manage patients, doctors, departments, emergency services (Radiology and Pathology), appointments, health readings, prescriptions, service orders, and encrypted medical documents - all from role-based dashboards.
Security, document encryption, responsive design, and role-based access control are core pillars of the system

✨ Features 

★ Authentication and Authorization:
    * Secure login, registration, and logout
    * Role-based access control [Admin(super user) and admin(general), Patient, Doctor, Department, Emergency]


★ Patient Dashboard:
    * Submit health readings - heart rate, blood pressure, temperature etc
    * View prescriptions and service order results
    * Schedule appointment
    * Upload and view personal documents


★ Doctor Dashboard:
    * View and manage appointments
    * Doctors view readings and submit prescriptions for patients
    * Create service orders (x-ray, pet scan, ct scan, blood works) to departments (Radiology, Pathology) for patients
    * View service order results

★ Department Dashboard:
    * View assigned service orders for patients placed by doctors
    * Fulfill orders and upload results for Radiology and Pathology services

★ Emergency Dashboard:
    * Manage and respond to emergency cases
    * Quickly intake new patients
    
★ Admin Features:
    * Super Admin Dashboard:
        ** Full control over the entire system via Django Admin panel
        ** Manage all users (patients, doctors, emergency, department users, other admins)
        ** Create, edit, and delete any user account
        ** Manage appointments, prescriptions, health readings, service orders, and documents
        ** View and modify all database easily
        ** Assign user roles during or after registration (patient, Doctor, Emergency, Department, Admin)
        ** Oversee system-wide notifications (email, push notifications if integrated)

    ★ General Admin Dashboard:
        ** Limited adimin access (based on permissions)
        ** View system data and statistics

★ Password Management:
    * Password reset functionality
    * Secure password update with email notifications even in development mode

★ Document Encryption
    * All uploaded medical documents are encrypted before being stored on the server. 
    * Only authenticated users with appropriate permissions (e.g., the uploader or an administrator) can access or delete these documents.

★ Responsive Design:
    * Built with Tailwind CSS for responsive beautiful UI
    * Smooth navigation and clean layouts 

★ Future Improvements:
    * Integrate push notifications (Firebase)
    * Switch SQLite to PostgreSQL for production


🛠 Tech Stack

★ Backend: Django (Python)
★ Frontend: Tailwind CSS, HTMX
★ Database: SQLite (development), easily swappable to PostgreSQL for production 
★ Encryption: Fernet encryption (cryptography library) for document security
★ Other:
    * Django's built-in authentication system
    * Widget Tweaks for form customization
    * Email backend (for password reset functionality)


📦 Setup Instructions

1. clone the repository
    * git clone 
    * cd Coruscant-Health-Administration

2. Create and Activate virtual environment
    * python3 -m venv medical_venv
    * source medical_venv/bin/activate 

3. Install Dependencies
    * pip install -r requirements.txt
    * Note: Make sure you install cryptography, widget-tweaks etc

4. Database Migration
    * python3 manage.py makemigrations
    * python3 manage.py migrate

5. Create a Superuser (Admin)
    * python3 manage.py createsuperuser

6. Run the development server
    * python manage.py runserver
    * Visit http://127.0.0.1:8000/ to access the application

🔐 Password reset configuration
    * For password reset emails in development, in settings.py, add
        * EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




