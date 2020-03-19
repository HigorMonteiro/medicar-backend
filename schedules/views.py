from rest_framework import generics, filters

from .serializers import ScheduleSerializer
from .models import Schedule


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['doctor__name']
