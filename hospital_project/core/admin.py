from django.contrib import admin
from .models import Patient,Doctor,PatientProfile,Disease,Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "age",
        "department"
    )

    search_fields=(
        "name",
        "age",
        "department"
    )

    list_filter=(
        "department",
    )

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):

    search_fields=(
        "disease_name",
    )

    list_filter=(
        "disease_name",
    )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "age",
    )

    search_fields=(
        "name",
        "disease"
    )

    list_filter=(
        "age",
    )

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display=(
        "patient",
        "blood_group",
        "emergency_contact"
    )

    search_fields=(
        "patient",
        "blood_group"
    )

    list_filter=(
        "patient",
        "blood_group"
        
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=[
        "patient",
        "doctor",
        "appointment_date",
        "appointment_time",
        "reason"
    ]
    search_fields=(
        "patient",
        "doctor",
    )

    list_filter=(
        "appointment_date",
    )