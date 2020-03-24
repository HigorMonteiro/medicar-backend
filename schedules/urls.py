from django.urls import path

from .views import ScheduleList


urlpatterns = [
    path('schedule/', ScheduleList.as_view()),
]