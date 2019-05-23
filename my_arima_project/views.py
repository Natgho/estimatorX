from rest_framework import viewsets
from my_arima_project.serializers import SpecialDataSerializer
from .models import SpecialData


class SpecialDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows special data to be viewed or edited.
    """
    queryset = SpecialData.objects.all()
    serializer_class = SpecialDataSerializer
