import time
from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import Consultation
from schedules.models import Schedule
from .serializers import ConsultationSerializer

from .filters import query_serializer


class ConsultationLisView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Consultation.objects.filter(accomplish=False)\
        .order_by('day', 'hour')
    serializer_class = ConsultationSerializer

    def get(self, request, *args, **kwargs):

        consultations_list = self.queryset.filter(user__id=request.user.id)
        for consultation in consultations_list:
            if date.today() >= consultation.day:
                if time.strftime('%H.%M:%S') > str(consultation.hour)\
                        and not consultation.accomplish:

                    obj = self.queryset.get(id=consultation.id)
                    obj.accomplish = True
                    obj.save()
        consultations = self.queryset.filter(
            accomplish=False, user__id=request.user.id)
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        schedule_id = request.data['schedule_id']
        schedule_hour = request.data['hour']+':00'
        patient = request.user
        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return Response({
                'msg': 'selected schedule was not found',
                'status': status.HTTP_404_NOT_FOUND
            })

        serializer = query_serializer(schedule, schedule_hour, patient)
        return Response(serializer.data)


class ConsultationDestroy(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.filter(accomplish=False)

    def delete(self, request, *args, **kwargs):

        if self.queryset.filter(user__id=request.user.id,
            accomplish = False, id=self.kwargs['pk']):
            return self.destroy(request, *args, **kwargs)
        return Response({
            'msg': 'selected conulstation was not found',
        })
