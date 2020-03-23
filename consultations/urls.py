from django.urls import path

from .views import ConsultationLisView, ConsultationDestroy


urlpatterns = [
    path('consultas/', ConsultationLisView.as_view()),
    path('consultas/<int:pk>', ConsultationDestroy.as_view()),
]
