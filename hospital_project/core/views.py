from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Hospital Management system")

def about(request):
    return HttpResponse("welcome to the about page of the hospital")

def contact(request):
    return HttpResponse("cotact us with abc@gmail.com")