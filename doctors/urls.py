from django.urls import path

from .views import SpecialtyList, DoctorList


urlpatterns = [
    path('specialties/', SpecialtyList.as_view()),
    path('doctors/', DoctorList.as_view())
]
