
from rest_framework import serializers
from .models import SpecialData


class SpecialDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpecialData
        fields = ('task_name', 'raw_data')
