from django.urls import path

from .views import ScheduleList


urlpatterns = [
    path('schedules/', ScheduleList.as_view()),
]