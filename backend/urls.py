from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('schedules.urls')),
    path('api/', include('consultations.urls')),
]
