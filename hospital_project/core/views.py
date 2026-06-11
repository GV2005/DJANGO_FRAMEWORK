from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm,RegistrationForm,LoginForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")

@login_required
def doctors(request):
    return render(request,'doctors.html')

@login_required
def patient_list(request):
    patients=Patient.objects.all()

    return render(request,'patient.html',
                  {"patients":patients})

@login_required
def create_patient(request):

    if request.method=="POST":
        form=PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("patient")
        if not form.is_valid():
            print(form.errors)

        
    else:
        form=PatientForm()

    return render(request,
                  "create_patient.html",
                  {"form":form})

@login_required
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

@login_required
def delete_patient(request,id):
    patient=get_object_or_404(Patient,id=id)
    patient.delete()
    return redirect("patient")


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=RegistrationForm()
    return render(request,"register.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        form = AuthenticationForm(
    request,
    data=request.POST
)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)

                return redirect("home")
    else:
        form=LoginForm()
    return render(request,"login.html",{"form":form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")
