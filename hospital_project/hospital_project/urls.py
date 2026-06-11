from django.contrib import admin
from django.urls import path
from core.views import home,about,contact,services,doctors,patient_list,create_patient,update_patient,delete_patient,register,user_login,user_logout

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('doctors/',doctors,name='doctors'),
    path('patient/',patient_list,name='patient'),
    path('create/',create_patient,name='create_patient'),
    path('update/<int:id>/',update_patient,name='update_patient'),
    path('delete/<int:id>/',delete_patient,name='delete_patient'),
    path('register/',register,name='register'),
    path('login/',user_login,name="login"),
    path('logout',user_logout,name="logout")


]