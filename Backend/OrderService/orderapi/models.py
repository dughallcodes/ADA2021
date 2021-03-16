from ast import copy_location
from django.db import models
from django.db.models import manager

# Create your models here.


class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.lat) + ":" + str(self.lng)


class Client(models.Model):
    name = models.CharField(max_length=50)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name + ":" + self.phone_number


class Order(models.Model):
    INIT = "INIT"
    ASSIGNED = "ASSIGNED"
    PICKUP = "PICKUP"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    STATUS = [
        (INIT, "Order Created"),
        (ASSIGNED, "Order assigned to courier"),
        (PICKUP, "Order picked up by courier"),
        (COMPLETED, "Order completed"),
        (CANCELED, "Order was canceled"),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS, default=INIT)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, primary_key=True)
    order_txt = models.CharField(max_length=100)
    pick_up_location = models.OneToOneField(Location, on_delete=models.CASCADE)
    pick_up_description = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.order_txt + self.client.location
