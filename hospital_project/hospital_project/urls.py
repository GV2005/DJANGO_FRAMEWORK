from django.contrib import admin
from django.urls import path
from core.views import home,about,contact,services,doctors,PatientListView,PatientCreateView,PatientUpdateView,PatientDeleteView,PatientDetailView,register,user_login,user_logout

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('doctors/',doctors,name='doctors'),
    path('patient/',PatientListView.as_view(),name='patient'),
    path("patient/<int:pk>/",PatientDetailView.as_view(),name="patient_detail"),
    path('create/',PatientCreateView.as_view(),name='create_patient'),
    path('update/<int:pk>/',PatientUpdateView.as_view(),name='update_patient'),
    path('delete/<int:pk>/',PatientDeleteView.as_view(),name='delete_patient'),
    path('register/',register,name='register'),
    path('login/',user_login,name="login"),
    path('logout',user_logout,name="logout")


]