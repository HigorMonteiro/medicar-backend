from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=90)

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=90)
    crm = models.CharField(max_length=7, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    specialty = models.ForeignKey(
        Specialty, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name + '-' + self.crm
