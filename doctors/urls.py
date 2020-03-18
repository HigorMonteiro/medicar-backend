from django.urls import path

from .views import SpecialtyList


urlpatterns = [
    path('especialidades', SpecialtyList.as_view())
]
