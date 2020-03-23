from rest_framework import serializers

from .models import Consultation


class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultation
        fields = ['id', 'day', 'hour', 'created', 'doctor']
        depth = 2
