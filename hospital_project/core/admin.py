from django.contrib import admin
from .models import Patient,Doctor,PatientProfile,Disease


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
