import time
from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import Consultation
from .serializers import ConsultationSerializer


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
