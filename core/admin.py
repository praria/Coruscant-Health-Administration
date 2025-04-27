from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Appointment, User, PatientProfile, DoctorProfile, HealthReading, Prescription, ServiceOrder, MedicalDocument

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'department', 'is_staff', 'is_superuser', 'is_active')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'department')}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role', 'department')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(HealthReading)
admin.site.register(Prescription)
admin.site.register(ServiceOrder)
admin.site.register(Appointment)
admin.site.register(MedicalDocument)

