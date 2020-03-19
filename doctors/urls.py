from django.urls import path

from .views import SpecialtyList, DoctorList


urlpatterns = [
    path('especialidades/', SpecialtyList.as_view()),
    path('medicos/', DoctorList.as_view())
]
