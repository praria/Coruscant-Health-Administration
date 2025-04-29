from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Auth and registration
    path('register/patient/', views.register_patient, name='register_patient'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/emergency/', views.register_emergency, name='register_emergency'),
    path('register/department/', views.register_department, name='register_department'),
     
    # Home redirects
    path('home/', views.home_redirect_view, name='home'),  
    path('home/patient/', views.patient_home, name='home_patient'),
    path('home/doctor/', views.doctor_home, name='home_doctor'),
    path('home/admin/', views.admin_home, name='home_admin'),
    path('home/emergency/', views.emergency_home, name='home_emergency'),
    path('home/department/', views.department_home, name='home_department'),
    
    # dashboards
    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),
    path('dashboard/doctor/', views.dashboard_doctor, name='dashboard_doctor'),
    path('dashboard/emergency/', views.dashboard_emergency, name='dashboard_emergency'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/department/', views.dashboard_department, name='dashboard_department'),
    
    path('health/submit/', views.submit_health_reading, name='submit_health_reading'),
    path('dashboard/doctor/readings/', views.view_health_readings, name='view_health_readings'),
    path('dashboard/doctor/prescribe/', views.write_prescription, name='write_prescription'),
    path('appointments/schedule/', views.schedule_appointment, name='schedule_appointment'),
    
    path('orders/create/', views.create_service_order, name='create_service_order'),
    path('orders/department/', views.department_orders, name='department_orders'),
    path('orders/<int:order_id>/upload-result/', views.upload_service_result, name='upload_service_result'),
    
    path('documents/', views.document_list, name='document_list'),
    path('documents/upload/', views.upload_medical_document, name='upload_medical_document'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),
    path('documents/delete/<int:document_id>/', views.delete_document, name='delete_document'),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)