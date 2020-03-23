from django.urls import path

from .views import ConsultationLisView


urlpatterns = [
    path('consultas/', ConsultationLisView.as_view()),
]
