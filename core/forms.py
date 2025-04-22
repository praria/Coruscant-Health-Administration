from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PatientProfile, DoctorProfile
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
