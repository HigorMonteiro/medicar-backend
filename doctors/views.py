from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from .models import Specialty, Doctor
from .serializers import SpecialtySerializer, DoctorSerializer


class SpecialtyList(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend]
    search_fields = ['name']
    filter_fields = ['specialty', 'specialty__id']
