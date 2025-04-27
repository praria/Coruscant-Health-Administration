from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from core.models import Appointment, HealthReading, Prescription, ServiceOrder, MedicalDocument, User
from .forms import DepartmentRegisterForm, ServiceOrderResultForm, ServiceOrderForm, AppointmentForm, CustomLoginForm, HealthReadingForm, PatientRegistrationForm, DoctorRegistrationForm, EmergencyRegistrationForm, PrescriptionForm, MedicalDocumentForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse

from .mock_data import (
    get_sample_appointments,
    get_sample_prescriptions,
    get_sample_patients,
    get_sample_emergency_logs,
)


@login_required
def home(request):
    return render(request, 'pages/home.html') 

@login_required
def patient_home(request):
    return render(request, 'pages/home_patient.html')

@login_required
def doctor_home(request):
    return render(request, 'pages/home_doctor.html')

@login_required
def admin_home(request):
    return render(request, 'pages/home_admin.html')

@login_required
def emergency_home(request):
    return render(request, 'pages/home_emergency.html')

@login_required
def department_home(request):
    return render(request, 'pages/home_department.html')

@login_required
def home_redirect_view(request):
    role = request.user.role
    if role == 'PATIENT':
        return redirect('home_patient')
    elif role == 'DOCTOR':
        return redirect('home_doctor')
    elif role == 'EMERGENCY':
        return redirect('home_emergency')
    elif role == 'ADMIN':
        return redirect('home_admin')
    elif role == 'DEPARTMENT':
        return redirect('home_department')
    else:
        return redirect('login')  # fallback
    
@login_required
@user_passes_test(lambda u: u.role == 'PATIENT')
def dashboard_patient(request):
    # appointments = get_sample_appointments()
    # prescriptions = get_sample_prescriptions()
    prescriptions = Prescription.objects.filter(patient=request.user).order_by('-created_at')
    appointments = Appointment.objects.filter(patient=request.user).order_by('-scheduled_time')
    orders = ServiceOrder.objects.filter(patient=request.user).exclude(result='').order_by('-ordered_at')
    return render(request, 'dashboard/patient.html', {
        'appointments': appointments,
        'prescriptions': prescriptions,
        'service_orders': orders,
    })

@login_required
def dashboard_doctor(request):
    #patients = get_sample_patients()
    appointments = Appointment.objects.filter(doctor=request.user).order_by('-scheduled_time')
    prescriptions = Prescription.objects.filter(doctor=request.user).order_by('-created_at')
    orders = ServiceOrder.objects.filter(doctor=request.user).exclude(result='').order_by('-ordered_at')
    return render(request, 'dashboard/doctor.html', {
        'appointments': appointments,
        'prescriptions': prescriptions,
        'service_orders': orders,
    })

@login_required
def dashboard_emergency(request):
    logs = get_sample_emergency_logs()
    return render(request, 'dashboard/emergency.html', {
        'logs': logs
    })
    
@login_required
def dashboard_admin(request):
    User = get_user_model()
    stats = {
        'total_users': User.objects.count(),
        'total_patients': User.objects.filter(role='PATIENT').count(),
        'total_doctors': User.objects.filter(role='DOCTOR').count(),
        'total_emergency': User.objects.filter(role='EMERGENCY').count(),
    }

    recent_users = User.objects.order_by('-date_joined')[:5]

    return render(request, 'dashboard/admin.html', {
        'stats': stats,
        'recent_users': recent_users
    })
    
@login_required
@user_passes_test(lambda u: u.role == 'DEPARTMENT')
def dashboard_department(request):
    orders = ServiceOrder.objects.filter(department=request.user.department).order_by('-ordered_at')
    return render(request, 'dashboard/department.html', {'orders': orders})


def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'auth/register_patient.html', {'form': form, 'title': 'Patient'})

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'auth/register_doctor.html', {'form': form, 'title': 'Doctor'})

def register_emergency(request):
    if request.method == 'POST':
        form = EmergencyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = EmergencyRegistrationForm()
    return render(request, 'auth/register_emergency.html', {'form': form, 'title': 'Emergency'})

