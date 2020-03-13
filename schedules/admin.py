from django.contrib import admin
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'day', 'hour']


admin.site.register(Schedule, ScheduleAdmin)