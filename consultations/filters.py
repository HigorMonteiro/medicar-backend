from datetime import datetime, date
from .models import Consultation
from rest_framework.response import Response
from .serializers import ConsultationSerializer


def query_serializer(schedule, schedule_hour, patient):
    hour_now = datetime.now().strftime('%H:%M')

    if date.today() <= schedule.day:
        if Consultation.objects.filter(
            day=schedule.day, hour=schedule_hour,
            user=patient).exists():
            return Response({'msg': 'Time already filled!'})
        elif Consultation.objects.filter(
            day=schedule.day, hour=schedule_hour,
            doctor=schedule.doctor).exists():
            return Response({'msg': 'Day and time have already been filled!'})
        else:
            consultation = Consultation.objects.create(
                day=schedule.day, hour=schedule_hour,
                doctor=schedule.doctor, user=patient)
            return ConsultationSerializer(consultation)

    return Response({'msg': 'Date and time are invalid!'})