def register_department(request):
    if request.method == 'POST':
        form = DepartmentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = DepartmentRegisterForm()
    return render(request, 'auth/register_department.html', {'form': form, 'title': 'Department'})



class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        user = self.request.user
        print(f"Logging in user: {user.username}, is_superuser: {user.is_superuser}, role: {getattr(user, 'role', None)}")

        if user.is_superuser:
            return '/admin/'  # Django Admin

        if user.role == 'PATIENT':
            return reverse('home_patient')
        elif user.role == 'DOCTOR':
            return reverse('home_doctor')
        elif user.role == 'EMERGENCY':
            return reverse('home_emergency')
        elif user.role == 'ADMIN':
            return reverse('home_admin')

        return reverse('home')  # fallback route
    

@login_required
def submit_health_reading(request):
    if request.user.role != 'PATIENT':
        return redirect('home')  # restrict access to patients only

    if request.method == 'POST':
        form = HealthReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = request.user
            reading.save()
            return redirect('dashboard_patient')
    else:
        form = HealthReadingForm()

    return render(request, 'pages/submit_health_reading.html', {'form': form})


def is_doctor(user):
    return user.is_authenticated and user.role == 'DOCTOR'

@login_required
@user_passes_test(is_doctor)
def view_health_readings(request):
    readings = HealthReading.objects.select_related('patient').order_by('-timestamp')
    return render(request, 'dashboard/doctor_readings.html', {'readings': readings})


@login_required
@user_passes_test(lambda u: u.role == 'DOCTOR')
def write_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()
            messages.success(request, 'Prescription submitted successfully.')
            return redirect('dashboard_doctor')
    else:
        form = PrescriptionForm()

    return render(request, 'dashboard/write_prescription.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'PATIENT')
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user  # Ensure patient is logged-in user
            appointment.save()
            return redirect('home_patient') 
    else:
        form = AppointmentForm()

    return render(request, 'pages/schedule.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'DOCTOR')
def create_service_order(request):
    if request.method == 'POST':
        form = ServiceOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.doctor = request.user
            order.save()
            return redirect('home_doctor')
    else:
        form = ServiceOrderForm()
    
    return render(request, 'pages/create_service_order.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'DEPARTMENT')
def department_orders(request):
    orders = ServiceOrder.objects.filter(department=request.user.department)
    return render(request, 'pages/department_orders.html', {'orders': orders})

@login_required
@user_passes_test(lambda u: u.role == 'DEPARTMENT')
def upload_service_result(request, order_id):
    order = get_object_or_404(ServiceOrder, id=order_id, department=request.user.department)

    if request.method == 'POST':
        form = ServiceOrderResultForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Service order result uploaded successfully!")
            return redirect('dashboard_department')
    else:
        form = ServiceOrderResultForm(instance=order)

    return render(request, 'pages/upload_service_result.html', {'form': form, 'order': order})



@login_required
def upload_medical_document(request):
    if request.method == 'POST':
        form = MedicalDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            if request.user.role == 'PATIENT':
                document.patient = request.user
            elif request.user.role == 'DOCTOR':
                patient_id = request.POST.get('patient_id')
                document.patient = get_object_or_404(User, id=patient_id, role='PATIENT')
            document.save()
            return redirect('home_patient' if request.user.role == 'PATIENT' else 'home_doctor')
    else:
        form = MedicalDocumentForm()

    patients = None
    if request.user.role == 'DOCTOR':
        patients = User.objects.filter(role='PATIENT')  # Simple for now

    return render(request, 'pages/upload_document.html', {'form': form, 'patients': patients})




@login_required
def document_list(request):
    if request.user.role == 'PATIENT':
        documents = MedicalDocument.objects.filter(patient=request.user)
    elif request.user.role == 'DOCTOR':
        documents = MedicalDocument.objects.filter(uploaded_by=request.user)
    else:
        documents = MedicalDocument.objects.all() 

    return render(request, 'pages/document_list.html', {'documents': documents})

