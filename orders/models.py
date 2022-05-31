from django.db import models
from cars.models import Car
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car)
    total = models.PositiveBigIntegerField(blank=True, null=True)
    total_price = models.PositiveBigIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name) 