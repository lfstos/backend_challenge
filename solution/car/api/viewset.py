from rest_framework import viewsets

from .models import Car
from .serializers import CarSerializers

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers