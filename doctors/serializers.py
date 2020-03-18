from rest_framework import serializers

from .models import Doctor, Specialty


class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = ('id', 'name')
