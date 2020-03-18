from rest_framework import generics, filters

from .models import Specialty
from .serializers import SpecialtySerializer


class SpecialtyList(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
