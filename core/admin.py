from django.contrib import admin
from .models import User, PatientProfile, DoctorProfile, HealthReading, Prescription, ServiceOrder

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(HealthReading)
admin.site.register(Prescription)
admin.site.register(ServiceOrder)
