from ast import copy_location
from django.db import models
from django.db.models import manager
from uuid import uuid4

# Create your models here.


class Address(models.Model):
    street_name = models.CharField(max_length=256, default="")
    street_number = models.CharField(max_length=256, default="")
    postal_code = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=256, default="")
    region = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.street_name + " " + self.street_number


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
    pick_up_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    pick_up_description = models.CharField(max_length=100, null=True)
    courier_id = models.CharField(max_length=100, default="")

    def __str__(self) -> str:
        return self.order_txt
