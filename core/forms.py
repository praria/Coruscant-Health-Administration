from django import forms
from django.forms.widgets import DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from .models import MedicalDocument, Appointment, HealthReading, Prescription, ServiceOrder, User, PatientProfile, DoctorProfile, EmergencyIntake
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
            })


class BaseUserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
            })


class PatientRegistrationForm(BaseUserRegistrationForm):
    age = forms.IntegerField()
    medical_device_id = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'PATIENT'
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                medical_device_id=self.cleaned_data['medical_device_id']
            )
        return user

class DoctorRegistrationForm(BaseUserRegistrationForm):
    specialization = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'DOCTOR'
        if commit:
            user.save()
            DoctorProfile.objects.create(
                user=user,
                specialization=self.cleaned_data['specialization'],
                license_number=self.cleaned_data['license_number']
            )
        return user

class EmergencyRegistrationForm(BaseUserRegistrationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'EMERGENCY'
        if commit:
            user.save()
        return user

class DepartmentRegisterForm(BaseUserRegistrationForm):
    department = forms.ChoiceField(choices=User.DEPARTMENT_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department']

    def clean(self):
        cleaned_data = super().clean()
        self.instance.role = 'DEPARTMENT'
        self.instance.department = cleaned_data.get('department')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'DEPARTMENT'
        user.department = self.cleaned_data['department']
        if commit:
            user.save()
        return user

    
class HealthReadingForm(forms.ModelForm):
    class Meta:
        model = HealthReading
        fields = ['heart_rate', 'blood_pressure', 'temperature', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class PrescriptionForm(forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=User.objects.filter(role='PATIENT'),
        label="Select Patient"
    )

    class Meta:
        model = Prescription
        fields = ['patient', 'instructions']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter prescription details...'}),
        }
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'scheduled_time', 'notes']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(role='DOCTOR')
        
        
class ServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['patient', 'department', 'order_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(role='PATIENT')
        
class ServiceOrderResultForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['result']
        widgets = {
            'result': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 5
            })
        }
        
        
class MedicalDocumentForm(forms.ModelForm):
    class Meta:
        model = MedicalDocument
        fields = ['file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'w-full border p-2 rounded',
                'rows': 3,
                'placeholder': 'Optional description...'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'w-full border p-2 rounded',
            }),
        }
        
        

class EmergencyIntakeForm(forms.ModelForm):
    class Meta:
        model = EmergencyIntake
        fields = ['name', 'symptoms', 'vitals']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'vitals': forms.Textarea(attrs={'rows': 2}),
        }

