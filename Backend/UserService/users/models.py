from django.db import models
from uuid import uuid4


class Address(models.Model):
    street_name = models.CharField(max_length=100, default="")
    street_number = models.CharField(max_length=100, default="")
    postal_code = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    region = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.street_name + " " + self.street_number


class BasicUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=257, default="")
    phone_number = models.CharField(max_length=11, default="")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
