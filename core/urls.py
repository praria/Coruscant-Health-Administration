from django.urls import path
from . import views
from .views import (
    CustomLoginView,
    patient_home,
    doctor_home,
    admin_home,
    emergency_home,
)

urlpatterns = [
    path('register/patient/', views.register_patient, name='register_patient'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/emergency/', views.register_emergency, name='register_emergency'),
    path('home/', views.home_redirect_view, name='home'), 
    # Custom login view that redirects based on user.role   
    path('home/patient/', patient_home, name='home_patient'),
    path('home/doctor/', doctor_home, name='home_doctor'),
    path('home/admin/', admin_home, name='home_admin'),
    path('home/emergency/', emergency_home, name='home_emergency'),
    # dashboard routes
    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),
    path('dashboard/doctor/', views.dashboard_doctor, name='dashboard_doctor'),
    path('dashboard/emmergency/', views.dashboard_emergency, name='dashboard_emergency'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    
    path('health/submit/', views.submit_health_reading, name='submit_health_reading'),
    path('dashboard/doctor/readings/', views.view_health_readings, name='view_health_readings'),
    path('dashboard/doctor/prescribe/', views.write_prescription, name='write_prescription'),
    path('appointments/schedule/', views.schedule_appointment, name='schedule_appointment'),


]