from django.contrib import admin
from .models import Specialty, Doctor


class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'crm', 'phone']
    list_display = ['name', 'crm', 'phone']


class SpecialtyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
