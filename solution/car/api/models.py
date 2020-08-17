from django.db import models

# Create your models here.


class Car(models.Model):
    # tyres = models.IntegerField(null=True)
    # liters = models.IntegerField(null=True)
    # total_km = models.IntegerField(null=True)
    # disagree = models.IntegerField(null=True)
    # piece = models.CharField(max_length=10, null=True)

    travel = models.CharField(null=True, max_length=50)
    refuel = models.CharField(null=True, max_length=50)
    maintenance = models.CharField(null=True, max_length=50)
    create_car = models.CharField(null=True, max_length=50)
    get_car_status = models.CharField(null=True, max_length=50)
    create_tyre = models.CharField(null=True, max_length=50)


    class Meta:
        db_table = 'car'