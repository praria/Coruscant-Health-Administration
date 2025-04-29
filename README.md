🏨 Coruscant Health Administration
Coruscant Health Administration is a full-featured, secure, and scalable medical management system built with Django and Tailwind CSS.
It enables hospitals and clinics to efficiently manage patients, doctors, departments, emergency services (Radiology and Pathology), appointments, health readings, prescriptions, service orders, and encrypted medical documents — all from role-based dashboards.
Security, document encryption, responsive design, and role-based access control are core pillars of the system.

✨ Features
🔐 Authentication and Authorization
Secure login, registration, and logout

Role-based access control (Admin (Superuser), Admin (General), Patient, Doctor, Department, Emergency)

🏥 Patient Dashboard
Submit health readings (heart rate, blood pressure, temperature, etc.)

View prescriptions and service order results

Schedule appointments

Upload and view personal documents

🩺 Doctor Dashboard
View and manage appointments

View patient readings and submit prescriptions

Create service orders (X-ray, PET scan, CT scan, bloodwork) for patients

View service order results

🏥 Department Dashboard
View assigned service orders from doctors

Fulfill orders and upload results (Radiology and Pathology services)

🚑 Emergency Dashboard
Manage and respond to emergency cases

Quickly intake new patients

🛠️ Admin Features
Super Admin Dashboard
Full control via Django Admin Panel

Manage users (patients, doctors, emergency, department, general admins)

Create, edit, and delete user accounts

Manage appointments, prescriptions, health readings, service orders, and documents

View and modify database entries

Assign or modify user roles

Oversee system-wide notifications (email, push notifications if integrated)

General Admin Dashboard
Limited access based on assigned permissions

View system data and statistics

🔑 Password Management
Password reset functionality

Secure password updates with email notifications (even in development mode)

📄 Document Encryption
All uploaded medical documents are encrypted before being stored.

Only authenticated users (uploader or admins) can access or delete documents.

🌐 Responsive Design
Built with Tailwind CSS for a modern, mobile-friendly UI

Smooth navigation and clean layouts

🚀 Future Improvements
Integrate real push notifications (e.g., Firebase)

Switch from SQLite to PostgreSQL for production

🛠 Tech Stack
Backend: Django (Python)

Frontend: Tailwind CSS, HTMX

Database: SQLite (development), easily swappable to PostgreSQL for production

Encryption: Fernet (Cryptography library) for document security

Other Tools:

Django's built-in authentication system

Widget Tweaks (for form customization)

Email backend (for password reset functionality)

📦 Setup Instructions

# 1. Clone the repository
git clone <your-repo-url>
cd Coruscant-Health-Administration

# 2. Create and activate a virtual environment
python3 -m venv medical_venv
source medical_venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
# Make sure you have 'cryptography', 'django-widget-tweaks', etc.

# 4. Database Migration
python3 manage.py makemigrations
python3 manage.py migrate

# 5. Create a Superuser (Admin)
python3 manage.py createsuperuser

# 6. Run the development server
python3 manage.py runserver
# Visit http://127.0.0.1:8000/ in your browser

🔐 Password Reset (Development)
In your settings.py, add the following for testing password reset emails:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
This will output password reset links directly to the console.