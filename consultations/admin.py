from django.contrib import admin
from .models import Consultation


class ConsultationAdmin(admin.ModelAdmin):
    search_fields = ['day', 'hour', 'created', 'doctor']
    list_display = ['day', 'hour', 'created', 'doctor']


admin.site.register(Consultation, ConsultationAdmin)