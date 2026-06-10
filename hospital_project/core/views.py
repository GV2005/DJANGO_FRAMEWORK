from django.http import HttpResponse
from django.shortcuts import render
from .models import Patient

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")

def doctors(request):
    return render(request,'doctors.html')

def patient_list(request):
    patients=Patient.objects.all()

    return render(request,'patient.html',
                  {"patients":patients})
