import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Specialty, Doctor
from .serializers import SpecialtySerializer, DoctorSerializer


class ListFilter(django_filters.Filter):
    def __init__(self, query_param, *args, **kwargs):
        super(ListFilter, self).__init__(*args, **kwargs)
        self.query_param = query_param
        self.lookup_expr = 'in'

    def filter(self, queryset, value):
        try:
            request = self.parent.request
        except AttributeError:
            return None

        values = set()
        query_list = request.GET.getlist(self.query_param)
        if query_list:
            for v in query_list:
                values = values.union(set(v.split(',')))
            values = set(map(int, values))
            queryset = super(ListFilter, self).filter(queryset, values)
        return queryset


class DoctorFilter(django_filters.FilterSet):
    specialty = ListFilter(field_name='specialty',
                           query_param='specialty')

    class Meta:
        model = Doctor
        fields = ['specialty']


class SpecialtyList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class DoctorList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = DoctorFilter
