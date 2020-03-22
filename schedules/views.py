import django_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import ScheduleSerializer
from .models import Schedule


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


class ScheduleFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='day', lookup_expr='gte')
    end_date = django_filters.DateFilter(
        field_name='day', lookup_expr='lte')
    specialty = ListFilter(field_name='doctor__specialty',
                           query_param='specialty')
    doctor = ListFilter(field_name='doctor',
                        query_param='doctor')

    class Meta:
        model = Schedule
        fields = ['specialty', 'doctor']


class ScheduleList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Schedule.objects.all().order_by('day')
    serializer_class = ScheduleSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = ScheduleFilter
