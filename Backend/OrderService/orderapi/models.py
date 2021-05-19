from ast import copy_location
from django.db import models
from django.db.models import manager
from uuid import uuid4

# Create your models here.


class Address(models.Model):
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    def __str__(self):
        return self.lat + ":" + self.lng


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
    id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.CharField(max_length=9, choices=STATUS, default=INIT)
    client_id = models.CharField(max_length=100, default="")
    order_txt = models.CharField(max_length=100, default="")
    pick_up_location = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="pick_up_location"
    )
    delivery_location = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="delivery_location",
        null=True,
    )
    pick_up_description = models.CharField(max_length=100, null=True)
    courier_id = models.CharField(max_length=100, default="")

    def __str__(self) -> str:
        return self.order_txt
