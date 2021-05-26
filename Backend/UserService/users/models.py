from django.db import models
from uuid import uuid4
import datetime


class CommonUserData(models.Model):
    username = models.CharField(unique=True, max_length=256, default="")
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_name = models.CharField(max_length=256, default="")
    first_name = models.CharField(max_length=256, default="")
    email = models.CharField(unique=True, max_length=256, default="")
    password = models.CharField(max_length=256, default="")
    phone_number = models.CharField(max_length=256, default="")

    class Meta:
        abstract = True


class User(CommonUserData):
    def __str__(self):
        return self.username


class Courier(CommonUserData):
    def __str__(self):
        return self.username