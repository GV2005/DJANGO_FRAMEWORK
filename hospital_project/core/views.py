from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm,RegistrationForm,LoginForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PatientSerializer

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

#apiview:

class PatientListAPIView(APIView):
    def get(self,request):
        patients=Patient.objects.all()

        serializer=PatientSerializer(patients,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer=PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

class PatientDetailListAPIView(APIView):
    def get(self,request,pk):
        patient=get_object_or_404(Patient,pk=pk)

        serializer=PatientSerializer(patient)

        return Response(serializer.data)
    
    def put(self,request,pk):
        patient=get_object_or_404(Patient,pk=pk)
        serializer=PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        patient=get_object_or_404(Patient,pk=pk)
        patient.delete()

        return Response({"message":"Patient deleted successfully"})
    
class PatientListView(ListView):
    model=Patient
    template_name="patient.html"
    context_object_name="patients"

from django.views.generic import DetailView

class PatientDetailView(DetailView):

    model = Patient

    template_name = "patient_detail.html"

    context_object_name = "patient"

class PatientCreateView(CreateView):
    model=Patient
    fields=[
        "name",
        "age",
        "doctor",
        "disease"
    ]
    template_name="create_patient.html"
    success_url=reverse_lazy("patient")

class PatientUpdateView(UpdateView):
    model=Patient
    fields=[
        "name",
        "age",
        "doctor",
        "disease"
    ]
    template_name="create_patient.html"
    success_url=reverse_lazy("patient")

class PatientDeleteView(DeleteView):
    model=Patient
    template_name="patient_confirm_delete.html"
    success_url=reverse_lazy("patient")


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
