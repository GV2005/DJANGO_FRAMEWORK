from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from core.views import home,about,contact,services,doctors,PatientViewSet,PatientRetriveUpdateDestroyAPIView,PatientListCreateAPIView,PatientDetailListAPIView,PatientListAPIView,PatientListView,PatientCreateView,PatientUpdateView,PatientDeleteView,PatientDetailView,register,user_login,user_logout

router=DefaultRouter()
router.register("patients",PatientViewSet)

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('doctors/',doctors,name='doctors'),
    path('api/',include(router.urls)),
    path('api/v2/patients/',PatientListAPIView.as_view(),name="api_patients"),
    path('api/v2/patients/',PatientListCreateAPIView.as_view()),
    path('api/v2/patients/<int:pk>/',PatientDetailListAPIView.as_view(),name="api_detailpatients"),
    path('api/v2/patients/<int:pk>/',PatientRetriveUpdateDestroyAPIView.as_view()),
    path('patient/v1/',PatientListView.as_view(),name='patient'),
    path("patient/v1/<int:pk>/",PatientDetailView.as_view(),name="patient_detail"),
    path('create/',PatientCreateView.as_view(),name='create_patient'),
    path('update/<int:pk>/',PatientUpdateView.as_view(),name='update_patient'),
    path('delete/<int:pk>/',PatientDeleteView.as_view(),name='delete_patient'),
    path('register/',register,name='register'),
    path('login/',user_login,name="login"),
    path('logout',user_logout,name="logout")


]