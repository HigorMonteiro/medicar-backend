from django.urls import path

from .views import ConsultationLisView, ConsultationDestroy


urlpatterns = [
    path('consultations/', ConsultationLisView.as_view()),
    path('consultation/<int:pk>', ConsultationDestroy.as_view()),
]
