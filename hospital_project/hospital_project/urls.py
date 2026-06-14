from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from core.views import home,about,contact,services,doctors,AppointmentViewSet,AppointmentDeleteView,AppointmentUpdateView,AppointmentCreateView,AppointmentDetailView,AppointmentListView,PatientViewSet,PatientRetriveUpdateDestroyAPIView,PatientListCreateAPIView,PatientDetailListAPIView,PatientListAPIView,PatientListView,PatientCreateView,PatientUpdateView,PatientDeleteView,PatientDetailView,register,user_login,user_logout

router=DefaultRouter()
router.register("patients",PatientViewSet)
router.register("appointments",AppointmentViewSet)

urlpatterns=[
    path('admin/',admin.site.urls),
    path('api/',include(router.urls)),
    path('register/',register,name='register'),
    path('login/',user_login,name="login"),
    path('logout',user_logout,name="logout"),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('doctors/',doctors,name='doctors'),
    # path('api/v2/patients/',PatientListAPIView.as_view(),name="api_patients"),
    # path('api/v2/patients/',PatientListCreateAPIView.as_view()),
    # path('api/v2/patients/<int:pk>/',PatientDetailListAPIView.as_view(),name="api_detailpatients"),
    # path('api/v2/patients/<int:pk>/',PatientRetriveUpdateDestroyAPIView.as_view()),
    path('patients/',PatientListView.as_view(),name='patient'),
    path("patients/<int:pk>/",PatientDetailView.as_view(),name="patient_detail"),
    path('patients_c/',PatientCreateView.as_view(),name='create_patient'),
    path('patients/<int:pk>/',PatientUpdateView.as_view(),name='update_patient'),
    path('patients_d/<int:pk>/',PatientDeleteView.as_view(),name='delete_patient'),
    path('appointments/',AppointmentListView.as_view(),name="appointments"),
    path('appointments/<int:pk>/',AppointmentDetailView.as_view(),name="appointment_detail"),
    path('appointments_b/',AppointmentCreateView.as_view(),name="book_appointment"),
    path('appointments/<int:pk>/',AppointmentUpdateView.as_view(),name="update_appointment"),
    path('appointments_d/<int:pk>/',AppointmentDeleteView.as_view(),name="delete_appointment")



]