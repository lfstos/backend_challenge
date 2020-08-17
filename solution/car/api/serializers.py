from rest_framework import serializers
from .models import Car

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car()
        fields = ['travel', 'refuel', 'maintenance', 'create_car', 'get_car_status', 'create_tyre']
