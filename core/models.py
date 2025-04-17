from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
        ('ADMIN', 'Admin'),
        ('EMERGENCY', 'Emergency Services'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
class PatientProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_device_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Patient: {self.user.username}"

class DoctorProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Doctor: {self.user.username}"

class HealthReading(models.Model):
    patient = models.ForeignKey('User', on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=20)
    temperature = models.FloatField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient.username} - {self.timestamp}"

class Prescription(models.Model):
    doctor = models.ForeignKey(
        'User', 
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'DOCTOR'},
        related_name='prescriptions_given'
    )
    patient = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'PATIENT'},
        related_name='prescriptions_received'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return f"Prescription for {self.patient.username} by {self.doctor.username}"

class ServiceOrder(models.Model):
    ORDER_CHOICES = [
        ('ct_scan', 'CT Scan'),
        ('pet_scan', 'PET Scan'),
        ('x_ray', 'X-Ray'),
    ]
    patient = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'PATIENT'},
        related_name='service_orders_received'
    )
    doctor = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'DOCTOR'},
        related_name='service_orders_issued'
    )
    department = models.CharField(max_length=100)
    order_type = models.CharField(max_length=50, choices=ORDER_CHOICES)
    ordered_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.service_type} for {self.patient.username}"

