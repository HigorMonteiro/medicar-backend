from django.urls import path

from .views import ScheduleList


urlpatterns = [
    path('agendas/', ScheduleList.as_view()),
]