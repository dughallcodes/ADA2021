from django.db import models
from uuid import uuid4


class Address(models.Model):
    street_name = models.CharField(max_length=256, default="")
    street_number = models.CharField(max_length=256, default="")
    postal_code = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=256, default="")
    region = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.street_name + " " + self.street_number


class Courier(models.Model):
    username = models.CharField(max_length=256, default="")
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=256, default="")
    first_name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    password = models.CharField(max_length=256, default="")
    phone_number = models.CharField(max_length=256, default="")


class User(Courier):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
