from django.contrib import admin
from django.urls import path
from core.views import home,about,contact,services,doctors,patient_list

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('doctors/',doctors,name='doctors'),
    path('patient/',patient_list,name='patient')


]