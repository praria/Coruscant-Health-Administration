from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from .forms import CustomLoginForm, PatientRegistrationForm, DoctorRegistrationForm, EmergencyRegistrationForm
from django.contrib.auth.decorators import login_required
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
    else:
        return redirect('login')  # fallback
    
@login_required
def dashboard_patient(request):
    appointments = get_sample_appointments()
    prescriptions = get_sample_prescriptions()
    return render(request, 'dashboard/patient.html', {
        'appointments': appointments,
        'prescriptions': prescriptions
    })

@login_required
def dashboard_doctor(request):
    patients = get_sample_patients()
    return render(request, 'dashboard/doctor.html', {
        'patients': patients
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