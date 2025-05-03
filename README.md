# 🏨 Coruscant Health Administration
It is a full-featured, secure, and scalable medical management system built with **Django and Tailwind CSS**. 
It enables hospitals and clinics to efficiently manage patients, doctors, departments, emergency services (Radiology and Pathology), appointments, health readings, prescriptions, service orders, and encrypted medical documents - all from role-based dashboards.
Security, document encryption, responsive design, and role-based access control are core pillars of the system

# ✨ Features 

# 1. Authentication and Authorization:
    * Secure login, registration, and logout
    * Role-based access control [Admin(super user) and admin(general), Patient, Doctor, Department, Emergency]


# 2. Patient Dashboard:
    * Submit health readings - heart rate, blood pressure, temperature etc
    * View prescriptions and service order results
    * Schedule appointment
    * Upload and view personal documents


# 3. Doctor Dashboard:
    * View and manage appointments
    * Doctors view readings and submit prescriptions for patients
    * Create service orders (x-ray, pet scan, ct scan, blood works) to departments (Radiology, Pathology) for patients
    * View service order results

# 4. Department Dashboard:
    * View assigned service orders for patients placed by doctors
    * Fulfill orders and upload results for Radiology and Pathology services

# 5. Emergency Dashboard:
    * Manage and respond to emergency cases
    * Quickly intake new patients
    
# 6. Admin Features:
    * Super Admin Dashboard:
        * Full control over the entire system via Django Admin panel
        * Manage all users (patients, doctors, emergency, department users, other admins)
        * Create, edit, and delete any user account
        * Manage appointments, prescriptions, health readings, service orders, and documents
        * View and modify all database easily
        * Assign user roles during or after registration (patient, Doctor, Emergency, Department, Admin)
        * Oversee system-wide notifications (email, push notifications if integrated)

    * General Admin Dashboard:
        * Limited adimin access (based on permissions)
        * View system data and statistics

# 7. Password Management:
    * Password reset functionality
    * Secure password update with email notifications even in development mode

# 8. Document Encryption
    * All uploaded medical documents are encrypted before being stored on the server. 
    * Only authenticated users with appropriate permissions (e.g., the uploader or an administrator) can access or delete these documents.

# 9. Responsive Design:
    * Built with Tailwind CSS for responsive beautiful UI
    * Smooth navigation and clean layouts 

# 10. Future Improvements:
    * Integrate push notifications (Firebase)
    * Switch SQLite to PostgreSQL for production


# 🛠 Tech Stack

1. Backend: Django (Python)
2. Frontend: Tailwind CSS, HTMX
3. Database: SQLite (development), easily swappable to PostgreSQL for production 
4. Encryption: Fernet encryption (cryptography library) for document security
5. Other:
    * Django's built-in authentication system
    * Widget Tweaks for form customization
    * Email backend (for password reset functionality)
6. Deployment on AWS EC2
    * GUNICORN
    * NGINX 


# 📦 Setup Instructions

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

# 🔐 Password reset configuration
    * For password reset emails in development, in settings.py, add
        * EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 🚀 Deployment on AWS EC2 with Gunicorn and Nginx
    * Prerequisites    
        * An AWS EC2 instance (Ubuntu 22.04 LTS recommended)
        * Port 80 and 22 open in the EC2 Security Group
        * SSH access to the instance
        * Django project uploaded to the EC2 instance

1. SSH into the EC2 instance
    * ssh -i your-key.pem ubuntu@your-ec2-public-ip

2. Install required packages
    * sudo apt update
    * sudo apt install python3-pip python3-venv nginx git

3. Set up the Django app
    * cd ~
    * git clone https://github.com/praria/Coruscant-Health-Administration.git
    * cd Coruscant-Health-Administration
    * python3 -m venv venv
    * source venv/bin/activate
    * pip install -r requirements.txt
    * Update the following in settings.py:
        ** ALLOWED_HOSTS = ['your-ec2-public-ip']
        ** STATIC_ROOT = BASE_DIR / 'staticfiles'
    * python manage.py collectstatic
    * python manage.py migrate

4. Install Gunicorn and Create Gunicorn systemd service
    * npm install gunicorn
    * sudo nano /etc/systemd/system/gunicorn.service

```
[Unit]
Description=gunicorn daemon for Coruscant Health Administration
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Coruscant-Health-Administration
ExecStart=/home/ubuntu/Coruscant-Health-Administration/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/home/ubuntu/Coruscant-Health-Administration/gunicorn.sock \
          coruscant_health_administration.wsgi:application

[Install]
WantedBy=multi-user.target
```
_Enable and start Gunicorn:_

```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

5. Configure Nginx
    * sudo nano /etc/nginx/sites-available/coruscant

```
server {
    listen 80;
    server_name 52.205.249.17;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /home/ubuntu/Coruscant-Health-Administration/staticfiles/;
    }

    location /media/ {
        alias /home/ubuntu/Coruscant-Health-Administration/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/Coruscant-Health-Administration/gunicorn.sock;
    }
}
```
_Enable the config and restart Nginx:_

```sudo ln -s /etc/nginx/sites-available/coruscant /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

6. Final Steps
    * Visit: http://your-ec2-public-ip/




