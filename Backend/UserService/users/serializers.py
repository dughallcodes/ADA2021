from django.db import models
from django.db.models import fields
from users.models import Courier, User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import logging


class CourierSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Courier.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Courier.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Courier
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__"