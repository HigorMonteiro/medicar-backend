from django.db import models
from django.contrib.postgres.fields import ArrayField

from .validators import validate_date
from doctors.models import Doctor


class Schedule(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE)
    day = models.DateField(validators=[validate_date])
    hour = ArrayField(models.TimeField(), size=12)

    class Meta:
        unique_together = ("doctor", "day")
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return self.doctor.name
