from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm

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

def create_patient(request):

    if request.method=="POST":
        form=PatientForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("patient")
        
    else:
        form=PatientForm()

    return render(request,
                  "create_patient.html",
                  {"form":form})

def update_patient(request,id):
    patient=get_object_or_404(Patient,id=id)



    if request.method=="POST":
        form=PatientForm(request.POST,instance=patient)

        if form.is_valid():
            form.save()

            return redirect("patient")
        
    else:
        form=PatientForm(instance=patient)

    return render(request,
                  "create_patient.html",
                  {"form":form})

def delete_patient(request,id):
    patient=get_object_or_404(Patient,id=id)
    patient.delete()
    return redirect("patient")