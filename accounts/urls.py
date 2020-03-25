from django.urls import path

from .views import UserCreate, UserLogin


urlpatterns = [
    path('auth/login/', UserLogin.as_view()),
    path('auth/register/', UserCreate.as_view())
]
