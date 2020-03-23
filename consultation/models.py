from django.db import models
from django.conf import settings

from doctors.models import Doctor


class Consultation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name='User')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE)
    day = models.DateField()
    hour = models.TimeField()
    created = models.DateTimeField('Created on', auto_now_add=True)
    accomplish = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'

    def __str__(self):
        return self.day + '-' + self.hour
