from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ScheduleSerializer
from .models import Schedule


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctor']
